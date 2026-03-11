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

def buscar_pokemon_por_nombre(name):
    for pokemon in all_pokemons:
        if pokemon.name.lower() == name.lower():
            return pokemon
    return None


@app.get("/showonepokemon/")
def show_one_pokemon(name: str = Query(...)):
    pokemon = buscar_pokemon_por_nombre(name)

    if pokemon:
        return pokemon

    return {"mensaje": "Pokemon no encontrado"}

def buscar_pokemon_por_id(id):
    for pokemon in all_pokemons:
        if pokemon.id == id:
            return pokemon
    return None

@app.get("/showonepokemonbyId/")
def show_one_pokemon_by_id(id: int = Query(...)):
    pokemon = buscar_pokemon_por_id(id)

    if pokemon:
        return pokemon

    return {"mensaje": "Pokemon no encontrado"}

@app.get("/pokemonbattle/")
def pokemon_battle(name1: str = Query(...), name2: str = Query(...)):
    pokemon1 = buscar_pokemon_por_nombre(name1)
    pokemon2 = buscar_pokemon_por_nombre(name2)

    if pokemon1 is None or pokemon2 is None:
        return {"mensaje": "Uno de los 2, o los 2 pokemones no existen"}

    vida_pokemon1 = pokemon1.live
    vida_pokemon2 = pokemon2.live

    while vida_pokemon1 > 0 and vida_pokemon2 > 0:
        vida_pokemon2 = vida_pokemon2 - pokemon1.attack

        if vida_pokemon2 <= 0:
            break

        vida_pokemon1 = vida_pokemon1 - pokemon2.attack

    if vida_pokemon1 > 0:
        ganador = pokemon1.name
    elif vida_pokemon2 > 0:
        ganador = pokemon2.name
    else:
        ganador = "Empate"

    return {
        "pokemon_1": pokemon1.name,
        "pokemon_2": pokemon2.name,
        "salida_1": pokemon1.leave_pokeball(),
        "salida_2": pokemon2.leave_pokeball(),
        "winner": ganador
    }