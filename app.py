import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, request, jsonify, render_template
from scipy.linalg import lu

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    slider_value = int(data['sliderValue'])

    # Generar una matriz aleatoria
    matriz = np.random.randint(-9, 9, size=(slider_value, slider_value))

    # Redondear los elementos de la matriz a dos decimales
    matriz_redondeada = np.round(matriz, decimals=2)

    # Realizar la factorización LU
    P, L, U = lu(matriz)

    # Generar la imagen de la matriz
    imagen_matriz = generar_imagen_matriz(matriz_redondeada)
    imagen_P=generar_imagen_matriz(P)
    imagen_L=generar_imagen_matriz(L)
    imagen_U=generar_imagen_matriz(U)

    P = np.round(P, decimals=2)
    L = np.round(L, decimals=2)
    U = np.round(U, decimals=2)


    # Preparar los resultados para enviarlos de vuelta a la página web
    resultados = {
        'matriz': matriz_redondeada.tolist(),
        'P': P.tolist(),
        'L': L.tolist(),
        'U': U.tolist(),
        'imagen_matriz': imagen_matriz,
        "imagen_P": imagen_P,
        "imagen_L": imagen_L,
        "imagen_U": imagen_U
    }

    return jsonify(resultados)

def generar_imagen_matriz(matriz):
    plt.figure(figsize=(6, 6))
    plt.imshow(matriz, cmap='coolwarm', interpolation='nearest')
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            plt.text(j, i, "{:.2f}".format(matriz[i, j]), ha='center', va='center', color='black',fontsize=12)
    plt.axis('off')  # Desactivar ejes
    plt.tight_layout()

    # Convertir la imagen a base64
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    return f'data:image/png;base64,{img_str}'

if __name__ == '__main__':
    app.run(debug=True)
