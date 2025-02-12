import json
import os
import re


class NoteBook:
    def __init__(self, notebook_name: str):
        """
        Loads notebook data from a given file.

        :param notebook_name: The name of the notebook to be retrieved.
        """
        self.filename = f"{notebook_name}.json"

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def __getitem__(self, note_name: str) -> str:
        """
        Retrieves the content of a note given a note name.

        :param note_name: The name of the note whose content is to be retrieved.
        :return: The content of the note. Returns an empty string if a note with the given name does not exist.
        """
        if note_name in self.data:
            return self.data[note_name]
        else:
            return ''

    def notes(self) -> list:
        """
        Retrieve all note names in the notebook.

        :return: A list containing the note names of all the notes in the notebook.
        """
        return list(self.data.keys())

    def add(self, note_name: str, note_content: str) -> bool:
        """
        Adds a new note to the notebook.

        :param note_name: The name of the note to be added.
        :param note_content: The content of the note to be added.
        :return: True if the note was successfully added.
        """
        if note_name in self.data:
            name_duplicates = [key for key in self.data if re.match(fr"^{note_name}\b", key)]
            duplicate_count = len(name_duplicates)
            note_name = f"{note_name} ({duplicate_count})"

        self.data[note_name] = note_content

        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

        return True

    def find(self, search_str: str) -> list:
        """
        Searches the notebook for notes whose content matches the given search string.

        :param search_str: A string to search for in the notebook.
        :return: A list of note names.
        """
        note_name_list = []

        for note_name, note_content in self.data.items():
            if search_str in note_content:
                note_name_list.append(note_name)

        return note_name_list

    def delete(self, note_name: str) -> bool:
        """
        Deletes a note from the notebook.

        :param note_name: The name of the note to be deleted.
        :return: True if the note was successfully deleted.
        """
        if note_name in self.data:
            del self.data[note_name]
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
            return True
        return False

    def rename(self, note_name: str, new_note_name: str) -> bool:
        """
        Renames a note.

        :param note_name: The name of the note to be renamed.
        :param new_note_name: The new name for the note.
        :return: True if the note was successfully renamed.
        """
        if note_name in self.data:
            self.add(new_note_name, self[note_name])
            self.delete(note_name)
            return True
        return False

    def edit(self, note_name: str, new_note_content: str) -> bool:
        """
        Edits the content of an existing note.

        :param note_name: The name of the note whose content is to be edited.
        :param new_note_content: The new content for the note.
        :return: True if the note was successfully edited.
        """
        if note_name in self.data:
            self.delete(note_name)
            self.add(note_name, new_note_content)
            return True
        return False

    def clear(self) -> bool:
        """
        Clears all the notes in the notebook.

        :return: True if the notebook was successfully cleared.
        """
        self.data.clear()

        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

        return True
