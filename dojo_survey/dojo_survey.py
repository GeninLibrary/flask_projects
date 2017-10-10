from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])

def results():
    return render_template('results.html', name = request.form['name'], location = request.form['location'])

app.run(debug=True)