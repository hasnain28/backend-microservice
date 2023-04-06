from flask import Flask, jsonify
app = Flask(__name__)

instructors = [
    { 'firstName': "Muhammad Hasnain", 'lastName': "Zaib"  },
    { 'firstName': "Muhammad", 'lastName': "Hamza"  }
]
students = [
    { 'id': "1", 'firstName': "Muhammad", 'lastName': "Naeem"  },
    { 'id': "2",'firstName': "Muhammad", 'lastName': "Ali"  },
    { 'id': "3",'firstName': "Haris", 'lastName': "zaib"  },
    { 'id': "4",'firstName': "Haider", 'lastName': "Hussain"  },
    { 'id': "5",'firstName': "Hamid", 'lastName': "Tahir"  },
]

@app.route('/hello')
def hello():
    greeting = "Hello world!"
    return greeting

@app.route('/instructors', methods=["GET"])
def getInstructors():
    return jsonify(instructors)

@app.route('/students', methods=["GET"])
def getStudents():
    return jsonify(students)

@app.route('/instructor/<id>', methods=["GET"])
def getInstructor(id):
    id = int(id) - 1
    return jsonify(instructors[id])

@app.route('/student/<id>', methods=["GET"])
def getStudent(id):
    id = int(id) - 1
    return jsonify(students[id])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)