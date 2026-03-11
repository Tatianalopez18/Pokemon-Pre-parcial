from typing import List
from fastapi import FastAPI, Query
from pydantic import BaseModel
from pokemons import pokemons

app = FastAPI(
    title="Pre-parcial Pokemon API",
    description="API hecha con FastAPI para consultar y enfrentar pokemones de primera generación",
)
class Pokemon(BaseModel):
    id: int
    name: str
    attack: int
    live: int
    type: List[str]

    def leave_pokeball(self) -> str:
        return f"{self.name} salió de la pokebola"
    

all_pokemons = [Pokemon(**pokemon) for pokemon in pokemons]

@app.get ("/showallpokemons/")
def show_all_pokemons():
    return all_pokemons

@app.get ("/showonepokemon/")
def show_one_pokemons(name:str = Query(...)):
    pokemon = nombre_pokemon(name)
    return one_pokemons 
