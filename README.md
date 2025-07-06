# 👁️ Real-Time Object Detection and Audio Guidance for Visually Impaired Individuals

**Vel Tech University | Minor Project 2 | 2025**

An intelligent vision aid system designed using real-time object detection and audio guidance to assist visually impaired individuals. This application uses YOLOv8 for object recognition and PyQt5 for GUI, providing spoken feedback to enhance mobility and safety.

---

## 📚 Table of Contents

* [Overview](#overview)
* [Technologies Used](#technologies-used)
* [Key Features](#key-features)
* [Priority Objects](#priority-objects)
* [Installation & Execution](#installation--execution)
* [Future Scope](#future-scope)

---

## 📌 Overview

This Python-based desktop application utilizes a webcam to detect real-world objects and provide real-time audio feedback to the visually impaired. Two modes are supported:

* **Navigation Mode**: Detects only priority objects essential for safe navigation
* **Detection Mode**: Detects and announces all objects in view

The user can select a mode and start/stop the camera using a simple GUI built with PyQt5.

---

## ⚙️ Technologies Used

* **Python 3.x**
* **OpenCV**
* **PyQt5** (for GUI)
* **Ultralytics YOLOv8** (for object detection)
* **pyttsx3** (for text-to-speech)
* **Threading** (for asynchronous speech)

---

## 🎯 Key Features

* 🧠 Real-time object detection using YOLOv8
* 🗣️ Speech feedback using pyttsx3
* 🎛️ Dual-mode operation: Navigation and Detection
* 🖼️ User-friendly GUI with PyQt5
* 📷 Webcam-based live feed with bounding box and labels
* 🧵 Multithreaded audio response to avoid lag

---

## 🚧 Priority Objects

Used in **Navigation Mode** for enhanced safety:

```python
PRIORITY_OBJECTS = {"person", "obstacle", "door", "mobile"}
```

Only these objects will be detected and announced in Navigation Mode.

---

## 🚀 Installation & Execution

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/vision-aid-object-detection.git
cd vision-aid-object-detection
```

2. **Install Dependencies:**

```bash
pip install pyqt5 opencv-python numpy pyttsx3 ultralytics
```

3. **Run the Application:**

```bash
python vision_aid.py
```

4. **Usage:**

* Select the desired mode (Navigation or Detection)
* Click **Start Camera** to begin detection
* The system will detect objects and speak out priority ones
* Click **Stop Camera** to exit detection mode

---

## 🔮 Future Scope

* 🌐 Add cloud model support for improved accuracy
* 🔗 Integrate with wearable devices or glasses
* 🎙️ Voice-command control for hands-free operation
* 🧠 Custom-trained YOLO model for specific indoor objects
* 📱 Develop mobile version using Kivy or Flutter

---

## 👨‍💻 Contributors

* **Rahul L** – [GitHub Profile](https://github.com/rahullakshmana/)

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE)

---

