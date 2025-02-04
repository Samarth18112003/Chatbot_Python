from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
responses = {
    "Hi": "Hello there! How can I help you today?",
    "Hello": "Hi! What can I do for you?",
    "Bye": "Goodbye! Have a nice day!",
    "default": "I'm not sure how to respond to that. Can you please rephrase?"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    bot_response = responses.get(user_message, responses['default'])
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
