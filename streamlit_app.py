import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

# Cache model loading for performance
@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

st.set_page_config(page_title="Hotdog? Not Hotdog?", page_icon="🌭", layout="centered")
st.title("🌭 Hotdog? Not Hotdog?")
st.write("Upload an image and see if it's a hotdog! (Only 100% sure hotdogs will be called hotdogs.)")

with st.spinner("Loading model..."):
    model = load_model()

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Input image", use_column_width=True)

    # Preprocess
    x = np.array(img.resize((224, 224)))
    x = preprocess_input(x[np.newaxis, ...])
    with st.spinner("Classifying..."):
        preds = model.predict(x)

    # Show top-3 predictions
    top_preds = decode_predictions(preds, top=3)[0]
    for i, (label, name, prob) in enumerate(top_preds):
        st.write(f"Top {i+1}: {name} ({label}) — {prob*100:.2f}%")

    # Only call it hotdog if it's the top-1 prediction and confidence is high (now > 90%)
    top_label, top_name, top_prob = top_preds[0]
    if "hotdog" in top_name.lower() and top_prob > 0.9:
        st.success("🌭 Hotdog!")
    else:
        st.error("Not Hotdog.")
