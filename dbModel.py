from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xxxx.xxxxxx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class UserData(db.Model):
    __tablename__ = 'UserData'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    display_name = db.Column(db.String(64))
    picture_url = db.Column(db.String(256), nullable=True)
    status_message = db.Column(db.String(256), nullable=True)
    group_id = db.Column(db.Integer, nullable=True)
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)

    def __init__(self
                 , user_id
                 , display_name
                 , picture_url
                 , status_message
                 , group_id
                 , create_date
                 , modify_date
                 ):
        self.user_id = user_id
        self.display_name = display_name
        self.picture_url = picture_url
        self.status_message = status_message
        self.group_id = group_id
        self.create_date = create_date
        self.modify_date = modify_date


def loadUserData():
    sql = 'SELECT * FROM "UserData"'
    result = db.session.execute(sql)
    for row in result:
        print(row)

if __name__ == '__main__':
    manager.run()

type(db)