from flask import Flask, request, jsonify
from negocio import agregar_producto, obtener_productos

app = Flask(__name__)

@app.route('/agregar', methods=['POST'])
def agregar():
    data = request.get_json()
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({'error': 'Nombre es requerido'}), 400

    resultado = agregar_producto(nombre)
    return jsonify({'mensaje': resultado}), 201

@app.route('/productos', methods=['GET'])
def listar():
    productos = obtener_productos()
    return jsonify(productos), 200

if __name__ == '__main__':
    app.run(debug=True)