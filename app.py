import json
from pathlib import Path
from importlib import import_module
from flask import Flask, render_template, request, redirect, url_for

class FlaskMVC:
    def __init__(self, app: Flask = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.template_folder = "templates"
        app.config.setdefault("FLASK_MVC_DIR", "app")
        self.root_path = Path(app.config["FLASK_MVC_DIR"])
        self._register_router(app)

    def _routes(self):
        with open(self.root_path / "routes.json", mode="r") as f:
            return json.load(f)

    def _register_router(self, app):
        for route in self._routes():
            controller = route["controller"]
            mod = import_module(f"{self.root_path}.controllers.{controller}_controller")
            clazz = getattr(mod, f"{controller.title()}Controller")

            app.add_url_rule(
                route["path"],
                endpoint=f"{controller}.{route['action']}",
                view_func=getattr(clazz(), route["action"]),
                methods=[route["method"]],
            )

app = Flask(__name__)
FlaskMVC(app)

# Placeholder for loading and displaying notes
def load_notes():
    # Your logic to load notes from a data source (e.g., database or file)
    return [{"id": 1, "text": "Note 1"}, {"id": 2, "text": "Note 2"}, {"id": 3, "text": "Note 3"}]

@app.route("/")
def index():
    notes = load_notes()
    return render_template("index.html", notes=notes)

@app.route("/add_note", methods=["POST"])
def add_note():
    if request.method == "POST":
        note_text = request.form["note_text"]
        # Your logic to add a note goes here
    return redirect(url_for("index"))

if __name__ == "__main__":
   app.run(debug=False,host="0.0.0.0")
