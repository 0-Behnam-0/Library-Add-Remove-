import mysql.connector

def AddMemmber() :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO members (FirstName, LastName, NationalCode, PhoneNumber) VALUES (%s, %s, %s, %s)"
  firstname = input("Enter your first name : ")
  lastname = input("Enter your last name : ")
  nationalcode = int(input("Enter your national code : "))
  phonenumber = int(input("Enter your phone number :"))
  val = (firstname,lastname,nationalcode,phonenumber)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record(s) inserted.")

def AddBook () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO books (BookName , Subject , Number , Shaback , Price) VALUES (%s, %s, %s, %s, %s)"
  bookname = input("Enter your book name : ")
  subject = input("Enter the subject of your book : ")
  number = int(input("Enter number of the book : "))
  shaback = input("Enter shaback : ")
  price = int(input("Enter the price : "))
  val = (bookname,subject,number,shaback,price)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record(s) inserted.")

def DeleteBook () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  sql = "DELETE FROM books WHERE Shaback = %s"
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
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  sql = "DELETE FROM members WHERE NationalCode = %s"
  deletemember = input("Enter nationalcode of the member you want to remove : ")
  adr = (deletemember,)

  mycursor.execute(sql, adr)

  mydb.commit()

  print(mycursor.rowcount, "record(s) deleted")

def ShowBooks () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM books")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
def ShowMembers () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM members")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

def Barrow () :
  ShowMembers()
  person_barrowing = int(input("Enter national code of the person who wants to barrow book : "))
  ShowBooks()
  book_barrowed = int(input("Enter shaback of the book which barrowed : "))

  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )
  mycursor = mydb.cursor()
  mycursor.execute("SELECT memberid FROM members WHERE nationalcode = person_barrowing ")
  myresult_members = mycursor.fetchall()

  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )
  mycursor = mydb.cursor()
  mycursor.execute("SELECT bookid FROM books WHERE shaback = book_barrowed ")
  myresult_books = mycursor.fetchall()

  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )
  mycursor = mydb.cursor()
  sql = "INSERT INTO barrow (memberid, bookid) VALUES (%s, %s)"
  val = (myresult_members, myresult_books)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

  #///////////////////////////////////////////////////////////////////////////////////////////////////////
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  sql = "SELECT number FROM books WHERE shaback = %s"
  adr = (book_barrowed,)

  mycursor.execute(sql, adr)

  myresult = mycursor.fetchall()
  myresult = int(myresult) - 1

  for x in myresult:
    print(x)

def ShowBarrow () :
  mydb = mysql.connector.connect(
    host="localhost",
    user="Behnam",
    password="my@dmin.2002",
    database="librarybeta"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM barrow")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)


option = 9
while not option == 0 :
  # order = 9
  # while (order!=1)or(order!=2)or(order!=3)or(order!=4)or(order!=0) :
  order = int(input("Enter \'1\' to add member... \n\t  \'2\' to add book... \n\t  \'3\' to delete member... \n\t  \'4\' to delete book... \n\t  \'5\' to show the books... \n\t  \'6\' to show the members... \n\t  \'7\' to barrow book... \n\t  \'8\' to show barrow list... \n  \U000027A1 "))
  if order==1 :
    AddMemmber()
  elif order==2 :
    AddBook()
  elif order==3 :
    DeleteMember()
  elif order==4 :
    DeleteBook()
  elif order==5 :
    ShowBooks()
  elif order==6 :
    ShowMembers()
  elif order==7 :
    Barrow()
  elif order==8 :
    ShowBarrow()
  else:
    option = 0