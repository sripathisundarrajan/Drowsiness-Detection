Requirements:

Python 3.x
tkinter
customtkinter
torch
numpy
opencv-python
Pillow
pygame

Installation:
1:Clone the repository:

git clone https://github.com/sripathisundarrajan/Drowsiness-Detection

2.Navigate to the project directory:
cd drowsiness-detection

3.Install the required packages:
pip install -r requirements.txt

Usage:

1.Ensure you have a working webcam connected to your system.

2.Place the YOLOv5 model weights (last.pt) in the appropriate directory (yolov5/runs/train/exp9/weights/).

3.Place your audio files (1.wav, 2.wav, 3.wav) in the root directory of the project.

4.Run the application:
python drowsiness_detection.py

Import Libraries:
import tkinter as tk
import customtkinter as ctk
import torch
import numpy as np
import cv2
from PIL import Image, ImageTk
import pygame.mixer
import random

Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.




License
This project is licensed under the MIT License.
