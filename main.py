from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from pokemons import pokemons

app = FastAPI()

class Pokemon(BaseModel):
    id: int
    name: str
    attack: int
    live: int
    type: List[str]

    def leave_pokeball(self) -> str:
        return f"{self.name} salio de la pokebola"

all_pokemons = [Pokemon(**pokemon) for pokemon in pokemons]

@app.get ("/showallpokemons/")
def show_all_pokemons():
    return all_pokemons