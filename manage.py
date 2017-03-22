import os
from app import create_app, db
# flasky used the db as well as create_app, but i think
# it was for Migrate, something I am not using.
from app.models import Notes, Prides
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
	return dict(app=app, db=db,
		Notes=Notes, Prides=Prides)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
	
##next up:
# add migrate for db
# create loging system
