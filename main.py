import mysql.connector

def AddMemmber() :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="mydatabase"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO customers (FirstName, LastName, NationalCode, PhoneNumber) VALUES (%s, %s, %s, %s)"
  firstname = input("Enter your first name : ")
  lastname = input("Enter your last name : ")
  nationalcode = int(input("Enter your national code : "))
  phonenumber = int(input("Enter your phone number :"))
  val = (firstname,lastname,nationalcode,phonenumber)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")

def AddBook () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="mydatabase"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO customers (BookName , Subject , Number , Shaback , Price) VALUES (%s, %s, %s, %s, %s)"
  bookname = input("Enter your book name : ")
  subject = input("Enter the subject of your book : ")
  number = int(input("Enter number of the book : "))
  shaback = input("Enter shaback : ")
  price = int(input("Enter the price : "))
  val = (bookname,subject,number,shaback,price)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")

def DeleteBook () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="mydatabase"
  )

  mycursor = mydb.cursor()

  sql = "DELETE FROM customers WHERE Shaback = %s"
  deletebook = input("Enter shaback of the book you want to remove : ")
  adr = (deletebook,)

  mycursor.execute(sql, adr)

  mydb.commit()

  print(mycursor.rowcount, "record(s) deleted")

def DeleteMember () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="mydatabase"
  )

  mycursor = mydb.cursor()

  sql = "DELETE FROM customers WHERE NationalCode = %s"
  deletemember = input("Enter nationalcode of the book you want to remove : ")
  adr = (deletemember,)

  mycursor.execute(sql, adr)

  mydb.commit()

  print(mycursor.rowcount, "record(s) deleted")

option = 9
while not option == 0 :
  order = 9
  while (order!=1)or(order!=2)or(order!=3)or(order!=4)or(order!=0) :
    order = int(input("Enter \'1\' to add member... \n\t \'2\' to add book... \n\t \'3\' to delete member... \n\t \'4\' to delete book... \n\t Or enter \'0\' to exit : "))
  if order==1 :
    AddMemmber()
  elif order==2 :
    AddBook()
  elif order==3 :
    DeleteMember()
  elif order==4 :
    DeleteBook()
  else:
    option = 0