import sys
import cv2
import numpy as np
import threading
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QTimer
from ultralytics import YOLO
import pyttsx3

# Load YOLOv8 model
model = YOLO("yolov8s.pt")



# Priority objects for visually impaired users
PRIORITY_OBJECTS = {"person", "obstacle", "door", "mobile"}

class ObjectDetectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vision Aid - Object Detection")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.ico"))  # Set application icon
        
        # UI Elements
        self.video_label = QLabel(self)
        self.mode_selector = QComboBox(self)
        self.mode_selector.addItems(["Navigation Mode", "Detection Mode"])
        self.start_button = QPushButton("Start Camera", self)
        self.stop_button = QPushButton("Stop Camera", self)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.mode_selector)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)
        
        # Camera settings
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        
        # Button actions
        self.start_button.clicked.connect(self.start_camera)
        self.stop_button.clicked.connect(self.stop_camera)
    
    def start_camera(self):
        self.timer.start(30)
    
    def stop_camera(self):
        self.timer.stop()
        self.cap.release()
        self.video_label.clear()
    
    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        
        frame_width = frame.shape[1]
        results = model(frame)
        detected_objects = set()
        
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = model.names[int(box.cls)]
                confidence = box.conf.item()
                
                if self.mode_selector.currentText() == "Navigation Mode" and label not in PRIORITY_OBJECTS:
                    continue
                
                detected_objects.add(label)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        if detected_objects:
            description = ", ".join(detected_objects)
            self.speak_text(f"There is a : {description}")
        
        # Convert frame for PyQt display
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))
    
    def speak_text(self, text):
        threading.Thread(target=self._speak, args=(text,), daemon=True).start()
    
    def _speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ObjectDetectionApp()
    window.show()
    sys.exit(app.exec_())
