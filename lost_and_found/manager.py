from app import create_app,db
from app.lost_and_found.models import LostAndFound
from flask_script import Manager,Shell

app = create_app()
manager = Manager(app)

def make_shell_context():
    return dict(app=app,db=db,LostAndFound=LostAndFound)

manager.add_command("shell",Shell(make_shell_context()))

if __name__ == "__main__":
    manager.run()