import json
from flask import Flask, request, jsonify
from crewai import CrewAI

app = Flask(__name__)
crew_ai = CrewAI()

@app.route('/', methods=['POST'])
def chat():
    data = request.get_json()
    contact = data['contact']
    message = data['message']
    response = crew_ai.handle_message(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
