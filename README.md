# Smile-Selfie-Capture

This repository contains a Python script that uses OpenCV to perform Smile-Selfie-Capture detection using Haar cascades.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3
- OpenCV (`pip install opencv-python`)

## Usage

1. Clone the repository to your local machine:
2. git clone https://github.com/AnuragNagare/smile-selfie-capture.git 
2. Navigate to the project directory:
3. 
3. Download the Haar cascade files and place them in the `dataset` directory:

- [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- [haarcascade_smile.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml)

4. Run the script:



The script will open the webcam feed and start detecting faces and smiles in real-time. Press 'q' to exit the program.

Detected images with smiles will be saved in the `D:/Photos/Photo shoot/` (replace the path to directory to save the images)  directory with filenames starting from "DSC_0207.JPG1.jpg" and incrementing for each detected smile.








