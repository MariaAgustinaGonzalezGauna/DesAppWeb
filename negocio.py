from datos import guardar_producto, listar_productos

def agregar_producto(nombre):
    producto = {'nombre': nombre}
    guardar_producto(producto)
    return 'Producto agregado con éxito'

def obtener_productos():
    return listar_productos()
