from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/chat', methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate a response using Gemini
        response = model.generate_content(
            f"without bolding the text, Talk to me in Gen Z slang and gossip about celebrities: {user_message} and also ask me a question based on my input and also make the conversation short"
        )
        bot_reply = response.text
        return jsonify({"user_message": user_message, "bot_reply": bot_reply})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Oops! Something went wrong. Try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
