from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
from flask import Flask, request
a = Flask(__name__)
engine = create_engine('sqlite:///task_1.db', echo=True)
meta = MetaData()

student = Table(
    'student', meta,
    Column('USN', Integer, primary_key=True),
    Column('Name', String),
    Column('Gender', String),
    Column('Entry', String),
    Column('YOA', Integer),
    Column('Migration', Boolean),
    Column('Transfer_details', String),
    Column('admission_in_seperate division', Boolean),
    Column('YOP', Integer),
    Column('degree_type', String),
    Column('pu_marks', Integer),
    Column('entrance_marks', Integer),
    Column('rank', Integer)
)
meta.create_all(engine)
conn = engine.connect()


def create():
    N = int(input("Enter the number of student's details to be entered: "))
    for i in range(N):
        USN = int(input("Enter the USN of the student: "))
        Name = str(input("Enter the name of the student: "))
        Gender = str(input("Gender :"))
        Entry = str(input("Type of entry(Normal/Lateral) : "))
        YOA = int(input("Enter the year of admission : "))
        Migration = str(
            input("Has the student migrated to other programs or institutions(Yes/No):"))
        if Migration == "Yes":
            Migration == 1
            Transfer_details = str(input("Enter the details of transfer :"))
        else:
            Migration == 0
            Transfer_details = None
        admission = str(
            input("Did the student take admission in separate division(Yes/No) :"))
        if admission == "Yes":
            admission == 1
            admission = str(
                input("Enter the details of admission in seperate division :"))
        else:
            admission == 0
            admission = None
        yop = int(input("Year of passing :"))
        degree = str(input("UG/PG : "))
        marks = int(input("Marks obtained in 12th in PCM subjects :"))
        entrance_marks = int(input("Marks obtained in entrance exam :"))
        rank = int(input("Rank in entrance exam :"))
        result = conn.execute(student.insert(),
                              ([{'usn': USN, 'name': Name, 'gender': Gender, 'entry': Entry, 'yoa': YOA, 'migration': Migration,
                                'transfer_details': Transfer_details, 'Admission': admission, 'YOP': yop, 'degree': degree, 'marks': marks, 'entrance_marks': entrance_marks, 'rank': rank}]))


def read():
    t = student.select()
    conn = engine.connect()
    result = conn.execute(t)
    for row in result:
        print(row)


def update():
    old = int(input("Enter the original USN of the student: "))
    new = str(input("Enter the new name of the student: "))
    conn = engine.connect()
    stmt = student.update().where(student.c.USN == old).values(Name=new)
    conn.execute(stmt)
    t = student.select()
    conn.execute(t).fetchall()


def delete():
    x = input("Enter the USN of the student whose record has to deleted: ")
    conn = engine.connect()
    stmt = student.delete().where(student.c.USN == x)
    conn.execute(stmt)
    t = student.select()
    conn.execute(t).fetchall()


@a.route('/1', methods=['POST'])
def task():
    body = request.get_json()
    x = create(body)
    return x


@a.route('/2', methods=['PUT'])
def TASK():
    body = request.get_json()
    y = update(body)
    return y


@a.route('/3', methods=['GET'])
def tsk():
    body = request.get_json()
    z = read(body)
    return z


@a.route('/4', methods=['DELETE'])
def ts():
    body = request.get_json()
    b = delete(body)
    return b


if __name__ == '__main__':
    a.run(debug=True)

operation_dict = {1: create, 2: read, 3: update, 4: delete}

while(True):
    operation = int(input("""To perform the following operations:
        Press 1 to enter new values:
        Press 2 to view the table:
        Press 3 to update the records:
        Press 4 to delete a record: """))
    performing = operation_dict[operation]()
