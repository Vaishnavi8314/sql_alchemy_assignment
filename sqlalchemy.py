#Commented USN column as the entries to it is showing as 'Datatype Mismatch'. Except that issue everything works fine
#Due to no access to USN , update and delete are on halt, the iterating and fetching vales from user given data is ready, but without USN
# we can't access that.

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean
engine = create_engine('sqlite:///task_1.db', echo=True)
meta = MetaData()

study = Table(
    'student', meta,
    #Column('USN', String, primary_key= True),
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
    Column('rank', Integer), 
)
meta.create_all(engine)
conn = engine.connect()


def create():
    N = int(input("Enter the number of student's details to be entered: "))
    for i in range(N):
        #USN = input("Enter the USN of the student: ")
        Name = input("Enter the name of the student: ")
        Gender = input("Gender :")
        Entry = input("Type of entry(Normal/Lateral) : ")
        YOA = input("Enter the year of admission : ")
        
        Migration = input("Has the student migrated to other programs or institutions(Yes/No):")
        if Migration == "Yes":
            Migration = True
        elif Migration == "No":
            Migration = False
        
        Transfer_details = input("Enter the details of transfer :")
        admission = input("Did the student take admission in separate division(Yes/No) :")
        if admission == "Yes":
            admission = True
        elif admission == "No":
            admission = False
        admission_div = input("Enter the details of admission in separate division :")
        YOP = input("Year of passing :")
        degree = input("UG/PG : ")
        marks = input("Marks obtained in 12th in PCM subjects :")
        entrance_marks = input("Marks obtained in entrance exam :")
        rank = input("Rank in entrance exam :")
        result = conn.execute(study.insert(),
                              [{'Name': Name, 'Gender': Gender, 'Entry': Entry, 'YOA': YOA , 'Migration': Migration,
                                'Transfer_details': Transfer_details, 'admission': admission, 'admission_div': admission_div,
                               'YOP': YOP, 'degree_type': degree, 'pu_marks': marks, 'entrance_marks': entrance_marks, 'rank': rank
                              }])
        
def read():
    dataview = study.select()
    result = conn.execute(dataview)
    for row in result:
        print (row)

'''def update():
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
 '''

