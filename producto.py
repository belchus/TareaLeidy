class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(
            f"ID: {self.id} | "
            f"{self.nombre} | "
            f"${self.precio:,.2f} | "
            f"Stock: {self.stock}"
        )
