from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def Welcome():
    return "Welcome to my portfolio! My name is Nathan."
    



@app.route('/projects')

def lsProjects():
    return render_template('my_projects.html')




@app.route('/bio')
    
def lsBio():
    return render_template('/bio.html')

app.run(debug=True)


