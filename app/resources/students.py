from flask_restful import Resource, reqparse
from ..models import Student
from ..extensions import db
from ..schemas import StudentSchema

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument("first_name", required=True, help="First name is required")
parser.add_argument("last_name", required=True, help="Last name is required")
parser.add_argument("email", required=True, help="Email is required")
parser.add_argument("phone", required=True, help="Phone is required")
parser.add_argument("reason", required=False)
parser.add_argument("course_name", required=True, help="Course name is required")

class StudentListResource(Resource):
    def get(self):
        students = Student.query.all()
        return students_schema.dump(students), 200

    def post(self):
        args = parser.parse_args()
        student = Student(**args)
        db.session.add(student)
        db.session.commit()
        return student_schema.dump(student), 201

class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get_or_404(student_id)
        return student_schema.dump(student), 200

    def delete(self, student_id):
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return "", 204
