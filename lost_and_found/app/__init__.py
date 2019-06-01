from flask import Flask
from app.database import db
import config
from flask_redis import FlaskRedis

redis_store = FlaskRedis()


def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object(config.DevConfig)

    db.init_app(app)
    redis_store.init_app(app)

    from app.lost_and_found import  lost_and_found
    app.register_blueprint(lost_and_found)

    return app