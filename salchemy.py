from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
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
    Column('admission', Boolean),
    Column('admission_div', String),
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
            Migration = True
        elif Migration == "No":
            Migration = False
        Transfer_details = str(input("Enter the details of transfer :"))
        admission = str(
            input("Did the student take admission in separate division(Yes/No) :"))
        if admission == "Yes":
            admission = True
        elif admission == "No":
            admission = False
        admission_div = str(
            input("Enter the details of admission in seperate division :"))
        YOP = int(input("Year of passing :"))
        degree = str(input("UG/PG : "))
        marks = int(input("Marks obtained in 12th in PCM subjects :"))
        entrance_marks = int(input("Marks obtained in entrance exam :"))
        rank = int(input("Rank in entrance exam :"))
        result = conn.execute(student.insert(),
                              ([{'USN': USN, 'Name': Name, 'Gender': Gender, 'Entry': Entry, 'YOA': YOA, 'Migration': Migration,
                                'Transfer_details': Transfer_details, 'admission': admission, 'admission_div': admission_div, 'YOP': YOP, 'degree': degree, 'marks': marks, 'entrance_marks': entrance_marks, 'rank': rank}]))


def read():
    t = student.select()
    conn = engine.connect()
    result = conn.execute(t)
    for row in result:
        print(row)


def update():
    old = int(input("Enter the original USN of the student: "))
    new = input("Enter the columns to be changed in dictionary format : ")
    new = eval(new)
    for key, value in new.items():
        print(key, value)
        updated = student.update().where(student.c.USN == old).values(key=value)
    result = conn.execute(updated)


def delete():
    x = input("Enter the USN of the student whose record has to deleted: ")
    conn = engine.connect()
    stmt = student.delete().where(student.c.USN == x)
    read()
    conn.execute().fetchall()


operation_dict = {1: create, 2: read, 3: update, 4: delete}

while(True):
    operation = int(input("""To perform the following operations:
        Press 1 to enter new values:
        Press 2 to view the table:
        Press 3 to update the records:
        Press 4 to delete a record: """))
    performing = operation_dict[operation]()
