from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    
    # if app.config["ENV"] == 'production':
    #     app.config.from_object('config.ProductionConfig')
    # else:
    #     app.config.from_object('config.DevelopmentConfig')

    # if config is not None:
    #     app.config.update(config)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dgdmzisdyjdknt:5a03ad1be9306bbe32a062fb214487d539cdcb0f2148da8cc58f24fde4c98a31@ec2-34-193-113-223.compute-1.amazonaws.com:5432/d6efdbmdq6p9ca"


    db.init_app(app)
    migrate.init_app(app, db)

    from project_app.routes import (main_route, book_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(book_route.bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
