import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def devserver():
    """
        runs devserver at host='0.0.0.0' (Can view is as localhost on outside vagrant)
    """
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    manager.run()
