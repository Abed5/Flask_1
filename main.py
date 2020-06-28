#Importing Flask and render_template modules and creating a Flask web server from Flask module
from flask import Flask, render_template
#This current file will represent my web application
app = Flask(__name__)
#Default page
@app.route("/")
#when user goes to my website, activate function below
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")
#when script is run, python assigns name "__main__" to script when executed
if __name__ == "__main__":
    app.run(debug=True)
