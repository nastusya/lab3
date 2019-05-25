from flask import Flask
from flask_compress import Compress
from models import db



PUBLIC_KEY = 'i18183574422'
PRIVATE_KEY = 'DWHmS0mwLkNTIUJJhP6bTmAN4WpKshVJomDSdeZ3'


app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db.init_app(app)

compress = Compress(app)

import views
