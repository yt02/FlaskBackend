
from flask import Flask, request, jsonify
from flask_cors import CORS
from detect import detect_objects
import os
import uuid

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "Flask backend is working!"

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    results = detect_objects(filepath)
    return jsonify({'results': results})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

