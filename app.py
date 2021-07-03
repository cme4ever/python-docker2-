from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! & returning another value & adding more here 어니럳지ㅏ럳지ㅏㅓㄹ'
