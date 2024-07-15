import tkinter as tk
from tkinter import messagebox
from Sistema import Sistema

class BibliotecaGUI:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Préstamos de Biblioteca")
        self.tipo_usuario = None  # Almacena el tipo de usuario logueado
        self.crear_pantalla_login()

    def crear_pantalla_login(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Seleccione su tipo de usuario:", font=("Arial", 14)).pack(pady=10)
        
        tk.Button(frame, text="Estudiante", command=lambda: self.iniciar_sesion("Estudiante"), width=20, height=2).pack(pady=5)
        tk.Button(frame, text="Docente", command=lambda: self.iniciar_sesion("Docente"), width=20, height=2).pack(pady=5)
        tk.Button(frame, text="Administrador", command=lambda: self.iniciar_sesion("Administrador"), width=20, height=2).pack(pady=5)

    def iniciar_sesion(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario
        self.crear_menu()

    def crear_menu(self):
        self.limpiar_frame()
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        if self.tipo_usuario == "Administrador":
            self.libros_menu = tk.Menu(self.menu)
            self.usuarios_menu = tk.Menu(self.menu)
            self.prestamos_menu = tk.Menu(self.menu)
            
            self.menu.add_cascade(label="Libros", menu=self.libros_menu)
            self.menu.add_cascade(label="Usuarios", menu=self.usuarios_menu)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            
            self.libros_menu.add_command(label="Agregar Libro", command=self.agregar_libro)
            self.libros_menu.add_command(label="Modificar Stock", command=self.modificar_stock)
            
            self.usuarios_menu.add_command(label="Registrar Usuario", command=self.registrar_usuario)
            self.usuarios_menu.add_command(label="Buscar Usuario", command=self.buscar_usuario)
            
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
            self.prestamos_menu.add_command(label="Registrar Pago Multa", command=self.registrar_pago_multa)
            self.prestamos_menu.add_command(label="Aplicar Multa", command=self.aplicar_multa)
        
        elif self.tipo_usuario == "Docente":
            self.prestamos_menu = tk.Menu(self.menu)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
            self.prestamos_menu.add_command(label="Devolver Libro", command=self.devolver_libro)
        
        elif self.tipo_usuario == "Estudiante":
            self.prestamos_menu = tk.Menu(self.menu)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.realizar_prestamo)
            self.prestamos_menu.add_command(label="Devolver Libro", command=self.devolver_libro)
            self.prestamos_menu.add_command(label="Pagar Multa", command=self.pagar_multa)
        
    def agregar_libro(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Agregar Libro", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="Código:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(frame, text="Título:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')
        tk.Label(frame, text="Autor:", font=("Arial", 12)).grid(row=3, column=0, sticky='e')
        tk.Label(frame, text="Stock:", font=("Arial", 12)).grid(row=4, column=0, sticky='e')

        codigo = tk.Entry(frame, width=30)
        titulo = tk.Entry(frame, width=30)
        autor = tk.Entry(frame, width=30)
        stock = tk.Entry(frame, width=30)

        codigo.grid(row=1, column=1)
        titulo.grid(row=2, column=1)
        autor.grid(row=3, column=1)
        stock.grid(row=4, column=1)

        tk.Button(frame, text="Agregar", command=lambda: self.guardar_libro(codigo.get(), titulo.get(), autor.get(), stock.get()), width=15).grid(row=5, columnspan=2, pady=10)

    def guardar_libro(self, codigo, titulo, autor, stock):
        self.sistema.registrar_libro(codigo, titulo, autor, int(stock))
        messagebox.showinfo("Éxito", "Libro agregado exitosamente")
        self.limpiar_frame()

    def registrar_usuario(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Registrar Usuario", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="Tipo:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(frame, text="Nombre:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')
        tk.Label(frame, text="RUT:", font=("Arial", 12)).grid(row=3, column=0, sticky='e')
        tk.Label(frame, text="Contacto:", font=("Arial", 12)).grid(row=4, column=0, sticky='e')

        tipo = tk.Entry(frame, width=30)
        nombre = tk.Entry(frame, width=30)
        rut = tk.Entry(frame, width=30)
        contacto = tk.Entry(frame, width=30)

        tipo.grid(row=1, column=1)
        nombre.grid(row=2, column=1)
        rut.grid(row=3, column=1)
        contacto.grid(row=4, column=1)

        tk.Button(frame, text="Registrar", command=lambda: self.guardar_usuario(tipo.get(), nombre.get(), rut.get(), contacto.get()), width=15).grid(row=5, columnspan=2, pady=10)

    def guardar_usuario(self, tipo, nombre, rut, contacto):
        self.sistema.registrar_usuario(tipo, nombre, rut, contacto)
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
        self.limpiar_frame()

    def realizar_prestamo(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Realizar Préstamo", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="RUT Usuario:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(frame, text="Código Libro:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')

        rut = tk.Entry(frame, width=30)
        codigo_libro = tk.Entry(frame, width=30)

        rut.grid(row=1, column=1)
        codigo_libro.grid(row=2, column=1)

        tk.Button(frame, text="Prestar", command=lambda: self.prestar_libro(rut.get(), codigo_libro.get()), width=15).grid(row=3, columnspan=2, pady=10)

    def prestar_libro(self, rut, codigo_libro):
        prestamo = self.sistema.realizar_prestamo(rut, codigo_libro)
        if prestamo:
            messagebox.showinfo("Éxito", "Préstamo realizado exitosamente")
        else:
            messagebox.showwarning("Error", "No se pudo realizar el préstamo")
        self.limpiar_frame()

    def devolver_libro(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Devolver Libro", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="RUT Usuario:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(frame, text="Código Libro:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')

        rut = tk.Entry(frame, width=30)
        codigo_libro = tk.Entry(frame, width=30)

        rut.grid(row=1, column=1)
        codigo_libro.grid(row=2, column=1)

        tk.Button(frame, text="Devolver", command=lambda: self.devolver_libro_accion(rut.get(), codigo_libro.get()), width=15).grid(row=3, columnspan=2, pady=10)

    def devolver_libro_accion(self, rut, codigo_libro):
        devolucion = self.sistema.devolver_prestamo(rut, codigo_libro)
        if devolucion:
            messagebox.showinfo("Éxito", "Libro devuelto exitosamente")
        else:
            messagebox.showwarning("Error", "No se pudo devolver el libro")
        self.limpiar_frame()

    def buscar_usuario(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Buscar Usuario", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="RUT:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')

        rut = tk.Entry(frame, width=30)
        rut.grid(row=1, column=1)

        tk.Button(frame, text="Buscar", command=lambda: self.mostrar_usuario(rut.get()), width=15).grid(row=2, columnspan=2, pady=10)

    def mostrar_usuario(self, rut):
        usuario = self.sistema.buscar_usuario(rut)
        if usuario:
            info = f"Nombre: {usuario['nombre']}\nTipo: {usuario['tipo']}\nContacto: {usuario['contacto']}\nMulta: {usuario['multa']}"
            messagebox.showinfo("Información del Usuario", info)
        else:
            messagebox.showwarning("Error", "Usuario no encontrado")
        self.limpiar_frame()

    def registrar_pago_multa(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Registrar Pago Multa", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="RUT:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')

        rut = tk.Entry(frame, width=30)
        rut.grid(row=1, column=1)

        tk.Button(frame, text="Registrar Pago", command=lambda: self.pago_multa(rut.get()), width=15).grid(row=2, columnspan=2, pady=10)

    def pago_multa(self, rut):
        self.sistema.registrar_pago_multa(rut)
        messagebox.showinfo("Éxito", "Pago de multa registrado exitosamente")
        self.limpiar_frame()

    def modificar_stock(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Modificar Stock", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="Código Libro:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(frame, text="Nuevo Stock:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')

        codigo_libro = tk.Entry(frame, width=30)
        nuevo_stock = tk.Entry(frame, width=30)

        codigo_libro.grid(row=1, column=1)
        nuevo_stock.grid(row=2, column=1)

        tk.Button(frame, text="Modificar", command=lambda: self.actualizar_stock(codigo_libro.get(), nuevo_stock.get()), width=15).grid(row=3, columnspan=2, pady=10)

    def actualizar_stock(self, codigo_libro, nuevo_stock):
        self.sistema.modificar_stock(codigo_libro, int(nuevo_stock))
        messagebox.showinfo("Éxito", "Stock modificado exitosamente")
        self.limpiar_frame()

    def aplicar_multa(self):
        self.limpiar_frame()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Aplicar Multa", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="RUT Usuario:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(frame, text="Monto Multa:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')

        rut = tk.Entry(frame, width=30)
        monto_multa = tk.Entry(frame, width=30)

        rut.grid(row=1, column=1)
        monto_multa.grid(row=2, column=1)

        tk.Button(frame, text="Aplicar", command=lambda: self.aplicar_multa_accion(rut.get(), monto_multa.get()), width=15).grid(row=3, columnspan=2, pady=10)

    def aplicar_multa_accion(self, rut, monto_multa):
        self.sistema.aplicar_multa(rut, int(monto_multa))
        messagebox.showinfo("Éxito", "Multa aplicada exitosamente")
        self.limpiar_frame()

    def limpiar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    sistema = Sistema()  # Instancia del sistema de biblioteca
    app = BibliotecaGUI(root, sistema)
    root.mainloop()