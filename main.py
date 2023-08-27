from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#sample_url = "https://rickandmortyapi.com/api/character"
#sample_date = datetime.now()

@app.get("/show_info")
async def show_info(request: Request):
    current_time = datetime.now()
    current_url = request.url
    return templates.TemplateResponse("index.html", {"request": request, "current_time": current_time, "current_url": current_url})

#@app.get("/index/", response_class=HTMLResponse)
#def index(request: Request):
    #return templates.TemplateResponse("index.html", {"request": request, "url": sample_url, "current_date": sample_date})
