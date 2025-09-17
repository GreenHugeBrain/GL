from .extensions import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    reason = db.Column(db.Text, nullable=True)
    course_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"
