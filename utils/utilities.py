from streamlit_extras.app_logo import add_logo
from PIL import Image
import streamlit as st

def set_logos():
    add_logo("ressources/logo.png", height=50)

def get_pokemon_type_image_url(pokemon_type):
    if pokemon_type=='bug':
        return "https://archives.bulbagarden.net/media/upload/2/26/Bug_icon_LA.png"
    if pokemon_type=='dark':
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Pok%C3%A9mon_Dark_Type_Icon.svg/768px-Pok%C3%A9mon_Dark_Type_Icon.svg.png"
    if pokemon_type=='dragon':
        return "https://archives.bulbagarden.net/media/upload/2/28/Dragon_icon_LA.png"
    if pokemon_type=="electric":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Pok%C3%A9mon_Electric_Type_Icon.svg/768px-Pok%C3%A9mon_Electric_Type_Icon.svg.png"
    if pokemon_type=="fairy":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Pok%C3%A9mon_Fairy_Type_Icon.svg/768px-Pok%C3%A9mon_Fairy_Type_Icon.svg.png"
    if pokemon_type=="fighting":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Pok%C3%A9mon_Fighting_Type_Icon.svg/768px-Pok%C3%A9mon_Fighting_Type_Icon.svg.png"
    if pokemon_type=="fire":
        return "https://archives.bulbagarden.net/media/upload/4/48/Fire_icon_LA.png"
    if pokemon_type=="flying":
        return "https://archives.bulbagarden.net/media/upload/d/de/Flying_icon_LA.png"
    if pokemon_type=="ghost":
        return "https://archives.bulbagarden.net/media/upload/b/b5/Ghost_icon_LA.png"
    if pokemon_type=="grass":
        return "https://archives.bulbagarden.net/media/upload/1/1b/Grass_icon_LA.png"
    if pokemon_type=="ground":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Pok%C3%A9mon_Ground_Type_Icon.svg/768px-Pok%C3%A9mon_Ground_Type_Icon.svg.png"
    if pokemon_type=="ice":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Pok%C3%A9mon_Ice_Type_Icon.svg/768px-Pok%C3%A9mon_Ice_Type_Icon.svg.png"
    if pokemon_type=="normal":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Pok%C3%A9mon_Normal_Type_Icon.svg/768px-Pok%C3%A9mon_Normal_Type_Icon.svg.png"
    if pokemon_type=="poison":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Pok%C3%A9mon_Poison_Type_Icon.svg/768px-Pok%C3%A9mon_Poison_Type_Icon.svg.png"
    if pokemon_type=="psychic":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Pok%C3%A9mon_Psychic_Type_Icon.svg/768px-Pok%C3%A9mon_Psychic_Type_Icon.svg.png"
    if pokemon_type=="rock":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Pok%C3%A9mon_Rock_Type_Icon.svg/768px-Pok%C3%A9mon_Rock_Type_Icon.svg.png"
    if pokemon_type=="steel":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Pok%C3%A9mon_Steel_Type_Icon.svg/768px-Pok%C3%A9mon_Steel_Type_Icon.svg.png"
    if pokemon_type=="water":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Pok%C3%A9mon_Water_Type_Icon.svg/768px-Pok%C3%A9mon_Water_Type_Icon.svg.png"
    if pokemon_type=="stellar":
        return "https://images.wikidexcdn.net/mwuploads/wikidex/6/6a/latest/20231216092512/Teratipo_astral_icono_EP.png"
    return pokemon_type