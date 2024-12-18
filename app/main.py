from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

app = FastAPI()

# Model configuration
MODEL_NAME = "Salesforce/blip-image-captioning-base"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model and processor once at startup
processor = AutoProcessor.from_pretrained(MODEL_NAME)
model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
      <head><title>Chat with Llama</title></head>
      <body>
        <h1>Welcome to Chat with Llama!</h1>
        <p>Upload an image to generate a caption:</p>
        <form action="/generate-caption/" method="post" enctype="multipart/form-data">
          <input type="file" name="file" accept="image/*" required />
          <button type="submit">Generate Caption</button>
        </form>
      </body>
    </html>
    """

@app.post("/generate-caption/")
async def generate_caption(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(device)
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        return {"caption": caption}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
