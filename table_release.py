import psycopg2
from main import host, user, password, db_name
from table_data import aa, aa2, aa3
import time


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True


    def print_waifus_from_db(sql_request):
        with connection.cursor() as cursor:
            cursor.execute(sql_request)
            for i in cursor.fetchall():
                print(f"Имя - {i[1]}, возраст - {i[2]}, рост - {i[3]}, цвет волос - {i[4]}, размер груди - {i[5]}, номер в таблице - {i[0]}")

    def defname(name):
        sql_request = f"""SELECT * FROM anime WHERE name = \'{name}\';"""
        print_waifus_from_db(sql_request)
        
    def defage(age):
        sql_request = f"""SELECT * FROM anime WHERE age <= \'{age}\';"""
        print_waifus_from_db(sql_request)

    def defheight(height):
        sql_request = f"""SELECT * FROM anime WHERE eight <= \'{height}\';"""
        print_waifus_from_db(sql_request)

    def defhair(hair):
        sql_request = f"""SELECT * FROM anime WHERE hair_color = \'{hair}\';"""
        print_waifus_from_db(sql_request)

    def defsize(size):
        sql_request = f"""SELECT * FROM anime WHERE breast_size = \'{size}\';"""
        print_waifus_from_db(sql_request)
    

    sfx = input("Введите один из перечисленных параметров: name, age, height, hair_color, breast_size - ").lower()
    
    if sfx == "name":
        print("Выберите одно из имён: ")
        time.sleep(2)
        for i in aa:
            print(i[0])
        inpname = input("Ваш выбор: ")
        defname(inpname)

    elif sfx == "age":
        inpage = input("Укажите верхнюю границу возраста: ")
        defage(inpage)

    elif sfx == "height":
        inpheight = input("Укажите максимально допустимый рост: ")
        defheight(inpheight)

    elif sfx == "hair_color":
        print("Выберите один из представленных цветов: ")
        time.sleep(1)
        for i in aa2:
            print(i)
        inphair = input("Ваш выбор: ")
        defhair(inphair)

    elif sfx == "breast_size":
        print("Какой размер вам нравится: ")
        time.sleep(1)
        for i in aa3:
            print(i)
        inpsize = input("Ваш выбор: ")
        defsize(inpsize)


except Exception as ex:
    print(ex)

else:
    connection.close()
    print("До скорых встреч")
