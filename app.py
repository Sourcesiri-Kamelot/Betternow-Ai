from flask import Flask, render_template, request, jsonify
from responses import get_positive_reply

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    reply = get_positive_reply(user_input)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)