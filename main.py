from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/characters", response_class=HTMLResponse)
async def characters(request: Request):
        response = requests.get("https://rickandmortyapi.com/api/character")
        response.raise_for_status()
        character_list = response.json()["results"]
        return templates.TemplateResponse("characters.html", {"request": request, "character_list": character_list})


@app.get("/characters/{character_id}", response_class=HTMLResponse)
async def character(request: Request, character_id: int):
    response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    character_only = response.json()
    return templates.TemplateResponse("character.html", {"request": request, "character": character_only})


@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, name: str = Form(...)):
    name=input("Enter the character name")
    response = requests.get(f"https://rickandmortyapi.com/api/character/?name={name}")
    response.raise_for_status()
    character_ = response.json()["results"]
    if character_list:
        print("Arama Sonuçları:")
        for character in character_list:
            print(f"Adı: {character['name']}, Durumu: {character['status']}")
    else:
        print("Arama sonuçları bulunamadı.")
    return templates.TemplateResponse("characters.html", {"request": request, "character_list": character_})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
