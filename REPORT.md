# Computer Vision Final Project Report

**Project:** Hotdog/Not Hotdog Classifier Web Demo  
**Author:** Mattew Londono  
**Date:** May 3, 2025

---

## Overview
This project implements a minimal, robust, and free web-based image classifier that determines whether an uploaded image is a hotdog or not. The solution leverages Streamlit for the user interface and TensorFlow's MobileNetV2 pretrained on ImageNet for classification. The app is designed for easy deployment on Streamlit Community Cloud.

## Approach
- **Model:** MobileNetV2, a lightweight convolutional neural network pretrained on ImageNet, is used for fast and accurate image classification.
- **UI:** Streamlit provides a simple, interactive web interface for image upload and result display.
- **Logic:** The app only predicts "Hotdog" if the top-1 ImageNet label is "hotdog" and the confidence is above 90%. Top-3 predictions are shown for transparency. This strict threshold minimizes false positives and maximizes reliability.

## Implementation
- **File:** `streamlit_app.py` contains all app logic, including model loading, image preprocessing, prediction, and UI.
- **Requirements:** Only essential dependencies are included (`streamlit`, `tensorflow`, `pillow`, `numpy`) for fast builds and free deployment.
- **Testing:** Example images are provided in `finaltest1/` and `finaltest2/` for validation. Users can also upload their own images.

## Usage
1. Run locally with `streamlit run streamlit_app.py` after installing requirements.
2. Upload an image (JPG/PNG). The app displays the image and the top-3 predictions.
3. If the top prediction is "hotdog" with >90% confidence, the app shows "🌭 Hotdog!" Otherwise, it shows "Not Hotdog."

## Deployment
- The app is ready for free deployment on [Streamlit Community Cloud](https://streamlit.io/cloud). Simply push the repo to GitHub and connect it to Streamlit Cloud for instant, public hosting.

## Results & Discussion
- The strict 90% confidence threshold ensures high reliability, but may miss some true hotdogs if the model is not confident.
- The approach is fast, free, and easy to use, making it ideal for demonstration and educational purposes.
- Limitations: The classifier is only as good as the ImageNet labels and may not generalize to all hotdog variations.

## Conclusion
This project demonstrates how to build and deploy a practical, minimal image classifier web app using modern tools and free resources. The solution is robust, easy to maintain, and ready for public use.

---
**End of Report**
