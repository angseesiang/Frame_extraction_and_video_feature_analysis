# 🎥 Video Processing Application

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-Video%20Processing-orange)](#)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Handling-green)](#)

This repository contains my training exercise on **video processing**
using **OpenCV**, **Pillow**, and **Matplotlib**.\
The project demonstrates how to load videos, extract frames, analyze
features, and save results for further use.

------------------------------------------------------------------------

## 📖 Contents

-   `video_processor.py` -- Core implementation:
    -   **VideoObject**: represents a video and its frames
    -   **Frame**: stores frame index and image
    -   **AnalysisResults**: encapsulates feature analysis results
    -   **VideoProcessor**: main class for:
        -   Loading videos
        -   Extracting frames at fixed intervals
        -   Analyzing features (e.g., average frame color)
        -   Saving results as JSON
-   `test_video_processor.py` -- Unit tests with `unittest` for:
    -   Video loading
    -   Frame extraction
    -   Feature analysis
    -   Results saving
-   `video1.mp4`, `test_video.mp4` -- Sample videos for testing
-   `results.json`, `test_results.json` -- Example outputs with average
    color values
-   `video_processor.pkl` -- Serialized processor object
-   `requirements.txt` -- Required dependencies

------------------------------------------------------------------------

## 🚀 How to Use

### 1. Clone this repository

``` bash
git clone https://github.com/your-username/video-processing-application.git
cd video-processing-application
```

### 2. Create and activate a virtual environment (recommended)

It is best practice to isolate project dependencies in a virtual
environment.

``` bash
python -m venv venv
source venv/bin/activate   # On Linux / macOS
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Run the video processor

``` bash
python video_processor.py
```

This will: - Load the video - Extract frames at fixed intervals -
Analyze average frame color - Save results to `results/results.json` -
Save the processor object to `results/video_processor.pkl`

### 5. Run tests

``` bash
python -m unittest test_video_processor.py
```

------------------------------------------------------------------------

## 🛠️ Requirements

See [`requirements.txt`](requirements.txt): - `joblib` -
`opencv-python` - `pillow` - `matplotlib`

------------------------------------------------------------------------

## 📌 Notes

-   This project was created during my **AI/ML training** to gain
    practical experience in **video processing pipelines**.
-   The example analysis extracts **average RGB color per frame**, but
    the framework can be extended to more advanced feature extraction
    tasks (e.g., object detection, motion tracking).

------------------------------------------------------------------------

## 📜 License

This repository is shared for **educational purposes**. Please credit if
you use it in your work.
