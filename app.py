from flask import Flask, request, render_template
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"), port=os.getenv("PORT"))
