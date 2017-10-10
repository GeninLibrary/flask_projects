from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def greeting():
    return render_template('index.html')


@app.route('/ninjas')

def ninjas():
    return render_template('ninjas.html')


@app.route('/dojo/new')

def dojo():
    return render_template('dojos.html')

app.run(debug=True)
