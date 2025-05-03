# 🌭 Hotdog? Not Hotdog? (Streamlit Demo)

A minimal, free, and fast hotdog/not-hotdog image classifier demo using Streamlit and MobileNetV2. Ready for Streamlit Community Cloud deployment.

## How to Use
1. Upload an image (JPG/PNG) in the web app.
2. The app will show the image and predict if it's a hotdog or not.
3. If the top ImageNet label contains "hotdog", you'll see "🌭 Hotdog!" Otherwise, "Not Hotdog."

## Local Development
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

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
- (Optional) `README.md`

## Files to Ignore/Delete (for a clean repo)
- `app.py`, `model.py`, `train.py`, `quick_train.py`, `Dockerfile`, etc.
- Any model weights or data folders not needed for Streamlit demo.

---
Created for Computer Vision final, May 2025.