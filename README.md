<div align="center">

<h1><b>Learning OpenCV — 90 Days Robotics Challenge</b></h1>

<p><em>A progressive learning workspace for Computer Vision, image processing, and human body tracking.</em></p>

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg?style=for-the-badge)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange.svg?style=for-the-badge)](https://google.github.io/mediapipe/)

</div>

<br>
<hr>

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Development Phases](#development-phases)
4. [Capstone Highlight](#capstone-highlight)
5. [Getting Started](#getting-started)
6. [Usage](#usage)
7. [Engineering Notes](#engineering-notes)
8. [Roadmap](#roadmap)
9. [Contributing](#contributing)
10. [License](#license)

---

## Overview

This workspace tracks hands-on progress through a structured 90-day robotics curriculum, covering fundamental image processing, real-time object detection, and AI-driven body landmark tracking. The codebase follows a deliberate progression — from raw pixel manipulation and NumPy array math to geometric facial meshes and full-body pose estimation using MediaPipe's ML pipeline.

Each script is a self-contained unit targeting a single concept, making the repository useful both as a personal reference and as a structured guide for engineers entering the Computer Vision domain.

### Key Features

- [x] Zero-config webcam scripts
- [x] MediaPipe Face Mesh integration
- [x] Real-time object isolation
- [x] Contour-based coin counting
- [x] Interactive HSV color picking

*Built with: `Python`, `OpenCV`, `MediaPipe`, `NumPy`, `Matplotlib`, `Pillow`.*

---

## Latest Updates

| Date | Update | Details |
|------|--------|---------|
| **May 10, 2026** | Assignment #2 Completed | Interactive image drawing utility with shape support (line, circle, rectangle, text), color selection, and save functionality |
| May 9, 2026 | Assignment #1 Completed | Grayscale image converter — load image, convert BGR to grayscale, save or display with user-selected file type |

---

## Architecture

<details>
<summary>📁 Repository structure</summary>

```text
learning_opencv/
├── AI_Face_Detector.py      # Haar Cascade face tracking
├── face_track.py            # MediaPipe Face Mesh
├── pose_track.py            # MediaPipe body landmark tracking
├── cv2_mpe.py               # Hand tracking tasks API
├── objact_isolate.py        # Color-based background masking
├── color_picker.py          # Interactive BGR to HSV utility
├── coin_counter.py          # Static image contour counting
├── webcam_counter.py        # Live webcam object counting
├── video_capture.py         # Boilerplate webcam setup & FPS
├── lec_2.py                 # Drawing matrices and shapes
├── learaning_pixal.py       # PIL/NumPy pixel manipulation
├── haarcascade_frontalface_default.xml
├── hand_landmarker.task
└── Assignments/
    ├── Assignment_no_1.py           # First assignment task
    └── assignment_no_2.py           # Image drawing utility (line, circle, rectangle, text)
```

</details>

---

## Development Phases

| Phase | Goal | Status | Outcome |
|---|---|---|---|
| Phase 1: Basics | Pixel math & shape drawing | ✅ Complete | Mastered array conversions |
| Phase 2: Object Detection | Color masking & contours | ✅ Complete | Built live coin counter |
| Phase 3: AI Tracking | Face, Pose, and Hands | 🔄 In Progress | MediaPipe meshes integrated |

> **Note:** Status indicators follow the convention: ✅ Complete · 🔄 In Progress · 🗓 Planned.

---

## Capstone Highlight

- Real-time Face Mesh generation
- Accurate HSV color isolation
- Live webcam object counting

---

## Getting Started

### Prerequisites

- Python ≥ 3.9
- Webcam (for live tracking)

### Installation

```bash
git clone https://github.com/relvixx/learning_opencv.git
cd learning_opencv
pip install opencv-python mediapipe numpy matplotlib pillow
```

---

## Usage

```bash
# Run traditional Haar Cascade Face Detection
python AI_Face_Detector.py

# Run advanced MediaPipe Pose Tracking
python pose_track.py

# Launch interactive color picker for HSV masking
# Adjust trackbar sliders to isolate a target hue range
python color_picker.py
```

> [!TIP]
> Start with `color_picker.py` before running `objact_isolate.py`. The picker outputs precise HSV lower/upper bounds that you can paste directly into the isolation script's masking parameters — no guesswork required.

---

## Engineering Notes

> [!NOTE]
> The project deliberately separates classical CV (`AI_Face_Detector.py` using Haar Cascades) from ML-based inference (`face_track.py` using MediaPipe). This dual approach makes the performance and accuracy trade-offs between the two paradigms immediately observable — a useful reference point when choosing a detection strategy for constrained hardware.

> [!IMPORTANT]
> The `hand_landmarker.task` model file must be present in the repository root at runtime. MediaPipe's `HandLandmarker` API resolves this path relatively — if you restructure directories, update the `model_asset_path` argument in `cv2_mpe.py` accordingly, or the process will exit silently.

> [!WARNING]
> Several static scripts (e.g., `coin_counter.py`) contain hardcoded absolute file paths pointing to local directories. Running them unmodified on any machine other than the original development environment will raise `FileNotFoundError`. Always audit and update image paths before executing static-image scripts.

### Known Limitations

- Hardcoded local file paths in static scripts require manual update before use on a new machine.
- Code comments include Hinglish phrasing, which may reduce readability for international contributors.

---

## Roadmap

- [ ] Refactor local file paths to relative paths
- [ ] Add ROS2 integration for physical robotics
- [ ] Build a hand-gesture volume controller

---

## Contributing

Open for feedback and educational PRs. Ensure you update file paths to relative directories before submitting.

> [!IMPORTANT]
> There is no automated test suite at this stage. Before opening a PR, manually verify that each modified script executes without errors against a live webcam feed or the expected static image input. Document any environment-specific dependencies in your PR description.

---

## License

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

Distributed under the MIT License. See `LICENSE` for full terms.

---

<div align="center">
<sub>Built with ♥ by relvixx &nbsp;·&nbsp; Learning OpenCV — 90 Days Robotics Challenge &nbsp;·&nbsp; 2026</sub>
</div>
