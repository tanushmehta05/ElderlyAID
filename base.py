## Folder Structure Setup
import os

folders = [
    "dataset",
    "models",
    "src",
    "src/models",
    "src/utils"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Folder Created: {folder}")

# Requirements File
requirements = '''
opencv-python
mediapipe
numpy
Flask
pyttsx3
torch
yolov5
'''

with open("requirements.txt", "w") as req:
    req.write(requirements)

print("Requirements file created")

# Base Code Files
base_files = {
    "src/pose_estimation.py": """# Pose Estimation with Mediapipe
import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Placeholder for pose detection
""",

    "src/fall_detection.py": """# Fall Detection Logic
# To be implemented
""",

    "src/inactivity_detection.py": """# Inactivity Detection Logic
# To be implemented
""",

    "src/alerts.py": """# Alert System
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "ElderlyAid Alert System"

if __name__ == '__main__':
    app.run(debug=True)
""",

    "src/utils.py": """# Utility Functions
import time

# Placeholder for utilities
"""
}

for file, content in base_files.items():
    with open(file, "w") as f:
        f.write(content)
    print(f"File Created: {file}")

print("Project Setup Complete")
