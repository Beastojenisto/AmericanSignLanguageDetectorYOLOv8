# YOLOv8 American Sign Language Detection Web Application

This repository contains code for training a YOLOv8 (You Only Look Once) model for object detection, a pre-trained YOLOv8 model, code for a web application utilizing the trained model, and the dataset used for training.

## Overview

- `americansignlanguagedetector.ipynb`: Contains scripts and configuration files for training a YOLOv8 model.
- `HandSignDetector.pt`: Is a pre-trained YOLO model for object detection.
- `app.py`: Is the code for a web application that uses the trained YOLO model for real-time object detection.
- `American-Sign-Language-Letters-1`: Contains the dataset used for training the YOLO model.

## Dataset

The dataset used for training the YOLO model is available in the `American-Sign-Language-Letters-1` directory. It consists of images annotated with bounding boxes for various objects. The dataset is structured in a format suitable for training YOLO models. The dataset is not mine. You can find the dataset [here](https://universe.roboflow.com/david-lee-d0rhs/american-sign-language-letters)

## YOLO Training

The `americansignlanguagedetector.ipynb` contains scripts and configuration files for training a YOLO model. Follow the instructions in the `yolo_training/README.md` file to train the model using your dataset.

## Trained Model

The `HandSignDetector.pt` contains a pre-trained YOLO model for object detection. This model can be used directly for inference or fine-tuned on a custom dataset if needed.

## Web Application

The `app.py` directory contains code for a web application that utilizes the trained YOLO model for real-time object detection. Users can upload images, and the application will perform object detection on them. Follow the instructions in the `README.md` file to set up and run the web application locally.

## Usage

1. Train a YOLO model using your dataset by running the code in the `americansignlanguagedetector.ipynb` file.
2. Alternatively, you can use the pre-trained YOLO model provided in the `HandSignDetector.pt` file.
3. Set up and run the web application using the code in the `app.py` file.
