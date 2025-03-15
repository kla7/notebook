from notebook import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func


class Note(db.Model):
    name = db.Column(db.String(), primary_key=True)
    content = db.Column(db.String(), nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_edited = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return (f"Note(Name: '{self.name}', Content: '{self.content}', Time created: '{self.time_created}', "
                f"Time updated: '{self.time_edited}')")

    @classmethod
    def add(cls, note_name, note_content):
        """
        Adds a new note to the database.

        :param note_name: The name of the note to be added.
        :param note_content: The content of the note to be added.
        :return: True if the note was successfully added.
        """
        try:
            note = Note(name=note_name, content=note_content)
            db.session.add(note)
            db.session.commit()
            return True
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def delete(cls, note_name: str):
        """
        Deletes a note from the notebook.

        :param note_name: The name of the note to be deleted.
        :return: True if the note was successfully deleted.
        """
        try:
            note = Note.query.filter_by(name=note_name).first()
            db.session.delete(note)
            db.session.commit()
            return True
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def rename(cls, note_name: str, new_note_name: str):
        """
        Renames a note.

        :param note_name: The name of the note to be renamed.
        :param new_note_name: The new name for the note.
        :return: True if the note was successfully renamed.
        """
        try:
            note = Note.query.filter_by(name=note_name).first()
            new_note = Note.query.filter_by(name=new_note_name).first()
            if note and not new_note:
                note.name = new_note_name
                db.session.flush()
                db.session.commit()
                return True
            else:
                return False
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def edit(cls, note_name: str, new_note_content: str):
        """
        Edits the content of an existing note.

        :param note_name: The name of the note whose content is to be edited.
        :param new_note_content: The new content for the note.
        :return: True if the note was successfully edited.
        """
        try:
            note = Note.query.filter_by(name=note_name).first()
            if note:
                note.content = new_note_content
                db.session.flush()
                db.session.commit()
                return True
            else:
                return False
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def clear(cls):
        """
        Clears all the notes in the notebook.

        :return: True if the notebook was successfully cleared.
        """
        try:
            Note.query.delete()
            db.session.commit()
            return True
        except IntegrityError as e:
            db.session.rollback()
            return e
