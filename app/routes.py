from flask import Blueprint, render_template, request, redirect, url_for
from .models import Book, Author, Loan, Return
from . import create_app, db  

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
def index():
    books = Book.query.all()
    authors = Author.query.all()
    loans = Loan.query.all()
    returns = Return.query.all()
    return render_template('index.html', books=books, authors=authors, loans=loans, returns=returns)

@routes_blueprint.route('/list_books')
def list_books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@routes_blueprint.route('/list_authors')
def list_authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)

@routes_blueprint.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        description = request.form['description']

        book = Book(title=title, author=author, year=year, genre=genre, description=description)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('routes.list_books'))
    return render_template('add_book.html')

@routes_blueprint.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birth_date']
        nationality = request.form['nationality']

        author = Author(name=name, birth_date=birth_date, nationality=nationality)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('routes.list_authors'))
    return render_template('add_author.html')

@routes_blueprint.route('/loans')
def list_loans():
    loans = Loan.query.all()
    return render_template('loans.html', loans=loans)

@routes_blueprint.route('/returns')
def list_returns():
    returns = Return.query.all()
    return render_template('returns.html', returns=returns)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
