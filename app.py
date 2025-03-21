# from flask import Flask,request, render_template
# import os
# import requests
# from dotenv import load_dotenv
# load_dotenv()
# grok_api_key = os.getenv('GROK_API_KEY')
# grok_api_url = "https://api.x.ai/v1/chat/completions"
# app = Flask(__name__)
# @app.route('/', methods=["POST","GET"])
# def home():
#     if request.method == "POST":
#         user_message = request.form["message"]
#         headers={
#             'Authorization': f'Bearer {grok_api_key}',
#             'Content_Type': 'application/json'
#         }
#         # data = {
#         #     'model': 'grok-2-latest',
#         #     'messages':[{'role': 'user', 'content': f"Talk to me in Gen Z slang and gossip about celebrities: {user_message}"}]
#         # }
#         data = {
#             'model': 'grok-2-latest',
#             'messages': [
#                 {'role': 'system', 'content': 'You are a test assistant which talks in genZ slang and gossip about celebrities.'},
#                 {'role': 'user', 'content': user_message}
#             ],
#             'stream': False,
#             'temperature': 0
#         }
#         response = requests.post(grok_api_url, headers=headers, json=data)
#         print(response.status_code)
#         if(response.status_code == 200):
#             grok_response = response.json()
#             bot_reply = grok_response['choices'][0]['message']['content']
#         else:
#             bot_reply = "Oops! Something went wrong. Try again later."
#         return render_template('index.html', user_message=user_message, bot_reply=bot_reply)
#     return render_template('index.html')
# if __name__ == '__main__':
#     debug = True
#     app.run(debug=debug)

# from flask import Flask, request, render_template
# import os
# from dotenv import load_dotenv
# from google import genai


# load_dotenv()

# app = Flask(__name__)


# gemini_api_key = os.getenv('GEMINI_API_KEY')


# client = genai.Client(api_key=gemini_api_key)

# @app.route('/', methods=["POST", "GET"])
# def home():
#     if request.method == "POST":
#         user_message = request.form["message"]
        
#         try:
 
#             response = client.models.generate_content(
#                 model='gemini-2.0-flash',
#                 contents = f"without bolding the text , Talk to me in Gen Z slang and gossip about celebrities: {user_message} and also ask me a question based on my input and also make the conversation short"
#             )
#             bot_reply = response.text

#         except Exception as e:
#             print(f"Error: {e}")
#             bot_reply = "Oops! Something went wrong. Try again later."
        
#         return render_template('index.html', user_message=user_message, bot_reply=bot_reply)
    
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
# from google import genai
import google.generativeai as genai


load_dotenv()

app = Flask(__name__)

gemini_api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=gemini_api_key)

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/chat', methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=f"without bolding the text, Talk to me in Gen Z slang and gossip about celebrities: {user_message} and also ask me a question based on my input and also make the conversation short"
        )
        bot_reply = response.text
        return jsonify({"user_message": user_message, "bot_reply": bot_reply})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Oops! Something went wrong. Try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
