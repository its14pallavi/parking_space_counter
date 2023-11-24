from flask import Flask, render_template
import time
import cv2
import pickle
import numpy as np

app = Flask(__name__)

# Load parking space data from pickle file
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Initialize the vehicle count and parking data dictionaries
vehicleCount = 0
entry_times = {}
vehicle_states = {}

@app.route('/')
def parking_status():
    global vehicleCount, entry_times, vehicle_states

    # Replace this section with your actual code to capture and process the video feed
    cap = cv2.VideoCapture('carPark.mp4')
    ret, frame = cap.read()
    if ret:


    return render_template('index.html', posList=posList, vehicleCount=vehicleCount, entry_times=entry_times, vehicle_states=vehicle_states)

if __name__ == '__main__':
    app.run(debug=True)
