from flask import Flask, render_template, jsonify, abort
import pandas as pd

app = Flask(__name__)

def cargar_productos():
    df = pd.read_csv('productos.csv')
    df.insert(0, 'id', range(1, len(df) + 1))  
    return df.to_dict(orient='records')

@app.route('/')
def home():
    productos = cargar_productos()
    return render_template('productos.html', productos=productos)

@app.route('/productos')
def api_productos():
    return jsonify(cargar_productos())

@app.route('/productos/<int:producto_id>')
def detalle_producto(producto_id):
    productos = cargar_productos()
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if not producto:
        abort(404)
    return render_template('detalles.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)