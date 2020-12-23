from ClassDatabase import Database

db = Database("Student")
conn= db.create_database()
create_table_student ="""
    CREATE TABLE IF NOT EXISTS student(
        id integer PRIMARY KEY,
        name_sudent text NOT NULL,
        address text NOT NULL,
        id_departament integer,
        FOREIGN KEY (id_departament) REFERENCES departaments (id)
    );
"""
create_table_departament="""
        CREATE TABLE IF NOT EXISTS departaments (
            id integer PRIMARY KEY,
            name text NOT NULL,
            numberStudent integer
            );        
    """


def insert_departament_data():
    id = int(input("Enter id of departament "))
    name = input("Enter name of departament ")
    numberStudent =int (input("Enter number of departament"))
    values = (id,name,numberStudent)
    return values

def insert_student_data(id_departamnet):
    id_student = input("Nhap id student ")
    id_student = int(id_student)
    name_student = input("Nhap ten sinh vien ")
    address_student = input("Nhap dia chi sinh vien ")
    id_departamnet =id_departamnet
    values = (id_student, name_student, address_student,id_departamnet)
    return values


# values_departament =insert_departament_data()
values_student = insert_student_data(1)
insert_departaments_sql ="""
        INSERT INTO departaments(id,name,numberStudent) VALUES(?,?,?)
"""
insert_student_sql = """
        INSERT INTO student(id,name_sudent,address,id_departament) VALUES(?,?,?,?)
"""
db.create_table(conn,create_table_departament)
db.create_table(conn,create_table_student)
# Insert Departament
# db.insert_data(conn,insert_departaments_sql,values_departament)
#Insert Student
db.insert_data(conn,insert_student_sql,values_student)
