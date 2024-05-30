# Imports
from flask import Flask, render_template, request
import openai
import os

# Setup Flask
app = Flask(__name__)

# API Key (environmental variable)
api_key = ""
openai.api_key =  "sk-proj-UxBz2AlNkFkqd3hXxgJnT3BlbkFJUYH8uQT4aBd8Do9KBFSE" # os.environ.get("API_KEY")

# Displaying the interface
@app.route("/")
def home():
    return render_template("interface.html")

# Getting the response from the model
@app.route("/get_response", methods=["POST"])
def get_response():
    conversation_history = request.json["conversation_history"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=conversation_history
    )
    bot_response = response.choices[0].message.content
    return {"bot_response": bot_response}

# Starting the flask web app
if __name__ == "__main__":
    app.run(debug=True)