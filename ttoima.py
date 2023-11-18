import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}
st.title("image generation application")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
prompt=st.text_input("enter ur statement")
bt=st.button("enter")
if bt:
    image_bytes = query({
        "inputs": prompt,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    images = Image.open(io.BytesIO(image_bytes))
    st.image(images)