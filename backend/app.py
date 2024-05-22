from flask import Flask

#for multi-server communication
from flask_cors import CORS 

from db.characters import *

app = Flask(__name__)
CORS(app)

@app.route("/characters")
def home():
    print(get_all_characters)
    return get_all_characters()
