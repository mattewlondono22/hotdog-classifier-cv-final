# 🌭 Hotdog? Not Hotdog? (Streamlit Demo)

A minimal, strict, and fast hotdog/not-hotdog image classifier demo using Streamlit and MobileNetV2. Ready for Streamlit Community Cloud deployment.

## Features
- Uses MobileNetV2 pretrained on ImageNet
- Only predicts "Hotdog" if the top-1 label is "hotdog" and confidence > 90%
- Shows top-3 predictions for transparency
- Clean, minimal code and requirements

## How to Use
1. Upload an image (JPG/PNG) in the web app.
2. The app will show the image and predict if it's a hotdog or not.
3. If the top ImageNet label contains "hotdog" and confidence > 90%, you'll see "🌭 Hotdog!" Otherwise, "Not Hotdog."

## Local Development
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Testing
- You can test with your own images or use the provided examples in `finaltest1/` and `finaltest2/`.
- Example: drag `finaltest2/notahotdog.png` into the app to see a negative case.

## Free Deployment
- Push this repo (with just `streamlit_app.py` and `requirements.txt`) to GitHub.
- Go to https://streamlit.io/cloud and connect your repo.
- The app will auto-deploy for free.

## Minimal Requirements
```
streamlit
tensorflow
pillow
numpy
```

## Files to Keep
- `streamlit_app.py`
- `requirements.txt`
- `README.md`
- (Optional) `finaltest1/`, `finaltest2/` for testing

---
Created for Computer Vision final, May 2025.