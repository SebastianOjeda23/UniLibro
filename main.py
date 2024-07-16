from tkinter import Tk
from Bibliotecagui import BibliotecaGUI
from Sistema import Sistema
from BibliotecaDAO import BibliotecaDAO

db_config = {
    'host': 'localhost',
    'user': 'root',
    'database': 'cun102652_UniLibros'
}

if __name__ == "__main__":
    try:
        dao = BibliotecaDAO(db_config)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS libros (
            codigo VARCHAR(255) PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            autor VARCHAR(255) NOT NULL,
            stock INT NOT NULL
        )
        """
        dao.create_table(create_table_sql)
    except Exception as e:
        print(f"No se pudo conectar a la base de datos: {e}")
        dao = None

    sistema = Sistema()
    root = Tk()
    app = BibliotecaGUI(root, sistema)
    root.mainloop()