import os
import json
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
from chat_logger import log_chat
from googletrans import Translator

load_dotenv()

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load chatbot configuration
with open("chatbot_config.json", "r") as f:
    config = json.load(f)

translator = Translator()

# Initialize Flask app
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")
    language = data.get("language", "en")

    # Translate user input if necessary
    if language != "en":
        user_input = translator.translate(user_input, src=language, dest="en").text

    response = generate_response(user_input)

    # Translate response back to user’s language
    if language != "en":
        response = translator.translate(response, src="en", dest=language).text

    log_chat(user_input, response, language)
    return jsonify({"response": response})

def generate_response(user_input):
    # Generate response using OpenAI API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{user_input}\n\n{config['FAQ_examples']}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
