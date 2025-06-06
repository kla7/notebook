# COSI 217 Assignment 1 | FastAPI, Flask, Streamlit

For this assignment, our task is to create a simple notebook app using FastAPI, Flask, and Streamlit with the following
minimum features:
1. See a list of all notes
2. See the content of an individual note identified by name
3. Add a new note with a name and content
4. Search for notes whose content matches a search term

## App Features

The notebook app contains the following features across all platforms:
* See a list of all notes in the notebook
* See the content of an individual note identified by name
* Add a new note with a name and content to the notebook
  * If there is already a note with the same name, an increment is added to the new note's name
* Edit an existing note in the notebook
  * This includes both renaming the note and altering its content
* Search for notes whose content matches a search term
* Delete a note from the notebook
* Clear all notes from the notebook

## Instructions

The instructions for running the app are as follows:

### Requirements

* Python 3.11 or higher
* Install dependencies from [requirements.txt](https://github.com/kla7/notebook/blob/master/assignment1/requirements.txt)

### FastAPI

To run the FastAPI script:
* In your terminal, run `uvicorn api:app --reload`
* The default server is http://127.0.0.1:8000/
* To see how to run all functionalities, you can either:
  * Access the server mentioned above
  * In your terminal, run `curl http://127.0.0.1:8000`

### Flask

To run the Flask script:
* In your terminal, run `python app.py`
* The default server is http://127.0.0.1:5000/

### Streamlit

To run the Streamlit script:
* In your terminal, run `streamlit run stream.py`
* The default server is http://localhost:8501/

## Contents of this repository

This folder contains 8 files and 2 directories:

1. This **README** file.
2. **static**, a folder containing the .css stylesheet used in the Flask application.
3. **templates**, a folder containing .html files used in the Flask application.
4. **notebook.py**, a script containing a notebook module with basic functions.
5. **api.py**, a script containing the FastAPI code.
6. **app.py**, a script containing the Flask main script.
7. **stream.py**, a script containing the Streamlit application.
8. **data.json**, a file serving as the database for the notes in the notebook.
9. **item.json**, a file containing a single note used as input for the FastAPI application.
10. **requirements.txt**, a document with the dependencies to run all applications.