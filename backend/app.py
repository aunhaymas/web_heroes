from flask import Flask, request

# for multi-server communication
from flask_cors import CORS

from db.characters import *

app = Flask(__name__)
CORS(app)


# DEVOLVER JSON CON CHARS
@app.route("/characters")
def home():
    print(get_all_characters)
    return get_all_characters()


# DEVOLVER CHAR POR ID
@app.route("/characters/<id>")
def character_id(id):
    return get_character_by_id(id)


# ELIMINAR CHAR
@app.route("/characters/<id>", methods=["DELETE"])
def remove_character_by_id(id):
    return {"success": remove_character(id)}


# CREAR CHAR
@app.route("/characters", methods=["POST"])
def _create_character():
    name = request.json.get("name")
    names = request.json.get("names")
    aligment = request.json.get("aligment")
    gender = request.json.get("gender")
    publisher = request.json.get("publisher")
    race = request.json.get("race")
    image = request.json.get("image")
    id = int(get_all_characters()[-1]["id"]) + 1

    character = {
        "id": id,
        "alignment": aligment,
        "gender": gender,
        "image": image,
        "name": name,
        "names": names,
        "publisher": publisher,
        "race": race,
    }
    return {"success": add_character(character), "id": id}
