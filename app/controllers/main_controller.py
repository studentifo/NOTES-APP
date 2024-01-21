from flask import render_template

class MainController:
    def index(self):
        # Your logic to load and display notes goes here
        return render_template("index.html", notes=[])
