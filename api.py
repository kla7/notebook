from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from notebook import NoteBook

app = FastAPI()

nb = NoteBook('test')


class Note(BaseModel):
    name: str
    content: str | None = ""


@app.get("/", response_class=PlainTextResponse)
def index():
    """Returns a text string with hints to the user on how to access the API."""
    output = """How to access the API
    
    Get a list containing the note names of all the notes in the notebook:
        
        curl http://127.0.0.1:8000/list

    Get a list of note names whose content matches a given search term:
        
        curl http://127.0.0.1:8000/find?term=<search term>

    Get the content of a note given a note name:

        curl http://127.0.0.1:8000/note/<note name>

    Add a new note to the notebook given a note name and note content via dictionary:

        curl -X 'POST' \\
            'http://127.0.0.1:8000/add' \\
            -H 'accept: application/json' \\
            -H 'Content-Type: application/json' \\
            -d '{
            "name": "<note name>",
            "content": "<note content>"
        }'
    
    Add a new note to the notebook given a note name and note content via json file:
    
        curl -X 'POST' \\
            'http://127.0.0.1:8000/add' \\
            -H 'accept: application/json' \\
            -H 'Content-Type: application/json' \\
            -d @<file with .json extension>

    Delete a note from the notebook given a note name:
    
        curl -X 'POST' \\
            'http://127.0.0.1:8000/delete?note_name=<note name>' \\
            -H 'accept: application/json' \\
            -d ''
        
    Rename a note given a note name and the new note name:
    
        curl -X 'POST' \\
            'http://127.0.0.1:8000/rename?note_name=<note name>&new_note_name=<new note name>' \\
            -H 'accept: application/json' \\
            -d ''
    
    Edit the content of an existing note given a note name and the new note content:
    
        curl -X 'POST' \\
            'http://127.0.0.1:8000/edit?note_name=<note name>&new_content=<new note content>' \\
            -H 'accept: application/json' \\
            -d ''
    
    Clear the entire notebook:
    
        curl -X 'POST' \\
            'http://127.0.0.1:8000/clear' \\
            -H 'accept: application/json' \\
            -d ''
    """
    return output


@app.get("/list")
def list_notes() -> list:
    """Returns a list containing the note names of all the notes in the notebook."""
    return nb.notes()


@app.get("/find")
def find_term(term: str) -> dict[str, str | list]:
    """Returns a dictionary of note names whose content matches a given search term."""
    return {"term": term, "matching notes": nb.find(term)}


@app.get("/note/{note_name}")
def get_note(note_name: str) -> str:
    """
    Returns the content of a note given a note name.

    Returns an empty string if the note is not found.
    """
    return nb[note_name]


@app.post("/add")
def add_note(note: Note) -> bool:
    """
    Adds a new note to the notebook given a note name and note content.

    Returns True if the note was successfully added.
    """
    return nb.add(note.name, note.content)


@app.post("/delete")
def delete_note(note_name: str) -> bool:
    """
    Deletes a note from the notebook given a note name.

    Returns True if the note was successfully deleted.
    """
    return nb.delete(note_name)


@app.post("/rename")
def rename_note(note_name: str, new_note_name: str) -> bool:
    """
    Renames a note given a note name and the new note name.

    Returns True if the note was successfully renamed.
    """
    return nb.rename(note_name, new_note_name)


@app.post("/edit")
def edit_note(note_name: str, new_content: str) -> bool:
    """
    Edits the content of an existing note given a note name and the new note content.

    Returns True if the note was successfully edited.
    """
    return nb.edit(note_name, new_content)


@app.post("/clear")
def clear_notebook() -> bool:
    """
    Clears the entire notebook.

    Returns True if the notebook was successfully cleared.
    """
    return nb.clear()
