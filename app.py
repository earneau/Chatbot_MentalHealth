from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import openai
import chatbot

openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_test.html')

@app.route('/sendMessage', methods=['POST'])
def send_message():
    user_input = request.json['user_input']
    response = chatbot.generate_gpt3_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
