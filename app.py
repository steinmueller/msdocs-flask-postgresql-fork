from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)
app.config.from_object('settings')
SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
SQLALCHEMY_TRACK_MODIFICATIONS=False,

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

# The import must be done after db initialization due to circular import issue
from models import User, Mission

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

from .views import views
from .auth import auth

# register blueprints
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

if __name__ == '__main__':
    app.run()
