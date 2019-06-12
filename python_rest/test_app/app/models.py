from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    res = db.Column(db.Integer)
    solids = db.Column(db.Boolean)
    NTU = db.Column(db.Boolean)
    org_mal = db.Column(db.Boolean)
    MPN_100ml = db.Column(db.Boolean)
    MPN_100ml_1 = db.Column(db.Boolean)
    LosR = db.Column(db.Integer)
    Silica = db.Column(db.Integer)
    Ca = db.Column(db.Integer)
    Mg = db.Column(db.Integer)
    Ca_Mg = db.Column(db.Integer)
    NO3 = db.Column(db.Integer)
    NO3_USGS = db.Column(db.Integer)
    Cl2 = db.Column(db.Integer)
    Na = db.Column(db.Integer)
    SO4 = db.Column(db.Integer)
    K = db.Column(db.Integer)
    pH = db.Column(db.Integer)
    Alk = db.Column(db.Integer)
    Hard = db.Column(db.Integer)
    Nhard = db.Column(db.Integer)
    C_USGSTemp = db.Column(db.Integer)
    F_USGS = db.Column(db.Integer)
    Temp = db.Column(db.Integer)
    MD_Precip_inch_mon = db.Column(db.Integer)
    MD_Temp_F = db.Column(db.Integer)

    def __repr__(self):
        return '<Data {}>'.format(self.month, self.year, self.id)