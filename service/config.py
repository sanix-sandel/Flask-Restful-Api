import os 

basedir=os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO=False
SQLALCHEMY_TRACK_MODIFICATIONS=True
SQLALCHEMY_DATABASE_URI="postgresql://sanix:19972017@localhost/flask_rest"
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir, 'db_repository')