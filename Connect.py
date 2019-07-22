import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="ashwin1233", password="ashwin", database="ashwin")

mycursor = mydb.cursor()

def add(name,city):
    sql = "INSERT INTO student (name,college) VALUES (%s, %s)"
    val = (name,city)
    mycursor.execute(sql,val)
    return "success"

def update(name,new_name):
    mycursor.execute("UPDATE student SET name='pram' WHERE name = 'prem'")
    return "success"
def delete(name):
    mycursor.execute(("DELETE From student where name='pram'"))
    return "success"

def view():
    mycursor.execute("select * from student")
    for i in mycursor:
        print(i)
    return "success"


add("test1","hyd")
view()
