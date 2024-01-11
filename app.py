from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import openai
import chatbot

openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sendMessage', methods=['POST'])
def send_message():
    user_input = request.json['user_input']
    response = chatbot.generate_gpt3_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
