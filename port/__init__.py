from dotenv import load_dotenv
load_dotenv()


from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

csrf=CSRFProtect()
mail = Mail()

def create_app():
    from port import config
    from port.models import db
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py',silent=True)
    app.config.from_object(config.DevelopmentConfig)
    csrf.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    Migrate(app,db)
    return app

app=create_app()

from port import route
from port import models,form
