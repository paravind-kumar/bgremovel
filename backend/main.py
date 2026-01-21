from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (frontend se request allow karne ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    image_bytes = await file.read()
    output = remove(image_bytes)
    return Response(content=output, media_type="image/png")
