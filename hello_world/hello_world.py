from flask import Flask 

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello World! \n This is a message from an alien entity named Nathan"


app.run(debug=True)