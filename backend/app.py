from flask import Flask, request

# for multi-server communication
from flask_cors import CORS

from db.characters import *

app = Flask(__name__)
CORS(app)

# HOME
@app.route("/")
def home():
    return"""
<html>
<body>
<h1>Welcome to HEROES API</h1>
<a href="/characters">Go to HomePage</a>
</body>
</html>
    """

# DEVOLVER JSON CON CHARS
@app.route("/characters")
def all_characters():
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
    alignment = request.json.get("alignment")
    gender = request.json.get("gender")
    publisher = request.json.get("publisher")
    race = request.json.get("race")
    image = request.json.get("image")
    id = int(get_all_characters()[-1]["id"]) + 1

    character = {
        "id": id,
        "gender": gender,
        "alignment": alignment,
        "image": image,
        "name": name,
        "names": names,
        "publisher": publisher,
        "race": race,
    }
    return {"success": add_character(character), "id": id}
#EDITAR CHAR

@app.route("/characters", methods=["PUT"])
def _edit_character():
    id = request.json.get("id")
    name = request.json.get("name")
    names = request.json.get("names")
    alignment = request.json.get("alignment")
    gender = request.json.get("gender")
    publisher = request.json.get("publisher")
    race = request.json.get("race")
    image = request.json.get("image")
    character = {
        "id": id,
        "gender": gender,
        "alignment": alignment,
        "image": image,
        "name": name,
        "names": names,
        "publisher": publisher,
        "race": race,
    }
    return{"success": edit_character(character)}
    
    