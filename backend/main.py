from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import os
import resend

from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

app = FastAPI(title="Lyrics to Frames API")

# ✅ CORS correcto
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://orionflower.com",
    "https://www.orionflower.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ Modelo del form
class ContactRequest(BaseModel):
    name: str
    artist_name: str | None = None
    email: EmailStr
    project_type: str
    message: str


# ✅ Root
@app.get("/")
def root():
    return {"status": "ok", "project": "Lyrics to Frames"}


# ✅ Showcase (carrusel)
@app.get("/api/showcase")
def get_showcase():
    return [
        {
            "title": "Bloody Cigarettes",
            "type": "Roll The Dice",
            "video": "/videos/Visual-1.mp4",
            "spotifyUrl": "https://open.spotify.com/track/5aIzjgc8sBEP5CMn9Vqm6g",
        },
        {
            "title": "Muunjuun",
            "type": "The Sun Grows where vegetable shines",
            "video": "/videos/Visual-2.mp4",
            "spotifyUrl": "https://open.spotify.com/track/0cyWyXq26bx5OH70BSzJ4S",
        },
        {
            "title": "Tears",
            "type": "Covered in tears",
            "video": "/videos/Visual-3.mp4",
            "spotifyUrl": "https://open.spotify.com/track/66XcFleJN3X35mYeHlQHGF",
        },
        {
            "title": "Break the Vault",
            "type": "DDTHAGR8",
            "video": "/videos/Visual-4.mp4",
            "spotifyUrl": "https://open.spotify.com/track/0cyWyXq26bx5OH70BSzJ4S",
        },
        {
            "title": "Relieves",
            "type": "cafe y cigarros",
            "video": "/videos/Visual-5.mp4",
            "spotifyUrl": "https://open.spotify.com/track/6zpG9Tv5k6eUp0WneNX9at",
        },
        {
            "title": "The Shellter",
            "type": "Furia",
            "video": "/videos/Visual-6.mp4",
            "spotifyUrl": "https://open.spotify.com/album/3Ei5O9wzreZSTdoodJIAVS",
        },
        {
            "title": "Los Paulians",
            "type": "Estelar",
            "video": "/videos/Visual-7.mp4",
            "spotifyUrl": "https://open.spotify.com/track/3cJNOjcWzm4EIl5zOPr7JY",
        },
        {
            "title": "Mango Street Trio",
            "type": "Lovers",
            "video": "/videos/Visual-8.mp4",
            "spotifyUrl": "https://open.spotify.com/track/1etfegO8A1f6XXJ3wh9EKA",
        },
        {
            "title": "SUMMERCHAMP",
            "type": "Blank page",
            "video": "/videos/Visual-9.mp4",
            "spotifyUrl": "https://open.spotify.com/track/0cyWyXq26bx5OH70BSzJ4S",
        },
    ]


# ✅ Contact form
@app.post("/api/contact")
def contact(data: ContactRequest):
    try:
        resend.Emails.send(
            {
                "from": "onboarding@resend.dev",
                "to": "jerry.amozurrutia@gmail.com",
                "subject": f"New project from {data.name}",
                "html": f"""
                    <h2>New Project Request</h2>
                    <p><strong>Name:</strong> {data.name}</p>
                    <p><strong>Artist:</strong> {data.artist_name or "N/A"}</p>
                    <p><strong>Email:</strong> {data.email}</p>
                    <p><strong>Type:</strong> {data.project_type}</p>
                    <p><strong>Message:</strong><br>{data.message}</p>
                """,
            }
        )

        return {"success": True}

    except Exception as e:
        print("EMAIL ERROR:", e)
        return {"success": False}