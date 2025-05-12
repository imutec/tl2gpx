import json
import re
import os
import sys
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree
from collections import defaultdict

def load_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_daily_tracks(semantic_segments):
    segments_by_date = defaultdict(list)

    for segment in semantic_segments:
        for point in segment.get("timelinePath", []):
            point_str = point.get("point", "")
            match = re.match(r"([0-9.\-]+)°,\s*([0-9.\-]+)°", point_str)
            if not match:
                continue

            lat, lon = match.groups()
            time_str = point.get("time")
            try:
                dt = datetime.fromisoformat(time_str)
                date = dt.date().isoformat()
                segments_by_date[date].append((float(lat), float(lon), dt))
            except ValueError:
                continue

    return segments_by_date

def write_gpx_for_day(date, points, output_dir):
    gpx = Element("gpx", {
        "version": "1.1",
        "creator": "tl2gpx",
        "xmlns": "http://www.topografix.com/GPX/1/1"
    })

    trk = SubElement(gpx, "trk")
    name = SubElement(trk, "name")
    name.text = f"Track {date}"
    trkseg = SubElement(trk, "trkseg")

    for lat, lon, dt in points:
        trkpt = SubElement(trkseg, "trkpt", {
            "lat": f"{lat:.7f}",
            "lon": f"{lon:.7f}"
        })
        SubElement(trkpt, "time").text = dt.isoformat()

    file_path = os.path.join(output_dir, f"{date}.gpx")
    tree = ElementTree(gpx)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    print(f"✅ Created: {file_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python tl2gpx.py <Timeline.json> <output_directory>")
        sys.exit(1)

    input_json = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(input_json):
        print(f"❌ Input file not found: {input_json}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    data = load_json(input_json)
    semantic_segments = data.get("semanticSegments", [])
    segments_by_date = extract_daily_tracks(semantic_segments)

    for date, points in sorted(segments_by_date.items()):
        write_gpx_for_day(date, points, output_dir)

    print(f"\n✅ All GPX files have been saved to: {output_dir}/")

if __name__ == "__main__":
    main()
