from . import app,db
from flask import request,jsonify
from .models import Student




@app.route('/')
def hello():
    message={"message":"Hey there Welcome to my awesome Student API"}
    return jsonify(message)

#create a student
@app.route('/students',methods=['POST'])
def create_student():
    name=request.json.get('name')
    age=request.json.get('age')
    grade=request.json.get('grade')
    new_student=Student(name=name,age=age,grade=grade)
    db.session.add(new_student)
    db.session.commit()

    message={"message":"New Student Created Successfully"}

    return jsonify(message)


#retrieve all students
@app.route('/students',methods=['GET'])
def get_all_students():
    students=Student.query.all()

    all_students = []
    for student in students:
        std_obj = {}
        std_obj["id"]=student.id
        std_obj["name"]=student.name
        std_obj["age"]=student.age
        std_obj["grade"]=student.grade
        all_students.append(std_obj)

    return jsonify({"students":all_students})



#retrieve a student with a particular id
@app.route('/students/<int:id>',methods=['GET'])
def get_a_student(id):
    student=Student.query.get(id)

    if student is None:
        return jsonify({"message":"Student does not exist"})
    std_obj={}
    std_obj["id"]=student.id
    std_obj["name"]=student.name
    std_obj["grade"]=student.grade
    std_obj["age"]=student.grade
    return jsonify({"student":std_obj})

#update a student's info
@app.route('/students/<int:id>',methods=['PATCH'])
def update_info(id):
    student_to_update=Student.query.get(id)
    if student_to_update is None:
        return jsonify({"message":"student not found"})
    student_to_update.name=request.json.get('name')
    student_to_update.age=request.json.get('age')
    student_to_update.grade=request.json.get('grade')
    db.session.commit()
    message={"message":"Info updated successfully"}
    return jsonify(message)

#delete a student
@app.route('/students/<int:id>')
def delete_a_student(id):
    student_to_del=Student.query.get(id)
    if not student_to_del:
        return jsonify({"message":"Student not found"})
    db.session.delete(student_to_del)





