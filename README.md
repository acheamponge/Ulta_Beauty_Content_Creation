# Ulta Beauty Adobe Content AI Agent  

A **Streamlit-based AI application** for automating content generation and creative workflows at Ulta Beauty. This proof of concept integrates **AI-powered image generation (via Replicate’s Stable Diffusion XL), text personalization, profanity filtering, and dynamic resizing for multiple aspect ratios.**  

---

## 🚀 Features  

- **Upload JSON campaign briefs** with `Products`, `Region`, `Audience`, and `Message`.  
- **Upload creative assets** (PNG/JPG/JPEG).  
- **Automatic message overlay** with profanity filtering.  
- **Dynamic aspect ratio resizing** (16:9, 1:1, 9:16).  
- **AI image generation** from text prompts using [Stable Diffusion XL](https://replicate.com/stability-ai/sdxl).  
- **Custom styling** with Streamlit and CSS.  

---

## 📂 Project Structure  

```
├── app.py                     # Main Streamlit application
├── image_editor.py            # Helper functions for image/text overlays
├── files/
│   └── wave.css               # Custom CSS for UI styling
├── 1.jpeg                     # Sample display image
├── ShinyCrystal-Yq3z4.ttf     # Custom font for overlays
├── .env                       # Environment variables (API keys, etc.)
```

---

## ⚙️ Requirements  

- Python 3.9+  
- Dependencies (see `requirements.txt`):  
  - `streamlit`  
  - `openai`  
  - `newsapi-python`  
  - `replicate`  
  - `requests`  
  - `pillow`  
  - `python-dotenv`  
  - `better-profanity`  

Install dependencies:  

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables  

Create a `.env` file in the project root with the following:  

```env
OPENAI_API_KEY=your_openai_key_here
REPLICATE_API_TOKEN=your_replicate_api_token_here
NEWSAPI_KEY=your_newsapi_key_here   # optional if using news API
```

---

## ▶️ Usage  

1. Run the app:  

```bash
streamlit run app.py
```

2. In the browser:  
   - Upload a valid **JSON file** (with keys: `Products`, `Region`, `Audience`, `Message`).  
   - Upload one or more **image files**.  
   - The system will:  
     - Overlay campaign message text (profanity-censored).  
     - Provide multiple aspect ratio outputs.  
   - Optionally, enter a **prompt** to generate new creatives via Stable Diffusion XL.  

---

## 📌 Example JSON Input  

```json
{
  "Products": ["Lipstick", "Foundation"],
  "Region": "US",
  "Audience": "Gen Z",
  "Message": "Get flawless skin with our new collection!"
}
```

---

## 🖼️ Example Workflow  

1. Upload JSON campaign brief ✅  
2. Upload product images ✅  
3. App applies text overlay with custom font ✅  
4. View images resized to **16:9, 1:1, and 9:16** ✅  
5. Generate new creatives with AI ✅  

---

## ⚠️ Notes  

- The app censors inappropriate language automatically.  
- Replicate API calls may take a few seconds per generation.  
- Font path (`ShinyCrystal-Yq3z4.ttf`) must exist in the project root.  

---

## 📜 License  

MIT License.  
