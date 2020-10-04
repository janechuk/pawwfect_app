"""Flask app for adopt app."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify, session

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet, User
from forms import AddPetForm, EditPetForm, RegisterForm, LoginForm
from secrets import API_SECRET_KEY
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key = API_SECRET_KEY)

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


##############################################################################

@app.route("/")
def home_page():
    """Landing Page"""
    
    return render_template("home.html")


@app.route("/about")
def about_page():
    """About Page"""
    
    return render_template("about.html")

# ************************PawwNews route*********************************************
@app.route("/pawwnews")
def news_page():
    """PawwNews Page"""
    all_articles = newsapi.get_everything(q='dogs, dog',
                                       language='en',
                                      sort_by='popularity',
                                      )
    articles = all_articles['articles']

    title = []
    description = []
    urlToImage = []
    url = []
    
    for i in range(len(articles)):
        myarticles = articles[i]

        title.append(myarticles['title'])
        description.append(myarticles['description'])
        urlToImage.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(title, description, urlToImage, url)
    
    return render_template("pawwnews.html", context = mylist)

# ************************PawwRepo route*********************************************
@app.route("/pawwrepo")
def pawwrepo_pets():
    """List all pets available"""

    pets = Pet.query.all()
    return render_template("pawwrepo.html", pets=pets)


# ************************Contact route*********************************************
@app.route("/contact")
def contact_page():
    """Contact Page"""
    
    return render_template("contact.html")

# ******************************Register New user route**********************************

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a user: produce form and handle form submission."""

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register(username, password, first_name, last_name, email)

        db.session.commit()
        session['username'] = user.username
        return redirect(f"/users/{user.username}")
    else:
        return render_template("register.html", form=form)


# ************************Authenticate and Login existing user route**************************
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Produce login form or handle login."""

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)  # <User> or False
        if user:
            session['username'] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ["Invalid username/password."]
            return render_template("login.html", form=form)

    return render_template("login.html", form=form)

# ************************Dashboard route*******************************************
@app.route("/users/<username>")
def user_detail_page(username):
    """Shows user detail page"""
    if "username" not in session:
        flash("Please login first!")
        return redirect("/login")
    else:
        user = User.query.get(username)
    return render_template("dashboard.html", user=user, username=username)


# ************************Log out user route*******************************************
@app.route("/logout")
def logout():
    """Logout route."""

    session.pop("username")
    return redirect("/")


# ************************Add Pet route*********************************************
@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))

    else:
        # re-present form for editing
        return render_template("pet_add_form.html", form=form)

# ************************Edit Pet route*********************************************
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))

    else:
        # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)

# ************************Pet route*********************************************
@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)
