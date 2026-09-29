from flask import Flask, render_template, request, jsonify
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        question = data.get("question", "")

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",cd Desktop\EduGenie
            contents=question
        )

        return jsonify({"answer": response.text})

    except Exception as e:
        print("GEMINI ERROR:", e)
        return jsonify({"error": str(e)}), 500
    data = request.json
    question = data.get("question", "")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return jsonify({"answer": response.text})

if __name__ == "__main__":
    app.run(debug=True)