from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userlist.db'
db = SQLAlchemy(app)

class User():
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(100)) 
    bio = db.Column(db.Text)
    links = db.relationship('Link', backref='user', lazy=True)

class Link():
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def SignupOrLogin():
    return render_template("SignUpOrLogin.html")

@app.route('/LoginPage.html')
def Login():
    return render_template('LoginPage.html')

@app.route('/SignUp.html')
def CreateAccount():
    

if __name__ == "__main__":
    app.run(debug=True)