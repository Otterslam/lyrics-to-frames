from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from datetime import datetime
import os
import resend

from dotenv import load_dotenv
load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

app = FastAPI(title="Lyrics to Frames API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ContactRequest(BaseModel):
    name: str
    artist_name: str | None = None
    email: EmailStr
    project_type: str
    message: str


@app.get("/")
def root():
    return {"status": "ok", "project": "Lyrics to Frames"}


@app.get("/api/showcase")
def get_showcase():
    return [
        {
            "title": "Bloody Cigarettes",
            "type": "Roll The Dice",
            "video": "/videos/visual-1.mp4",
            "spotifyUrl": "https://open.spotify.com/track/5aIzjgc8sBEP5CMn9Vqm6g?si=e2b93144bc044485",
        },
        {
            "title": "Muunjuun",
            "type": "The Sun Grows where vegetable shines",
            "video": "/videos/visual-2.mp4",
            "spotifyUrl": "https://open.spotify.com/track/0cyWyXq26bx5OH70BSzJ4S?si=9d8caf71bd2c4bf5",
            
        },
        {
            "title": "Tears",
            "type": "Covered in tears",
            "video": "/videos/visual-3.mp4",
            "spotifyUrl": "https://open.spotify.com/track/66XcFleJN3X35mYeHlQHGF?si=7f06d542f0d14e5c",
        },
        {
            "title": "Break the Vault",
            "type": "DDTHAGR8",
            "video": "/videos/visual-4.mp4",
            "spotifyUrl": "https://open.spotify.com/track/0cyWyXq26bx5OH70BSzJ4S?si=9d8caf71bd2c4bf5",
        },
         {
            "title": "Relieves",
            "type": "cafe y cigarros",
            "video": "/videos/visual-5.mp4",
            "spotifyUrl": "https://open.spotify.com/track/6zpG9Tv5k6eUp0WneNX9at?si=eaa63598b713443f",
        },
         {
            "title": "The Shellter",
            "type": "Furia",
            "video": "/videos/visual-6.mp4",
            "spotifyUrl": "https://open.spotify.com/album/3Ei5O9wzreZSTdoodJIAVS?si=rg_oqy-bSBCrlTIfZbkMSA",
        },
         {
            "title": "Los Paulians",
            "type": "Estelar",
            "video": "/videos/visual-7.mp4",
            "spotifyUrl": "https://open.spotify.com/track/3cJNOjcWzm4EIl5zOPr7JY?si=ffb0ed67f8fd48f3https://open.spotify.com/track/3cJNOjcWzm4EIl5zOPr7JY?si=ffb0ed67f8fd48f3",
        },
         {
            "title": "Mango Street Trio",
            "type": "Lovers",
            "video": "/videos/visual-8.mp4",
            "spotifyUrl": "https://open.spotify.com/track/1etfegO8A1f6XXJ3wh9EKA?si=0145cb6442144308",
        },
         {
            "title": "SUMMERCHAMP",
            "type": "Blank page",
            "video": "/videos/visual-9.mp4",
            "spotifyUrl": "https://open.spotify.com/track/0cyWyXq26bx5OH70BSzJ4S?si=9d8caf71bd2c4bf5",
        },
    ]


@app.post("/api/contact")
def contact(data: ContactRequest):
    try:
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "jerry.amozurrutia@gmail.com",
            "subject": f"New project from {data.name}",
            "html": f"""
                <h2>New Project Request</h2>
                <p><strong>Name:</strong> {data.name}</p>
                <p><strong>Artist:</strong> {data.artist_name}</p>
                <p><strong>Email:</strong> {data.email}</p>
                <p><strong>Type:</strong> {data.project_type}</p>
                <p><strong>Message:</strong><br>{data.message}</p>
            """
        })

        return {"success": True}

    except Exception as e:
        print("EMAIL ERROR:", e)
        return {"success": False}