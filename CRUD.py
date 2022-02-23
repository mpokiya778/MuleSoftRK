import sqlite3
con=sqlite3.connect("Crud.db")
print('DB Created')

con.execute('create table Movies (mname varchar(20),actor varchar(20),actress varchar(20),year int,dname varchar(20))')
con.commit()
print('Table Created')

con.execute('insert into Movies(mname,actor,actress,year,dname) values("Vivah","Shahid Kapoor","Vani",2005,"Suraj Baraiya")')
con.commit()
print('inserted')

data=con.execute('select * from Movies')
for row in data:
    print('mname:{},actor:{},actress:{},year:{},dname:{}'.format(row[0],row[1],row[2],row[3],row[4]))
    con.commit()
