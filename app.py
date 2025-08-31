import streamlit as st
from openai import OpenAI
from newsapi import NewsApiClient
import smtplib
from email.mime.text import MIMEText
from langsmith import traceable
import os
import json
import replicate
import time
from dotenv import load_dotenv
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from image_editor import multiple_images, textboxes
load_dotenv()
from better_profanity import profanity



st.set_page_config(
    page_title="Ulta Beauty Adobe Experience",
    page_icon="�",
    layout="centered",
    initial_sidebar_state="auto"
)

profanity.load_censor_words()

with open('./files/wave.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



# --- Streamlit App Layout ---
st.title("💰 Ulta Beauty Adobe Content AI Agent")
st.markdown("---")

pict_side, config_side = st.columns([2, 1], gap="large")

st.write(
    "Welcome to your Ulta Beauty Adobe Automation Proof of Concept."
)

image = Image.open('./1.jpeg')

st.image(image)

uploaded_file = st.file_uploader("Choose a JSON file", type="json")


if uploaded_file is not None:
    file_content_bytes = uploaded_file.read()
    file_content_string = file_content_bytes.decode('utf-8')
    try:
        data = json.loads(file_content_string)
        
        if 'Products' in data and 'Region' in data and 'Audience' in data and 'Message' in data and (len(data['Products'])) > 1:
            st.write("JSON is valid")
            uploaded_file = st.file_uploader("Upload your images here",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True)

            if uploaded_file:
                for i in uploaded_file:
                    text_to_add = data['Message']
                    text_to_add=profanity.censor(text_to_add)
                    text_color = (255, 255, 255)
                    image = Image.open(i)
                    draw = ImageDraw.Draw(image)
                    font_path = "./ShinyCrystal-Yq3z4.ttf"  # Replace with the actual path to a .ttf file
                    font_size = 60  # Desired font size
                    font = ImageFont.truetype(font_path, size=font_size)
                    draw.text((10, 10),text_to_add,(0,0,0), font=font)
                    st.write(text_to_add)

                    st.write("16:9 aspect ratio")
                    new_width = st.slider("New Width", min_value=50, max_value=image.width, value=image.width)
                    new_height = int(new_width * (9/16)) # Example for 16:9 aspect ratio
                    resized_image = image.resize((new_width, new_height))
                    st.image(resized_image, caption=f"Resized Image ({new_width}x{new_height})")
                    st.write("1:1 aspect ratio")
                    new_height = int(new_width * (1)) 
                    resized_image = image.resize((new_width, new_height))
                    st.image(resized_image, caption=f"Resized Image ({1}x{1})")
                    st.write("1:1 aspect ratio")
                    new_height = int(new_width * (16/9)) 
                    resized_image = image.resize((new_width, new_height))
                    st.image(resized_image, caption=f"Resized Image ({9}x{16})")
                    
                  
               

            prompt = st.text_input("Enter a prompt for the image:")
        
            if st.button("Generate Images"):
                with st.spinner("Generating Images...", show_time=True):
                    time.sleep(5)

                
                start_time = time.time()
                output = replicate.run(
                        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                    input={
                        "width": 1024,
                        "height": 1024,
                        "prompt": prompt,
                        "refine": "expert_ensemble_refiner",
                        "num_outputs": 3,
                        "apply_watermark": False,
                        "negative_prompt": "low quality, worst quality",
                        "num_inference_steps": 25
                    }
                )

                # The output is typically a list with one or more image URLs
                if output and len(output) > 0:
                    # Get the first image URL
                    image_url = output[0]
                    
                    # Download the image
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        # Convert the image data to a format Streamlit can display
                        image = Image.open(BytesIO(response.content))

                        text_to_add = data['Message']
                        text_to_add=profanity.censor(text_to_add)
                        text_color = (255, 255, 255)
                        draw = ImageDraw.Draw(image)
                        font_path = "./ShinyCrystal-Yq3z4.ttf"  # Replace with the actual path to a .ttf file
                        font_size = 60  # Desired font size
                        font = ImageFont.truetype(font_path, size=font_size)
                        draw.text((10, 10),text_to_add,(0,0,0), font=font)
                        st.write(text_to_add)

                        st.write("16:9 aspect ratio")
                        new_width = st.slider("New Width", min_value=50, max_value=image.width, value=image.width)
                        new_height = int(new_width * (9/16)) # Example for 16:9 aspect ratio
                        resized_image = image.resize((new_width, new_height))
                        st.image(resized_image, caption=f"Resized Image ({new_width}x{new_height})")
                        st.write("1:1 aspect ratio")
                        new_height = int(new_width * (1)) 
                        resized_image = image.resize((new_width, new_height))
                        st.image(resized_image, caption=f"Resized Image ({1}x{1})")
                        st.write("1:1 aspect ratio")
                        new_height = int(new_width * (16/9)) 
                        resized_image = image.resize((new_width, new_height))
                        st.image(resized_image, caption=f"Resized Image ({9}x{16})")
                       
                        
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        st.write(f"Image generated in {elapsed_time:.2f} seconds")
                    else:
                        st.error("Failed to download the generated image")
                else:
                    st.error("No image was generated")

        

                st.success("Done!")
                

    except:
        st.warning("")
                