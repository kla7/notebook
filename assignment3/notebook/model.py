from notebook import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func


class Note(db.Model):
    note_name = db.Column(db.Text, primary_key=True)
    note_content = db.Column(db.Text, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_edited = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    comments = db.relationship('Comment', backref='comment', lazy=True)

    def __repr__(self):
        return (f"Note(Name: '{self.note_name}', Content: '{self.note_content}', Time created: '{self.time_created}', "
                f"Time updated: '{self.time_edited}', Comments: {self.comments})")

    @classmethod
    def add(cls, note_name: str, note_content: str):
        """
        Adds a new note to the database.

        :param note_name: The name of the note to be added.
        :param note_content: The content of the note to be added.
        :return: True if the note was successfully added.
        """
        try:
            note = Note(note_name=note_name, note_content=note_content)
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
            note = Note.query.filter_by(note_name=note_name).first()
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
            note = Note.query.filter_by(note_name=note_name).first()
            new_note = Note.query.filter_by(note_name=new_note_name).first()
            if note and not new_note:
                note.note_name = new_note_name
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
            note = Note.query.filter_by(note_name=note_name).first()
            if note:
                note.note_content = new_note_content
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


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    note_name = db.Column(db.Text, db.ForeignKey('note.note_name'), nullable=False)
    comment_content = db.Column(db.Text, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return (f"Comment(ID: '{self.id}', Note name: '{self.note_name}', Comment content: '{self.comment_content}', "
                f"Time created: '{self.time_created}')")

    @classmethod
    def add(cls, note_name: str, comment_content: str):
        """
        Adds a new comment to the database.

        :param note_name: The name of the note for which the comment is to be added.
        :param comment_content: The content of the comment to be added.
        :return: True if the comment was successfully added.
        """
        try:
            if comment_content:
                comment = Comment(note_name=note_name, comment_content=comment_content)
                db.session.add(comment)
                db.session.commit()
                return True
            else:
                return False
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def delete(cls, note_name: str):
        """
        Deletes comments from a given note.

        :param note_name: The name of the note whose comments are to be deleted.
        :return: True if the comments were successfully deleted.
        """
        try:
            comments = Comment.query.filter_by(note_name=note_name).all()
            for comment in comments:
                db.session.delete(comment)
                db.session.commit()
            return True
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def change_note(cls, note_name: str, new_note_name: str):
        """
        When a note is renamed, alter the note name column for each of the note's comments to match the change.

        :param note_name: The name of the note to be renamed.
        :param new_note_name: The new name for the note.
        :return: True if the change was successful.
        """
        try:
            comments = Comment.query.filter_by(note_name=note_name).all()
            for comment in comments:
                comment.note_name = new_note_name
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
        Clears all the comments in the notebook.

        :return: True if the comments were successfully cleared.
        """
        try:
            Comment.query.delete()
            db.session.commit()
            return True
        except IntegrityError as e:
            db.session.rollback()
            return e
