from flask import Flask, render_template, request
from main import get_latest_meeting_key, generate_strategy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_strategy', methods=['POST'])
def get_strategy():
    circuit = request.form['circuit']

    meeting_key = get_latest_meeting_key(circuit)
    if not meeting_key:
        return render_template('index.html', result="No meetings found for that circuit.", circuit=circuit)

    strategy = generate_strategy(meeting_key)
    return render_template('index.html', result=strategy, circuit=circuit)

if __name__ == '__main__':
    app.run(debug=True)
