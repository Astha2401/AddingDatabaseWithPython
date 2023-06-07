import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="c361cohort"
)
cursor =connection.cursor()
create_table_query="""CREATE TABLE if not exists table_name3(id int auto_increment primary key , column1 varchar(255), column2 int)"""

cursor.execute(create_table_query)
print("Table created successfully")

insert_query="insert into table_name3 (column1,column2) values (%s,%s)"

data=[("Value1",33),("Value2",55)]
cursor.executemany(insert_query,data)

connection.commit()

selectquery ="select * from table_name3"
cursor.execute(selectquery)

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
cursor.close()    
connection.close()