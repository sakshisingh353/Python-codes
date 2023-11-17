import mysql.connector #importing the library

#connect to the database
mydb=mysql.connector.connect(
   host='localhost',
   user='root',
   password='@Sakshi1243'
)

print(mydb.is_connected()) # connection established between the db and python

#how many databases are available 

cur=mydb.cursor() #connecting to pointers to browser
cur.execute("show databases") #write the query
for i in cur :
    print(i)
