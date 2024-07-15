import mysql.connector
from mysql.connector import Error

class BibliotecaDAO:
    def __init__(self, db_config):
        """ Inicializa el DAO con la conexión a la base de datos """
        self.connection = self.create_connection(db_config)
    
    def create_connection(self, db_config):
        """ Crea una conexión a la base de datos MySQL """
        try:
            conn = mysql.connector.connect(**db_config)
            if conn.is_connected():
                print("Conexión establecida a la base de datos.")
            return conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def create_table(self, create_table_sql):
        """ Crea una tabla usando la sentencia SQL pasada como argumento """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Tabla creada exitosamente.")
        except Error as e:
            print(f"Error al crear la tabla: {e}")

    def insert_libro(self, libro):
        """ Inserta un libro en la tabla de libros """
        sql = ''' INSERT INTO libros(codigo, titulo, autor, stock)
                  VALUES(%s, %s, %s, %s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, libro)
            self.connection.commit()
            print("Libro agregado exitosamente.")
        except Error as e:
            print(f"Error al insertar libro: {e}")

    def select_libro_by_codigo(self, codigo):
        """ Selecciona un libro por su código """
        sql = ''' SELECT * FROM libros WHERE codigo=%s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (codigo,))
            libro = cursor.fetchone()
            return libro
        except Error as e:
            print(f"Error al seleccionar libro: {e}")
            return None

    def update_libro_stock(self, codigo, stock):
        """ Actualiza el stock de un libro """
        sql = ''' UPDATE libros
                  SET stock = %s
                  WHERE codigo = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (stock, codigo))
            self.connection.commit()
            print("Stock del libro actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar el stock del libro: {e}")

    def delete_libro(self, codigo):
        """ Elimina un libro por su código """
        sql = ''' DELETE FROM libros WHERE codigo = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (codigo,))
            self.connection.commit()
            print("Libro eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar el libro: {e}")