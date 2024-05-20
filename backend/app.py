from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body>
    <h1>Mendigo, mercachinfle!</h1>
    </body>
    </html>
    """
