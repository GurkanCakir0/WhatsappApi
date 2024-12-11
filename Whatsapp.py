from flask import Flask, request, jsonify
import os

app = Flask(__name__)

from flask_cors import CORS

CORS(app)

UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "Flask API is running!", 200


@app.route("/upload", methods=["POST"])
def upload_audio():
    try:
        audio_data = request.data

        if not audio_data:
            return jsonify({"error": "No audio data received"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, "audio_received.raw")
        with open(file_path, "wb") as f:
            f.write(audio_data)

        return jsonify({"message": "Audio received and saved successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
