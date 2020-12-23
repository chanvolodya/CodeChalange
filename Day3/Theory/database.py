import sqlite3
from sqlite3 import Error
# 1. Create a database if not exist
def create_connection(db_file):
    """Create a database connection to a SQLite db"""
    conn = None
    try:
        conn =sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn

# 2. Create a table student if not exists
def create_table(conn,create_table_sql):
    """Create a table from the crate_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#3. Insert data
def insert_data(conn,data_insert,infor_depart):
    """Insert data to table"""
    try:
        c = conn.cursor()
        c.execute(data_insert,infor_depart)
    except Error as e:
        print(e)
def main():

    database = "ManageStudents.db"
    student_table = """
        CREATE TABLE IF NOT EXISTS students (
            id_student integer PRIMARY KEY,
            name text NOT NULL,
            address text,
            id_departament integer NOT NULL,    
            FOREIGN KEY (id_departament) REFERENCES departaments (id)
             );
    """
    departament_table="""
        CREATE TABLE IF NOT EXISTS departaments (
            id integer PRIMARY KEY,
            name text NOT NULL,
            numberStudent integer
            );        
    """



    conn = create_connection(database)

    if conn is not None:
        create_table(conn,student_table)
        create_table(conn,departament_table)
    else:
        print("Error! cannot crate database connection")

    id_departament = input("Nhap ma khoa ")
    id_departament =int(id_departament)
    name_departament = input("Nhap ten khoa ")
    number_departament = input("So sinh vien la")
    number_departament = int(number_departament)
    infor_depart = (id_departament,name_departament,number_departament)
    data_insert_departament = """
            INSERT INTO departaments(id,name,numberStudent) VALUES(?,?,?)
            """
    insert_data(conn,data_insert_departament,infor_depart)
    conn.commit()
    conn.close()

    # id_student = input("Nhap id student ")
    # id_student = int(id_student)
    # name_student = input("Nhap ten sinh vien ")
    # address_student = input("Nhap dia chi sinh vien ")
    #
    # data_insert_student = f"""
    #         INSERT INTO students VALUES({id_student},{name_student},{address_student},{number_departament})
    #     """


    # insert_data(conn, data_insert_student)
    # id_student = input("Nhap id student ")
    # id_student = int(id_student)
    # name_student = input("Nhap ten sinh vien ")
    # address_student = input("Nhap dia chi sinh vien ")
    #
    # data_insert_student = f"""
    #         INSERT INTO students VALUES({id_student},{name_student},{address_student},{number_departament})
    #     """
    # insert_data(conn, data_insert_student)

if __name__ == '__main__':
    main()