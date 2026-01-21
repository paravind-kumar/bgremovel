from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "Backend is running"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    from rembg import remove  # 👈 yahan import
    image_bytes = await file.read()
    output = remove(image_bytes)
    return Response(content=output, media_type="image/png")
