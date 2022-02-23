import sqlite3
con=sqlite3.connect('CRUD.db')
class hello:
    def __init__(self):
       pass

    def insert():
         mname=input('Enter Movie name:')
         actor=input('Enter Actor name:')
         actress=input('Enter Actress name:')
         year=int(input('Enter Year:'))
         dname=input('Enter Director name:')
         con.execute('insert into Movies(mname,actor,actress,year,dname)values(?,?,?,?,?)',(mname,actor,actress,year,dname))
         con.commit()

    def display():
        data=con.execute('select * from Movies')
        for row in data:
            print('mname:{},actor:{},actress:{},year:{},dname:{}'.format(row[0],row[1],row[2],row[3],row[4]))
            con.commit()
h1=hello
h1.insert()
h1.display()