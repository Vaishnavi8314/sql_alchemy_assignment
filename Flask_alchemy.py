from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tps.db'
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
engine = create_engine('sqlite:///task_1.db', echo=True)
meta = MetaData()


students = Table(
    'students', meta,
    Column('USN', Integer, primary_key=True),
    Column('Name', String),
    Column('Gender', String),
    Column('Entry', String),
    Column('YOA', Integer),
    Column('Migration', Boolean),
    Column('Transfer_details', String),
    Column('Admission', Boolean),
    Column('Admission_div', String),
    Column('YOP', Integer),
    Column('degree_type', String),
    Column('pu_marks', Integer),
    Column('entrance_marks', Integer),
    Column('rank', Integer)
)
meta.create_all(engine)


def create(body):
    conn = engine.connect()
    N = int(body['N'])
    for i in range(N):
        USN = str(body['USN'])
        Name = str(body['Name'])
        Gender = str(body['Gender'])
        Entry = str(body['Entry'])
        YOA = int(body['Year of admission'])
        Migration = str(body['Migration'])
        if Migration == "Yes":
            Migration = True
        elif Migration == "No":
            Migration = False
        Transfer_details = str(body['transfer_details'])
        Admission = str(body['admission'])
        if Admission == "Yes":
            Admission = True
        elif Admission == "No":
            Admission = False
        Admission_div = str(body['admission_division'])
        YOP = int(body['Year of passing'])
        degree = str(body['degree_type'])
        marks = int(body['marks'])
        entrance_marks = int(body['entrance_marks'])
        rank = int(body['rank'])
        result = students.insert().values(USN=USN, Name=Name, Gender=Gender, Entry=Entry, YOA=YOA, Migration=Migration,
                                          Transfer_details=Transfer_details, Admission=Admission, Admission_div=Admission_div, YOP=YOP, degree=degree, marks=marks, entrance_marks=entrance_marks, rank=rank)
        x = conn.execute(result)
        return "Inserted successfully"


def read():

    conn = engine.connect()
    view = students.select()
    result = conn.execute(view)
    for row in result:
        print(row)


def update(body):
    conn = engine.connect()
    a = dict(body)
    usn = str(body['USN'])
    for key, value in a.items():
        new = students.update().where(
            students.c.USN == usn).values({key: value})
        result = conn.execute(new)

        return "Updated successfully"


def delete(body):
    x = body['USN']
    conn = engine.connect()
    stmt = students.delete().where(students.c.USN == x)
    result = conn.execute(stmt)
    return "Successfully Deleted"


@app.route('/create', methods=['POST'])
def add():
    body = request.get_json()
    result = create(body)
    return result


@app.route('/read', methods=['GET'])
def view():
    body = request.get_json()
    result = read(body)
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
