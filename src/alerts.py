# Alert System
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "ElderlyAid Alert System"

if __name__ == '__main__':
    app.run(debug=True)
