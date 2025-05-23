## Assignment 3 | Docker

For this assignment, our task is to Dockerize the notebook app.

## App Features

The notebook app contains the following features:
* See a list of all notes in the notebook
* See the content of an individual note identified by name
* Add a new note with a name and content to the notebook
* Edit an existing note in the notebook
  * This includes both renaming the note and altering its content
* Allow comments to be added on a note
* See all comments under a note
* See the date and time for when:
  * A note was created and last edited
  * A comment was added
* Search for:
  * Notes whose name contains a search term
  * Notes whose content contains a search term
  * Notes whose comments contain a search term
* Delete a note from the notebook
  * This includes deleting all of a note's comments
* Clear all notes from the notebook

## Instructions

The instructions for running the app are as follows:

### Requirements

* Python 3.11 or higher
* Install dependencies from [requirements.txt](https://github.com/kla7/notebook/blob/master/assignment3/requirements.txt)

### Docker

To run the Flask app using Docker:
* In your terminal, run `docker build -t notebook .` to create the Docker image
* In your terminal, run `docker run -v $pwd/instance:/app/instance -p 5000:5000 notebook` to create the Docker container
* Access the app at http://127.0.0.1:5000/ in your browser

## Contents of this repository

This folder contains 4 files and 2 directories:

1. This **README** file.
2. **instance**, a folder containing the SQL database containing notebook entries.
3. **notebook**, a folder containing the Python package, .css stylesheet, .js script, and .html template files.
4. **Dockerfile**, a document containing the instructions to build a Docker image.
5. **requirements.txt**, a document with the dependencies to run the application.
6. **run.py**, a script that runs the application.