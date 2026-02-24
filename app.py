from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    if 'imageFile' not in request.files:
        return "No file", 400

    file = request.files['imageFile']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return "OK", 200

@app.route("/")
def home():
    return "Server running"
