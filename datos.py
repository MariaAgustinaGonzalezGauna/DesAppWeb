# Lista en memoria simulando la base de datos
productos = []

def guardar_producto(producto):
    productos.append(producto)

def listar_productos():
    return productos
