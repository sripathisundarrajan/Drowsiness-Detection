import tkinter as tk
import customtkinter as ctk 
import torch
import numpy as np
import cv2
from PIL import Image, ImageTk
import pygame.mixer
import random

app = tk.Tk()
app.geometry("600x600")
app.title("Drowsy Boi 4.0")
ctk.set_appearance_mode("dark")

vidFrame = tk.Frame(height=480, width=600)
vidFrame.pack()
vid = ctk.CTkLabel(vidFrame)
vid.pack()

counter = 0 
counterLabel = ctk.CTkLabel(master=app, text=str(counter), height=40, width=120, text_color="white", fg_color="teal")
counterLabel.pack(pady=10)

def reset_counter(): 
    global counter
    counter = 0 
resetButton = ctk.CTkButton(app, text="Reset Counter", command=reset_counter, height=40, width=120, text_color="white", fg_color="teal") 
resetButton.pack()

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp9/weights/last.pt', force_reload=True)
cap = cv2.VideoCapture(0)

# Initialize Pygame mixer
pygame.mixer.init()

# Load audio files
audio_files = [pygame.mixer.Sound(f"{i}.wav") for i in range(1, 4)]

# Define a flag to track if alarm is already triggered
alarm_triggered = False

def detect(): 
    global counter, alarm_triggered
    ret, frame = cap.read()
    if not ret or frame is None:
        # Handle empty frame
        print("Error: Unable to read frame from camera.")
        return

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    results = model(frame) 
    img = np.squeeze(results.render())

    if len(results.xywh[0]) > 0: 
        dconf = results.xywh[0][0][4]
        dclass = results.xywh[0][0][5]

        if dconf.item() > 0.85 and dclass.item() == 1.0:
            if not alarm_triggered:  # Check if alarm is not already triggered
                filechoice = random.choice(audio_files)
                filechoice.play() 
                counter += 1 
                alarm_triggered = True  # Set the flag to True to indicate alarm is triggered
        else:
            if alarm_triggered:  # Check if alarm is already triggered
                # Stop all playing sounds
                pygame.mixer.stop()
                alarm_triggered = False  # Reset the flag

    imgarr = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(imgarr) 
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10, detect) 
    counterLabel.configure(text=str(counter))  

detect()
app.mainloop()
