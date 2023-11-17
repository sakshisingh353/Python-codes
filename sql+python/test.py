import mysql.connector #importing the library

#connect to the database
mydb=mysql.connector.connect(
   host='localhost',
   user='user',
   password='password'
)

print(mydb.is_connected()) # connection established between the db and python

#how many databases are available 

cur=mydb.cursor() #connecting to pointers to browser

# cur.execute("create database system_db") #create a database in mysql
cur.execute("Use system_db")
# cur.execute("create table employees (name varchar(40),designation varchar(30),phone_number int , mail_id varchar(50))")
# cur.execute("insert into employees values ('Sakshi','data scientist',11234,'test@gmail.com')")
# cur.execute("insert into employees values ('Shekhar','web developer',1254,'test@gmail.com')")


# mydb.commit()

cur.execute("select * from employees")
for i in cur:
    print(i)
