from flask_sqlalchemy import SQLAlchemy
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author = db.Column(db.String(64))
    year = db.Column(db.Integer)
    genre = db.Column(db.String(64))
    description = db.Column(db.Text)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    birth_date = db.Column(db.String(10)) 
    nationality = db.Column(db.String(64))

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    borrower_name = db.Column(db.String(64))  
    loan_date = db.Column(db.Date) 
    due_date = db.Column(db.Date)  
    returned = db.Column(db.Boolean, default=False)

class Return(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'))
    return_date = db.Column(db.Date)  
    fine = db.Column(db.Float)
