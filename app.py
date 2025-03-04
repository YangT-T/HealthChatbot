# main.py
from flask import Flask, render_template, request, jsonify
import requests
import Services.ChainService
import os
from dotenv import load_dotenv

from Controllers.EnquiryController import handleEnquiry

os.environ["TOKENIZERS_PARALLELISM"] = "false"

app = Flask(__name__)

load_dotenv()

chat_history=[]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message", methods=["POST"])
def message():
    user_input = request.form["input"]
    
    response,_ = handleEnquiry(user_input,chat_history)
    
    return jsonify({"response": response})
    


if __name__ == "__main__":
    app.run(debug=True)
