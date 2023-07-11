from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = [
    {"title": "Book 1", "author": "Author 1", "rating": 8},
    {"title": "Book 2", "author": "Author 2", "rating": 7},
    {"title": "Book 3", "author": "Author 3", "rating": 9}
]


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)

