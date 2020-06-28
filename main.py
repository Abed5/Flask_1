#Importing Flask module and creating a Flask web server from Flask module
from flask import Flask
#This current file will represent my web application
app = Flask(__name__)
#Default page
@app.route("/")
#when user goes to my website, activate function below
def home():
    return "Hello, World!"


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
#when script is run, python assigns name "__main__" to script when executed
if __name__ == "__main__":
    app.run(debug=True)
