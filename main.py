from cliente import Cliente
from producto import Producto
import json


def cargar_clientes():
    return [
        Cliente(1, "Ana", "Gómez", "ana@email.com"),
        Cliente(2, "Juan", "Pérez", "juan@email.com"),
        Cliente(3, "Leidy", "Herrera", "leidy@email.com"),
        Cliente(4, "Violetta", "Tovar", "violetta@email.com")
    ]

def guardar_cliente(lista_cliente): 
    cliente_diccionario = [cliente.to_dict() for cliente in lista_cliente]
    with open("datos\clientes.json", "w", encoding="utf-8") as archivo:
        json.dump(cliente_diccionario, archivo, indent=4, ensure_ascii=False)
    print("Clientes guardados correctamente.")

def cargar_productos():
    return [
        Producto(1, "Remera básica", 15000, 10),
        Producto(2, "Pantalón", 28000, 5),
        Producto(3, "Zapatillas", 45000, 3),
        Producto(4, "Vestido estampado", 30500, 7)
    ]

def guardar_producto(lista_producto): 
    producto_diccionario = [producto.to_dict() for producto in lista_producto]
    with open("datos\productos.json", "w", encoding="utf-8") as archivo:
        json.dump(producto_diccionario, archivo, indent=4, ensure_ascii=False)
    print("Productos guardados correctamente.")


def mostrar_menu(cliente):
    print("\n==============================")
    print("      VENUS CLOTHES")
    print("==============================")
    print(f"Cliente: {cliente.nombre} {cliente.apellido}")
    print(f"Email: {cliente.email}")
    print("------------------------------")
    print("1. Ver productos")
    print("2. Ver mis datos")
    print("3. Actualizar email")
    print("4. Salir")


def mostrar_productos(productos):
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for producto in productos:
        producto.mostrar()  


def main():
    clientes = cargar_clientes()
    productos = cargar_productos()

    guardar_producto(productos)
    guardar_cliente(clientes)

    cliente_actual = int(input("Ingrese su id: "))
    cliente_encontrado = None

    for cliente in clientes:
        if cliente.id == cliente_actual:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado is None:
            print("El cliente no existe.")
            return
    
    while True:
        mostrar_menu(cliente_encontrado)
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            cliente.mostrar()
        elif opcion == "3":
            email_nuevo = cliente.actualizar_email()
            cliente.email = email_nuevo
            print(f"Se actualizó correctamente el email.")
        elif opcion == "4":
            print("¡Gracias por visitar VENUS CLOTHES, vuelve pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()