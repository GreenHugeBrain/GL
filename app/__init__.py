from flask import Flask
from flask_restful import Api
from .extensions import db, migrate
from .resources.students import StudentListResource, StudentResource

def create_app():
    app = Flask(__name__)
    
    # Config
    app.config.from_object("config.Config")
    
    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # API
    api = Api(app)
    api.add_resource(StudentListResource, "/students")
    api.add_resource(StudentResource, "/students/<int:student_id>")
    
    return app
