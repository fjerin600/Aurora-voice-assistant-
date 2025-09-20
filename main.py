import sys, threading, webbrowser, requests, numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QMovie, QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QTimer
import speech_recognition as sr
import pyttsx3
import json
import os

# -------------------------------
# Helper Functions (uses utils.py)
# -------------------------------
from utils import get_weather, get_news

# -------------------------------
# Waveform Animation Widget
# -------------------------------
class Waveform(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.amplitude = np.zeros(100)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_wave)
        self.timer.start(50)  # refresh every 50ms

    def update_wave(self):
        self.amplitude = np.roll(self.amplitude, -1)
        self.amplitude[-1] = np.random.uniform(0, 1)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(255, 255, 255))
        pen.setWidth(2)
        painter.setPen(pen)
        w = self.width()
        h = self.height()
        step = w / len(self.amplitude)
        for i, val in enumerate(self.amplitude):
            painter.drawLine(i*step, h/2, i*step, h/2 - val*50)

# -------------------------------
# Main Voice Assistant GUI
# -------------------------------
class AuroraAssistant(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aurora Voice Assistant Premium")
        self.setGeometry(100, 100, 500, 600)

        # Layout
        self.layout = QVBoxLayout()

        # Animated Mic
        self.mic_label = QLabel(self)
        self.mic_movie = QMovie("assets/mic_pulse.gif")
        self.mic_label.setMovie(self.mic_movie)
        self.mic_movie.start()
