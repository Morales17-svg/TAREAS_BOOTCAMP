// Seleccionamos los controles deslizantes y los elementos del texto
const inputRojo = document.getElementById("rojo");
const inputVerde = document.getElementById("verde");
const inputAzul = document.getElementById("azul");

const textoRojo = document.getElementById("texto-rojo");
const textoVerde = document.getElementById("texto-verde");
const textoAzul = document.getElementById("texto-azul");

// Valores iniciales
let rojo = inputRojo.value;
let verde = inputVerde.value;
let azul = inputAzul.value;

// Muestra los valores iniciales en los elementos <p>
textoRojo.textContent = rojo;
textoVerde.textContent = verde;
textoAzul.textContent = azul;

// Función para actualizar el fondo de pantalla
function actualizarColor(rojo, verde, azul) {
    // Cambia el color del fondo del body usando los valores RGB
    document.body.style.backgroundColor = `rgb(${rojo}, ${verde}, ${azul})`;
}

// Agrega un event listener para el input de Rojo.
inputRojo.addEventListener('input', (e) => {
    // Actualiza el valor de la variable y el texto.
    rojo = e.target.value;
    textoRojo.textContent = rojo;
  
    // Llama a la función para actualizar el color de fondo.
    actualizarColor(rojo, verde, azul);
});

// Agrega un event listener para el input de Verde.
inputVerde.addEventListener('input', (e) => {
    // Actualiza el valor de la variable y el texto.
    verde = e.target.value;
    textoVerde.textContent = verde;
  
    // Llama a la función para actualizar el color de fondo.
    actualizarColor(rojo, verde, azul);
});

// Agrega un event listener para el input de Azul.
inputAzul.addEventListener('input', (e) => {
    // Actualiza el valor de la variable y el texto.
    azul = e.target.value;
    textoAzul.textContent = azul;
  
    // Llama a la función para actualizar el color de fondo.
    actualizarColor(rojo, verde, azul);
});

// Inicializa el color de fondo al cargar la página
actualizarColor(rojo, verde, azul);
