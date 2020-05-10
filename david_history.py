import mysql.connector
import david
import datetime
from datetime import date
conn= mysql.connector.connect(host="localhost", user="root", passwd="", database="jar_history")
cus=conn.cursor()

def jarv_db(command):
    tm1=datetime.datetime.now().strftime("%H:%M:%S")
    cus.execute("insert into history_table(command, time_given) values('{}','{}');".format(command, tm1))
    conn.commit()

def show_his():
    cus.execute("select * from history_table")
    print("COMMAND   |   DATE   |   TIME")
    count=1
    for i in cus:
        print(f"{i[0]}   |   {i[1]}   |   {i[2]}")
        count=count+1
        
    print(f"\nTotal commands today:: {count}")
    count=0