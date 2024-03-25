from flask import Flask, render_template, request, jsonify

import openai

openai.api_key = "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"





app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    chat_messages = [{'role': 'system', 'content': 'You are a helpful campus assistant, you help students navigate through the school environment, give them available landmarks to locate thier destinations and provide them with information about the recources and utilities in each structure.'}, {'role': 'user', 'content': input}]
    return get_openai_response(chat_messages)

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
    )

    return response['choices'][0]['message']['content']


if __name__ == '__main__':
    app.run()
