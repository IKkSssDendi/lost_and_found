from app import create_app
from app import db

app = create_app()
app.app_context().push()
db.create_all(app=app)


if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    app.run()