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

    def to_dict(self):
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "apellido" : self.apellido,
            "email" : self.email
        }

    def actualizar_email(self):
        print(f"El email actual es: {self.email}")
        email_nuevo = input("Ingrese el nuevo email: ")
        return email_nuevo