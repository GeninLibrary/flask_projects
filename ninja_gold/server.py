from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = 'hello darkness my old friend'

@app.route('/')
def intialize():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html', gold = session['gold'])


@app.route('/process_money', methods = ['POST'])
def process():
    if request.form['building'] == 'cave':
        session['gold'] += 5
        session['Activities'] = 
    if request.form['building'] == 'house':
        session['gold'] += 100
    if request.form['building'] == 'farm':
        session['gold'] += 1000
    if request.form['building'] == 'casino':
        session['gold'] += 2000
    return redirect ('/')

app.run(debug=True)