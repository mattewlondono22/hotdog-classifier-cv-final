# Computer Vision Final Project Report

**Project Title:** Hotdog/Not Hotdog Classifier Web Application  
**Author:** Mattew Londono  
**Date:** May 3, 2025  
**GitHub Repository:** https://github.com/mattewlondono22/hotdog-classifier-cv-final  
**Live Application:** https://hotdog-classifier-cv-final.streamlit.app/

---

## 1. Introduction
The objective of this project is to develop a lightweight, web-based image classification application capable of determining whether an uploaded image depicts a hotdog. Inspired by the “Not Hotdog” app from the television series Silicon Valley, this project serves as a practical exercise in deploying machine learning models for real-world applications.

The application leverages TensorFlow’s MobileNetV2 model, pretrained on the ImageNet dataset, to perform image classification. Streamlit is utilized to create an interactive and user-friendly web interface, facilitating easy deployment and accessibility.

---

## 2. Problem Definition and Algorithm
### 2.1 Task Definition
The task involves binary image classification to determine if an input image contains a hotdog. Formally, given an input image I, the model predicts a label y ∈ {“Hotdog”, “Not Hotdog”}.

### 2.2 Algorithm Description
- **Model:** MobileNetV2, a convolutional neural network architecture optimized for mobile and embedded vision applications, is employed. The model is pretrained on the ImageNet dataset, which includes a diverse range of object categories, including “hotdog.”
- **Inference Logic:** Upon receiving an image, the application processes it through the MobileNetV2 model to obtain classification probabilities. If the top-1 predicted label is “hotdog” with a confidence score exceeding 90%, the image is classified as “Hotdog.” Otherwise, it is classified as “Not Hotdog.”
- **Transparency:** To provide users with insight into the model’s decision-making process, the top-3 predicted labels along with their confidence scores are displayed.

---

## 3. Implementation
### 3.1 Application Structure
- **Main Script:** `streamlit_app.py` contains the core logic, including model loading, image preprocessing, prediction, and user interface components.
- **Dependencies:** The application requires the following Python packages:
  - streamlit
  - tensorflow
  - pillow
  - numpy
- **Directory Structure:** The repository includes directories `finaltest1/` and `finaltest2/` containing sample images for testing and validation purposes.

### 3.2 User Interface
The Streamlit framework provides an intuitive interface where users can:
1. Upload an image in JPG or PNG format.
2. View the uploaded image displayed on the web page.
3. Receive classification results indicating whether the image is a “Hotdog” or “Not Hotdog,” along with the top-3 predicted labels and their confidence scores.

---

## 4. Experimental Evaluation
### 4.1 Methodology
The model’s performance was evaluated using a set of test images categorized into two groups:
- **Hotdog Images:** Images that clearly depict hotdogs.
- **Non-Hotdog Images:** Images of objects that are visually similar to hotdogs (e.g., sausages, sandwiches) and unrelated objects.

The evaluation aimed to assess the model’s accuracy in correctly identifying hotdogs while minimizing false positives.

### 4.2 Results
- **Accuracy:** The model demonstrated high accuracy in classifying clear images of hotdogs.
- **False Positives:** The 90% confidence threshold effectively reduced false positives, ensuring that only images with high confidence scores were classified as “Hotdog.”
- **Limitations:** Some images with unconventional presentations of hotdogs or poor image quality resulted in lower confidence scores, leading to “Not Hotdog” classifications despite containing hotdogs.

### 4.3 Discussion
The use of a high-confidence threshold enhances the reliability of the classification but may lead to conservative predictions, potentially overlooking true positives with lower confidence scores. Future improvements could involve fine-tuning the model on a specialized dataset of hotdog images to enhance its sensitivity and robustness.

---

## 5. Related Work
The concept of a “Hotdog/Not Hotdog” classifier gained popularity through its portrayal in Silicon Valley. Similar projects have been developed using various machine learning frameworks and deployment platforms. This project distinguishes itself by utilizing Streamlit for rapid development and deployment, and by employing a pretrained MobileNetV2 model for efficient inference.

---

## 6. Conclusion
This project successfully demonstrates the development and deployment of a web-based image classification application using modern machine learning tools. By integrating TensorFlow’s MobileNetV2 model with Streamlit, the application provides an accessible and efficient solution for binary image classification tasks. The project’s modular design allows for future enhancements, such as model fine-tuning and the incorporation of additional classes.

---

## 7. References
1. Howard, A. G., et al. (2017). “MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications.” arXiv preprint arXiv:1704.04861.
2. Deng, J., et al. (2009). “ImageNet: A Large-Scale Hierarchical Image Database.” In 2009 IEEE Conference on Computer Vision and Pattern Recognition (pp. 248-255).
3. Streamlit Documentation: https://docs.streamlit.io/
4. TensorFlow Documentation: https://www.tensorflow.org/

---

End of Report
