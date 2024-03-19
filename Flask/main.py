from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/kishan'  # SQLite database file
db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.before_first_request
def create_tables():
    db.create_all()

#insert student record
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    student = Student(name, age)
    db.session.add(student)
    db.session.commit()

    return jsonify({'message': 'Student created successfully.'})


#get all student
@app.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    result = []
    for student in students:
        student_data = {
            'id': student.id,
            'name': student.name,
            'age': student.age
        }
        result.append(student_data)

    return jsonify(result)

#specific student
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found.'}), 404

    student_data = {
        'id': student.id,
        'name': student.name,
        'age': student.age
    }
    return jsonify(student_data)

#update student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found.'}), 404

    data = request.get_json()
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    db.session.commit()

    return jsonify({'message': 'Student updated successfully.'})

#delete student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found.'}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({'message': 'Student deleted successfully.'})


#main 
if __name__ == '__main__':
    app.run(debug=True)
