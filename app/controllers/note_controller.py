from flask import render_template

class NoteController:
    def add_note(self):
        # Your logic to add a note goes here
        return render_template("index.html", notes=[])
