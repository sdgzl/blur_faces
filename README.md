

---

# Face Blurring GUI with MediaPipe

This project is a Python-based graphical user interface (GUI) application that automatically detects and blurs faces in both **images** and **videos**. It leverages the power of **Google MediaPipe** for high-performance face detection and **OpenCV** for image processing.

## 🚀 Features

*   **Real-time Image Processing:** Upload any image (JPG, PNG, JPEG) and get an instantly blurred result.
*   **Video Processing:** Upload video files (MP4, AVI, MOV) to see faces being blurred frame-by-frame in real-time.
*   **High Accuracy:** Uses MediaPipe’s BlazeFace model for robust face detection.
*   **User-Friendly Interface:** Simple and clean GUI built with Tkinter.
*   **Advanced Blurring:** 
    *   Rectangular median blur for static images.
    *   Smooth elliptical mask blurring for videos to provide a more natural look.

## 🛠️ Tech Stack

*   **Python 3.x**
*   **OpenCV:** Image and video processing.
*   **MediaPipe:** ML-based face detection.
*   **Tkinter:** GUI development.
*   **Pillow (PIL):** Image handling within the interface.
*   **NumPy:** Efficient array manipulations.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sdgzl/blur_faces.git
    cd blur_faces
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install opencv-python mediapipe numpy Pillow
    ```

## 🖥️ Usage

1.  Run the application:
    ```bash
    python blur_faces.py
    ```
2.  Click on **"Upload An Image"** to process a single photo.
3.  Click on **"Upload A Video"** to select a video file and start the face-blurring playback.

## 🔍 How it Works

*   **Detection:** The app converts the input frame to RGB and passes it to `mp.solutions.face_detection`.
*   **Localization:** It retrieves the relative bounding box of the detected face and scales it to the original image dimensions.
*   **Blurring Logic:**
    *   For images, it applies `cv2.medianBlur` directly to the detected bounding box.
    *   For videos, it creates an elliptical mask to target the face area precisely, ensuring the background remains sharp while the face is obscured.

---

