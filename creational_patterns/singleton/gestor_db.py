import pymysql
from singleton_meta_class import SingletonMetaClass


# This data should come from a .env
HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "1000036726As."
DATABASE_NAME = "prueba"
DATABASE_NAME_2 = "pomodoro_db"


class GestorDb(metaclass=SingletonMetaClass):

    def __init__(self, data_conexion):
        self.data_conexion = data_conexion

    def create_conexion(self) -> pymysql.connect:
        conexion = pymysql.connect(**self.data_conexion)
        return conexion

    def rewrite_data_conexion(self, data_conexion):
        self.data_conexion = data_conexion


data_conexion = {
    "host": HOST,
    "user": USER,
    "port": PORT,
    "password": PASSWORD,
    "database": DATABASE_NAME,
}

instance_gestor_db = GestorDb(data_conexion)
db_conexion = instance_gestor_db.create_conexion()

if db_conexion:
    with db_conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
        print("DATOS PRIMERA DB: ", result)


data_conexion_2 = data_conexion
data_conexion_2["database"] = DATABASE_NAME_2

instance_gestor_db.rewrite_data_conexion(data_conexion_2)
db_conexion = instance_gestor_db.create_conexion()

if db_conexion:
    with db_conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM table_scope")
        result = cursor.fetchall()
        print("DATOS SEGUNDA DB: ", result)
