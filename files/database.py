from idlelib.debugobj import myrepr

import pymysql
from tkinter import messagebox
def connect_database():
    global mycursor
    global conn
    try:
        conn=pymysql.connect(host="localhost",user="root",password="1234")
        mycursor=conn.cursor()
    except:
        messagebox.showerror("Error","Something went wrong.Please open my sql before trying again")
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data(Id Varchar(20) , Name Varchar(50), Phone Varchar(15), Role Varchar(50),Gender Varchar(20),Salary DECIMAL(10,2))')


def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute("SELECT * FROM data")
    result=mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE from data where id=%s',id)
    conn.commit()

def search(option,value):
    mycursor.execute(f"SELECT * FROM data where {option}=%s",value)
    result =mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute("TRUNCATE TABLE data")
    conn.commit()



connect_database()