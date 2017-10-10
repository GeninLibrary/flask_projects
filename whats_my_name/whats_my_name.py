from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')

def formPage():
    return render_template('formPage.html')


@app.route('/process', methods=['POST'])

def createUser():
    print request.form['name']
    return redirect('/')

app.run(debug = True)

