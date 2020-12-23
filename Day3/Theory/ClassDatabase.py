import sqlite3
from sqlite3 import Error
class Database:
    '''Class DATABASE store data of students and their departament'''
    def __init__(self,name_database):
        self.name_database = name_database


    def create_database(self):
        """Create data base"""
        conn = None
        try:
            conn = sqlite3.connect(f"{self.name_database}.db")
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(self,conn,create_table_sql):
        """Create table if not exits"""
        try:
            c =conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_data(self,conn,insert_table_sql,values_insert):
        try:
            c = conn.cursor()
            c.execute(insert_table_sql,values_insert)
        except Error as e:
            print(e)
        conn.commit()
