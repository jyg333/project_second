"""Access AWS RDS"""

import pymysql

host_name = 'database-1.clq1g0g3exq8.ap-northeast-2.rds.amazonaws.com'

user_name = 'seamus'
pass_word = 'hidden'
db_name = 'database-1'

db = pymysql.connect(host=host_name,port=3306,user= user_name,passwd=pass_word)
# db = pymysql.connect('database-1.clq1g0g3exq8.ap-northeast-2.rds.amazonaws.com','seamus',passwd=pass_word,'database-1')

cursor = db.cursor()
cursor.execute("select version()")



data =cursor.fetchone()
print(data)

# sql = """create database test01"""
# cursor.execute(sql)
# cursor.connection.commit()

sql01 = """use test01 """
cursor.execute(sql01)

# sql02 = """create table test01.stock(
#     id int not null auto_increment,
#     fname text,
#     lname text,
#     primary key (id))"""
# cursor.execute(sql02)

sql03 = """show tables"""
# sql04 = """show tables"""
cursor.execute(sql03)

sql05 = """show columns from stock"""
print("22",cursor.execute(sql05))
a = cursor.fetchall()

# print(a[1])

cursor.close()
