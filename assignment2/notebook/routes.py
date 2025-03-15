from flask import request, render_template, make_response, redirect, url_for
from flask_restful import Resource, Api
from notebook import app
from notebook.model import Note


api = Api(app)


class Index(Resource):
    def get(self):
        notes_list = Note.query.all()
        add_note = request.args.get('add_note', type=bool)
        note_name = request.args.get('note_name', type=str)
        note_content = request.args.get('note_content', type=str)

        if add_note:
            Note.add(note_name, note_content)
            return redirect(url_for('index'))

        clear_notebook = request.args.get('clear', type=bool)

        if clear_notebook:
            Note.clear()
            return redirect(url_for('index'))

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', notes=notes_list,
                                             clear=clear_notebook), headers)


class Find(Resource):
    def get(self):
        search_term = request.args.get('search_term', type=str)
        name_matches = Note.query.filter(Note.name.contains(search_term)).all()
        content_matches = Note.query.filter(Note.content.contains(search_term)).all()

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('find.html', search_term=search_term,
                                             name_match_notes=name_matches, content_match_notes=content_matches), headers)


class Notes(Resource):
    def get(self, note_name):
        note = Note.query.get(note_name)

        edit = request.args.get('edit', type=bool)
        save_edit = request.args.get('save_edit', type=bool)
        new_note_content = request.args.get('new_note_content', type=str)
        new_note_name = request.args.get('new_note_name', type=str)

        if save_edit:
            if new_note_name != note.name and new_note_content != note.content:
                Note.edit(note_name, new_note_content)
                renamed = Note.rename(note_name, new_note_name)
                if renamed:
                    return redirect(url_for('notes', note_name=new_note_name))
                else:
                    return redirect(url_for('notes', note_name=new_note_name))
            elif new_note_content != note.content:
                Note.edit(note_name, new_note_content)
                return redirect(url_for('notes', note_name=note_name))
            else:
                renamed = Note.rename(note_name, new_note_name)
                if renamed:
                    return redirect(url_for('notes', note_name=new_note_name))
                else:
                    return redirect(url_for('notes', note_name=note_name))

        delete = request.args.get('delete', type=bool)

        if delete:
            Note.delete(note_name)
            return redirect(url_for('index'))

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('note.html', note=note, delete=delete, edit=edit),
                             headers)


api.add_resource(Index, '/')
api.add_resource(Find, '/find')
api.add_resource(Notes, '/<string:note_name>')
