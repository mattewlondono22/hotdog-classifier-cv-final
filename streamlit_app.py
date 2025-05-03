import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

model = load_model()

st.title("🌭 Hotdog? Not Hotdog?")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Input image", use_column_width=True)

    x = np.array(img.resize((224, 224)))
    x = preprocess_input(x[np.newaxis, ...])
    preds = model.predict(x)

    label, _, prob = decode_predictions(preds, top=1)[0][0]
    st.write(f"**Prediction:** {label} — {prob*100:.2f}%")

    # Optional: Hotdog/Not Hotdog logic
    if "hotdog" in label.lower():
        st.success("🌭 Hotdog!")
    else:
        st.info("Not Hotdog.")
