import psycopg2
from main import host, user, password, db_name
from table_data import aa


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # with connection.cursor() as cursor:
    #     cursor.execute("""CREATE TABLE anime(
    #     id serial PRIMARY KEY,
    #     Name varchar(50) NOT NULL,
    #     Age integer NOT NULL,
    #     Height integer NOT NULL,
    #     Hair_color varchar(20) NOT NULL,
    #     Breast_size varchar(1) NOT NULL);""")

    # with connection.cursor() as cursor:
    #     insert_script = 'INSERT INTO anime (name, age, height, hair_color, breast_size) VALUES (%s, %s, %s, %s, %s)'
    #     for i in aa:
    #         cursor.execute(insert_script, i)

    # with connection.cursor() as cursor:
    #     cursor.execute(""" DROP TABLE anime;""")

except Exception as ex:
    print(ex)

else:
    connection.close()
    print("table close")
