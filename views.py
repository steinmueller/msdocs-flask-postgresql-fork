from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def landingpage():
    return render_template("landingpage.html", user=current_user)

# TODO add functionalities for the web app
@views.route('/home')
@login_required
#@oidc.require_login
def home():
    return render_template("home.html", user=current_user)

@views.route('/app')
@login_required
def app():
    return render_template("app.html", user=current_user)
