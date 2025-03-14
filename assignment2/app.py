from flask import Flask, request, render_template, make_response, redirect, url_for
from flask_restful import Resource, Api
from notebook import NoteBook

app = Flask(__name__)
api = Api(app)

nb = NoteBook('data')


class Index(Resource):
    """
    Renders the main page of the app. Functions available: find notes by a search term,
    see a list of note names for all the notes in the notebook, add a new note, and clear the notebook."""
    def get(self):
        notes_list = nb.notes()
        add_note = request.args.get('add_note', type=bool)
        note_name = request.args.get('note_name', type=str)
        note_content = request.args.get('note_content', type=str)

        if add_note:
            nb.add(note_name, note_content)
            return redirect(url_for('index'))

        clear_notebook = request.args.get('clear', type=bool)

        if clear_notebook:
            nb.clear()
            return redirect(url_for('index'))

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', notes_list=notes_list,
                                             clear=clear_notebook), headers)


class Find(Resource):
    """Renders the search page of the app. See a list of note names whose content matches the given search term."""
    def get(self):
        search_term = request.args.get('search_term', type=str)
        found_notes = nb.find(search_term)

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('find.html', search_term=search_term,
                                             found_notes=found_notes), headers)


class Note(Resource):
    """
    Renders the note page of the app. See the note name and note content for a selected note.
    Users can edit or delete the note.
    """
    def get(self, note_name):
        note_content = nb[note_name]

        edit = request.args.get('edit', type=bool)
        save_edit = request.args.get('save_edit', type=bool)
        new_note_content = request.args.get('new_note_content', type=str)
        new_note_name = request.args.get('new_note_name', type=str)

        if save_edit:
            if new_note_name != note_name and new_note_content != note_content:
                nb.edit(note_name, new_note_content)
                nb.rename(note_name, new_note_name)
                return redirect(url_for('note', note_name=new_note_name))
            elif new_note_content != note_content:
                nb.edit(note_name, new_note_content)
                return redirect(url_for('note', note_name=note_name))
            else:
                nb.rename(note_name, new_note_name)
                return redirect(url_for('note', note_name=new_note_name))

        delete = request.args.get('delete', type=bool)

        if delete:
            nb.delete(note_name)
            return redirect(url_for('index'))

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('note.html', note_name=note_name,
                                             note_content=note_content, delete=delete, edit=edit), headers)


api.add_resource(Index, '/')
api.add_resource(Find, '/find')
api.add_resource(Note, '/note/<string:note_name>')


if __name__ == '__main__':
    app.run(debug=True)
