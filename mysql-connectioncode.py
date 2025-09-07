import pymysql
connection = pymysql.connect(host='localhost', user='root', passwd='1234', db='sales')

mycursor = connection.cursor()
mycursor.execute('select * from student')
for row in mycursor:
    print(row)

# mycursor.execute('insert into student values (%s, %s)', ('PP', 'spl'))
#
# connection.commit()
print(mycursor.rowcount)