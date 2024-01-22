from flask import render_template

class MainController:
    def index(self):
        return render_template("index.html", notes=[])
