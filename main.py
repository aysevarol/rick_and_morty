from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {request: Request})


@app.get("/characters", response_class=HTMLResponse)
async def characters(request):
    response = requests.get("https://rickandmortyapi.com/api/character")
    character_list = response.json()["results"]
    return templates.TemplateResponse("characters.html", {"request": request, "character": character_list})


@app.get("/character/{character_id}", response_class=HTMLResponse)
async def character(request: Request, character_id: int):
    response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    character_only = response.json()
    return templates.TemplateResponse("character.html", {"request": request, "character": character_only})


@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, name: str = Form(...)):
    response = requests.get(f"https://rickandmortyapi.com/api/character/?name={name}")
    character_ = response.json()["results"]
    return templates.TemplateResponse("characters.html", {"request": request, "character": character_})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
