import mysql.connector


#connection de SGBD
mydb = mysql.connector.connect(host="localhost", user="root",password="", database='mydatabase')


#fait la connection
mycursor = mydb.cursor()

sql="delete from client where id=4"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")

mycursor.execute("SELECT * FROM client ")
myresult = mycursor.fetchall()
for x  in myresult:
    print(x)




# sql ="INSERT INTO client (nom, adresse) VALUES (%s, %s)"
# val = [("Hamza","Balabla"),("Abdillahi","hodan"),("Zeinab","pk12"),("Ifrah","Q1")]


# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record inserted.")



#execute une requette
#mycursor.execute("CREATE DATABASE mydatabase")


#creation d'une table
#mycursor.execute("create table client (id int AUTO_INCREMENT PRIMARY KEY, nom varchar(200), adresse varchar(200))")

# for x in mycursor:
#     print(x)