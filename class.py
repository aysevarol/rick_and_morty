from pydantic import BaseModel


class Character(BaseModel):
    name: str
    status: str
    species: str
    origin: str
    episodes: list