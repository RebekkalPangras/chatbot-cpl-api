
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define your chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Get the input data from the request
    message = data['message']  # Extract the chat message from the data

    # Send a request to the ChatGPT API
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': 'Bearer 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',
            'Content-Type': 'application/json'
        },
        json={
            'messages': [{'role': 'system', 'content': 'You are a user.'},
                         {'role': 'user', 'content': message}]
        }
    )

    # Process the response
    if response.status_code == 200:
        output = response.json()
        generated_message = output['choices'][0]['message']['content']
        # Additional processing or formatting if needed

        # Return the response
        return jsonify({'response': generated_message})
    else:
        return jsonify({'error': 'Failed to generate response'})

if __name__ == '__main__':
    app.run()