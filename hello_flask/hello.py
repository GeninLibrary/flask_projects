from flask import Flask, render_template            
app = Flask(__name__)                               # "__name__" is a global variable that tells Flask whether or not we are 
                                                    # running the file directly, or importing it as a module

                                                    # "app" is a variable that stores an "instance" of the Flask module. 

@app.route('/')                                     # The "@" symbol designates a "decorator" which attaches the following 
                                                    # function to the '/' route. This means that whenever we send a request to 
                                                    # localhost:5000/ we will run the following "hello_world" function.

                                                    # The local server in this case is localhost:5000. The DECORATOR is the "/".
                                                    # So localhost:5000 + "/"(decorator) == "ROUTE" to function


def hello_world():                                  # This function is tied to the "/" decorator
    return render_template('success.html')



# @app.route('/success')


# def success():
#     print "hello"
#     return render_template('success.html')          #


app.run(debug=True)                                 # Run the application in debug mode




                                                                