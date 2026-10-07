from cliente import Cliente
from producto import Producto


def cargar_clientes():
    return [
        Cliente(1, "Ana", "Gómez", "ana@email.com"),
        Cliente(2, "Juan", "Pérez", "juan@email.com"),
    ]


def cargar_productos():
    return [
        Producto(1, "Remera básica", 15000, 10),
        Producto(2, "Pantalón", 28000, 5),
        Producto(3, "Zapatillas", 45000, 3),
    ]


def mostrar_menu(cliente):
    print("\n==============================")
    print("      MI ECOMMERCE")
    print("==============================")
    print(f"Cliente: {cliente.nombre} {cliente.apellido}")
    print(f"Email: {cliente.email}")
    print("------------------------------")
    print("1. Ver productos")
    print("2. Ver mis datos")
    print("3. Salir")


def mostrar_productos(productos):
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for producto in productos:
        producto.mostrar()


def main():
    clientes = cargar_clientes()
    productos = cargar_productos()

    cliente = clientes[0]

    while True:
        mostrar_menu(cliente)
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            cliente.mostrar()
        elif opcion == "3":
            print("¡Gracias por visitar el ecommerce!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
