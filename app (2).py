from PIL import Image,ImageDraw,ImageFont
import numpy as np
from ultralytics import YOLO
import streamlit as st

model = YOLO('HandSignDetector.pt')
font_size = 40
img = st.file_uploader('Choose an Image')
font = ImageFont.truetype("arial.ttf", size=font_size)
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if img is not None:
    img = Image.open(img).resize((416,416)).convert('RGB')
    results = model(img)
    for result in results:
        cls = result.boxes.cls[0]
        cls = arr[int(cls)]
        lbl = result.boxes.conf[0]
        boxes = result.boxes.xyxy[0]
        draw = ImageDraw.Draw(img)
        draw.rectangle([boxes[0], boxes[1], boxes[2], boxes[3]], outline="black", width=5)
        text_position = (boxes[0]+boxes[2])/2, boxes[1]-10
        draw.text(text_position, f'{cls} {lbl}', fill="red", font=font)

    st.image(img,'Detected')