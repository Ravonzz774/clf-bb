from mysql.connector import connect, Error
import datetime
import clf

now = datetime.datetime.now()
try:
    with connect(
        host="127.0.0.1",
        user="root",
        database="timetable",
        autocommit=True
    ) as connection:
        query = f"""
               INSERT INTO TIMETABLE1(create_time,body)
               VALUES('{now.strftime('%Y-%m-%d %H:%M:%S')}','{str(clf.get()).replace("'",'"')}')
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
except Error as e:
    print(e)
