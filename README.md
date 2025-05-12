## 🗺️ tl2gpx

**Convert your Android-exported Google Timeline JSON into daily GPX tracks.**

Convert a Google Timeline JSON file (exported from Android) into **daily GPX track files**.
Each `.gpx` file represents a day of location history with standard GPS `<trk>` data, compatible with tools like **Kashmir 3D**, **Garmin BaseCamp**, or **QGIS**.

---

### ✨ Features

* ✅ Supports `semanticSegments` format used in Android timeline exports
* 📆 Automatically splits data into **daily tracks**
* 🗂️ Outputs one `.gpx` file per day
* 🧭 GPX 1.1-compliant output
* 🐍 Lightweight, no external dependencies

---

### 📥 Input Format

This tool accepts a JSON file exported from the **Android "Timeline" export feature** (not from Google Takeout).
Example top-level keys expected:

```json
{
  "semanticSegments": [...],
  "rawSignals": [...],
  "userLocationProfile": {...}
}
```

---

### 🔧 Usage

#### 1. Install Python (3.7 or higher recommended)

#### 2. Run from command line:

```bash
python tl2gpx.py <Timeline.json> <output_directory>
```

Example:

```bash
python tl2gpx.py Timeline.json gpx_output
```

* `Timeline.json`: Your exported timeline JSON file
* `gpx_output`: Directory where GPX files will be saved

---

### 📁 Output Example

After running the script, you’ll get:

```
gpx_output/
├── 2023-08-01.gpx
├── 2023-08-02.gpx
├── ...
```

Each file contains a `<trk>` element with GPS `<trkpt>` entries and timestamps.

---

### 🧪 Sample Use Cases

* Load tracks into **Garmin devices** or BaseCamp
* Analyze or overlay paths in **QGIS**

---

### 📄 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
