import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="ashwin1233", password="ashwin", database="ashwin")

mycursor = mydb.cursor()

mycursor.execute("INSERT into student values ('Manju', 'Pune'), ('Monica', 'Devi') ")

mycursor.execute("UPDATE student SET name='pram' WHERE name = 'prem'")
mycursor.execute(("DELETE FROM student WHERE name='pram'"))
mycursor.execute("select * from student")



for i in mycursor:
    print(i)