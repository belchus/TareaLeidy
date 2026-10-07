class Cliente:
    def __init__(self, id_cliente, nombre, apellido, email):
        self.id = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def mostrar(self):
        print("\n--- DATOS DEL CLIENTE ---")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Email: {self.email}")
