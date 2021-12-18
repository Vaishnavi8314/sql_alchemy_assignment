from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tps.db'
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

meta = db.MetaData()


students = db.Table(
    'student', meta,
    db.Column('USN', db.String, primary_key=True),
    db.Column('Name', db.String),
    db.Column('Gender', db.String),
    db.Column('Entry', db.String),
    db.Column('YOA', db.Integer),
    db.Column('Migration', db.Boolean),
    db.Column('Transfer_details', db.String),
    db.Column('Admission', db.Boolean),
    db.Column('Admission_div', db.String),
    db.Column('YOP', db.Integer),
    db.Column('degree_type', db.String),
    db.Column('pu_marks', db.Integer),
    db.Column('entrance_marks', db.Integer),
    db.Column('rank', db.Integer)
)
meta.create_all(db.engine)


def create(body):
    conn = db.engine

    USN = str(body['USN'])
    Name = str(body['Name'])
    Gender = str(body['Gender'])
    Entry = str(body['Entry'])
    YOA = int(body['YOA'])
    Migration = str(body['Migration'])
    if Migration == "Yes":
        Migration = True
    elif Migration == "No":
        Migration = False
    Transfer_details = str(body['Transfer_details'])
    Admission = str(body['Admission'])
    if Admission == "Yes":
        Admission = True
    elif Admission == "No":
        Admission = False
    Admission_div = str(body['Admission_div'])
    YOP = int(body['YOP'])
    degree = str(body['degree_type'])
    marks = int(body['marks'])
    entrance_marks = int(body['entrance_marks'])
    rank = int(body['rank'])
    result = students.insert().values({'USN': USN, 'Name': Name, 'Gender': Gender, 'Entry': Entry, 'YOA': YOA, 'Migration': Migration,
                                      'Transfer_details': Transfer_details, 'Admission': Admission, 'Admission_div': Admission_div, 'YOP': YOP, 'degree': degree, 'marks': marks, 'entrance_marks': entrance_marks, 'rank': rank})
    x = db.engine.execute(result)
    db.session.commit()
    return "Inserted successfully"


def read():

    view = students.select()
    result = db.engine.execute(view)
    row_list = []
    for row in result.fetchall():
        row_list.append(dict(row))
    return jsonify(row_list)


def update(body):

    a = dict(body)
    usn = str(body['USN'])
    for key, value in a.items():
        new = students.update().where(
            students.c.USN == usn).values({key: value})
        result = db.engine.execute(new)

        return "Updated successfully"


def delete(body):
    x = body['USN']

    stmt = students.delete().where(students.c.USN == x)
    result = db.engine.execute(stmt)
    return "Successfully Deleted"


@app.route('/create', methods=['POST'])
def add():
    body = request.get_json()
    result = create(body)
    return result


@app.route('/read', methods=['GET'])
def view():

    result = read()
    return result


@app.route('/update', methods=['PUT'])
def change():
    body = request.get_json()
    result = update(body)
    return result


@app.route('/delete', methods=['DELETE'])
def deleting():
    body = request.get_json()
    result = delete(body)
    return result


if __name__ == '__main__':
    app.run(debug=True, port=5000)
