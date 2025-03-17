from flask import Flask
from notebook.model import db

app = Flask(__name__)

app.config['SECRET_KEY'] = '4b6e95bfb6dd6dc860c76f21f2e31ff4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
