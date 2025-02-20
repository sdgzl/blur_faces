import cv2
import tkinter as tk
import mediapipe as mp
import numpy as np
from tkinter import filedialog
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Blur Faces")
root.geometry("600x500")

canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

def blur_face_images(image_path):
    img=cv2.imread(image_path)
    H, W, _ = img.shape
    face_detect = mp.solutions.face_detection

    with face_detect.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out = face_.process(img_rgb)

        if out.detections is not None:

            for detection in out.detections:
                location_data = detection.location_data
                bbox = location_data.relative_bounding_box
                x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                x1 = int(x1 * W)
                y1 = int(y1 * H)
                w = int(w * W)
                h = int(h * H)
                img[y1:y1 + h, x1:x1 + w, :] = cv2.medianBlur(img[y1:y1 + h, x1:x1 + w, :], 81)

    return img

def blur_face_video(frame):
        face_detect = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
        H, W, _ = frame.shape
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out = face_detect.process(img_rgb)

        if out.detections:
            mask = np.zeros((H, W), dtype=np.uint8)

            for detection in out.detections:
                location_data = detection.location_data
                bbox = location_data.relative_bounding_box
                x1 = int(bbox.xmin * W)
                y1 = int(bbox.ymin * H)
                w = int(bbox.width * W)
                h = int(bbox.height * H)
                center = (x1 + w // 2, y1 + h // 2)
                axes = (w // 2, h // 2)
                cv2.ellipse(mask, center, axes, 0, 0, 360, 255, -1)

            blurred_frame = cv2.medianBlur(frame, 51)
            frame = np.where(mask[:, :, None] == 255, blurred_frame, frame)

        return frame

def select_image() :
    image_path=filedialog.askopenfilename(filetypes=[("Image Files","*.png;*.jpg;*.jpeg")])
    blur_face_images(image_path)

    if image_path:
        img= blur_face_images(image_path)
        img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img= Image.fromarray(img)
        img= img.resize((600, 400))
        img_tk = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.image = img_tk

def select_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", ".mp4;.avi;*.mov")])

    if video_path:
        cap = cv2.VideoCapture(video_path)

        def update_frame():
            ret, frame = cap.read()

            if ret:
                frame = blur_face_video(frame)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_pil = Image.fromarray(frame_rgb)
                frame_pil = frame_pil.resize((600, 400))
                img_tk = ImageTk.PhotoImage(image=frame_pil)
                canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
                canvas.image = img_tk
                root.after(20, update_frame)

            else:
                cap.release()

        update_frame()

image_button = tk.Button(root, text="Upload An Image",command=select_image)
video_button = tk.Button(root, text="Upload A Video",command=select_video)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

video_button.grid(row=3, column=0, padx=100, pady=10, sticky="s")
image_button.grid(row=3, column=1, padx=100, pady=10, sticky="s")

root.mainloop()
