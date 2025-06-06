## Assignment 2 | Flask-SQLAlchemy

For this assignment, our task is to expand on the notebook app by adding a database backend using Flask-SQLAlchemy
with the following additional features:

1. Allow comments to be added on a note
2. See all comments under a note
3. Add a date to each note and comment
4. Search for notes whose comments match a search term
5. Delete a note and all of its comments

## App Features

The notebook app contains the following features:
* See a list of all notes in the notebook
* See the content of an individual note identified by name
* Add a new note with a name and content to the notebook
* Edit an existing note in the notebook
  * This includes both renaming the note and altering its content
* Allow comments to be added on a note **[NEW!]**
* See all comments under a note **[NEW!]**
* See the date and time for when:
  * A note was created and last edited **[NEW!]**
  * A comment was added **[NEW!]**
* Search for:
  * Notes whose name contains a search term **[NEW!]**
  * Notes whose content contains a search term
  * Notes whose comments contain a search term **[NEW!]**
* Delete a note from the notebook
  * This includes deleting all of a note's comments **[NEW!]**
* Clear all notes from the notebook

## Instructions

The instructions for running the app are as follows:

### Requirements

* Python 3.11 or higher
* Install dependencies from [requirements.txt](https://github.com/kla7/notebook/blob/master/assignment2/requirements.txt)

### Flask

To run the Flask script:
* In your terminal, run `python run.py`
* The default server is http://127.0.0.1:5000/

## Contents of this repository

This folder contains 3 files and 2 directories:

1. This **README** file.
2. **instance**, a folder containing the SQL database containing notebook entries.
3. **notebook**, a folder containing the Python package, .css stylesheet, .js script, and .html template files.
4. **requirements.txt**, a document with the dependencies to run the application.
5. **run.py**, a script that runs the application.