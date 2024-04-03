from market import app
from flask import render_template , request
from market.models import Item , Message
from market import db

@app.route("/")  # decorators # what url in your website I am going to run with
@app.route("/home")
def main_page():
    return render_template("index.html") # knows how to handle our request and direct them
    # to our

@app.route("/about/<username>")

def about_page(username):
    return f"<h1>This is the about page of {username}</h1>"


@app.route("/market")
def market_page():
    items = Item.query.all() #basically return all the items inside the database
    return render_template("market.html" , items = items) # we are calling the items

@app.route("/base")
def base_page():
    return render_template("base.html") 

@app.route("/post")
def post_page():
    messages = Message.query.all()
    return render_template("post.html" , messages = messages)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        content = request.form['message']
        new_message = Message(content=content)
        db.session.add(new_message)
        db.session.commit()
        messages = Message.query.all()
        return render_template("post.html" , messages = messages)
    return 'Hata: İstek metodu geçersiz.'