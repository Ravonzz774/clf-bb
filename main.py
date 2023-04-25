import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="127.0.0.1",
        user="root",
        database="online_movie_rating"
    ) as connection:
        query = """
                CREATE TABLE test1(
                    id INT PRIMARY KEY,
                    name varchar(60)
                )
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
except Error as e:
    print(e)
