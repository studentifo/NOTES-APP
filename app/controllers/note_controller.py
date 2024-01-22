from flask import render_template

class NoteController:
    def add_note(self):
        return render_template("index.html", notes=[])
