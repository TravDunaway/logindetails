from logindetailsapp import app, db, locations
from flask import render_template, redirect,request,url_for,flash, abort, session
from flask_login import login_user, login_required, logout_user
from logindetailsapp.models import User
from logindetailsapp.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
import jinja2
from logindetailsapp.locations import Location

app.jinja_env.undefined = jinja2.StrictUndefined

@app.errorhandler(404)
def error_404(e):
   return render_template("404.html")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            session["username"] = user['username']
            flash("logged in successfully")

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)


@app.route('/house')
@login_required
def housepage():
    return render_template('house.html')

@app.route("/locations")
def all_locations():
   location_list = locations.get_all()
   return render_template("all_locations.html", location_list=location_list)

@app.route("/location/<location_id>")
def location_details(location_id):
   location = locations.get_id(location_id)
   return render_template("location_details.html", location=location)

@app.route("/add_to_cart/<location_id>")
@login_required
def add_to_cart(location_id):

   if 'cart' not in session:
      session['cart'] = {}
   cart = session['cart']

   cart[location_id] = cart.get(location_id, 0) + 1
   session.modified = True
   flash(f"Your chosen {location_id} successfully posted.")
   print(cart)

   return redirect("/cart")

@app.route("/cart")
@login_required
def shopping_cart():


   order_total = 0
   cart_ = []

   cart = session.get("cart", {})

   for melon_id, quantity in cart.items():
      melon = melons.get_by_id(melon_id)

      total_cost = quantity * melon.price
      order_total += total_cost

      melon.quantity = quantity
      melon.total_cost = total_cost

      cart_.append(melon)

   return render_template("cart.html", cart_=cart_, order_total=order_total)

@app.route('/welcome')
@login_required
def welcome_user():
   
        return render_template('welcome_user.html')

















@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('home'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering!!")
        return redirect(url_for('login'))

    return render_template('register.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)

























