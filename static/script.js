const slider = document.getElementById('slider');
const sliderValue = document.getElementById('slider-value');

slider.addEventListener('input', function() {
    sliderValue.textContent = this.value;
});

document.querySelector('button').addEventListener('click', function() {
    var sliderValue = document.getElementById('slider').value;

    // Enviar el valor del slider a Python
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/calcular', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var resultados = JSON.parse(xhr.responseText);
            // Actualizar las matrices en la página con los resultados
            document.querySelector('.imagen-container').style.display = 'flex';
            document.querySelector('.image-container').style.display = 'flex';
            
            // Mostrar la imagen de la matriz en la página
            document.getElementById('imagen_matriz').src = resultados.imagen_matriz;
            document.getElementById('imagen_P').src = resultados.imagen_P;
            document.getElementById('imagen_L').src = resultados.imagen_L;
            document.getElementById('imagen_U').src = resultados.imagen_U;
        }
    };
    xhr.send(JSON.stringify({sliderValue: sliderValue}));
});

function actualizarMatriz(elementoId, matriz) {
    var container = document.getElementById(elementoId);
    container.innerHTML = ''; // Limpiar el contenido previo

    // Crear elementos de tabla para mostrar la matriz
    var tabla = document.createElement('table');
    matriz.forEach(function(fila) {
        var filaElemento = document.createElement('tr');
        fila.forEach(function(valor) {
            var celda = document.createElement('td');
            celda.textContent = valor;
            filaElemento.appendChild(celda);
        });
        tabla.appendChild(filaElemento);
    });
    container.appendChild(tabla);
}


