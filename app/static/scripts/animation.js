document.getElementById("btn-girar").addEventListener("click", () =>{
    let ruleta = document.getElementById("ruleta");
    let imgGanador = document.getElementById("imagen-Ganador");
    let tituloGanador = document.getElementById("titulo-Ganador");

    imgGanador.style.display = "none";
    tituloGanador.innerText = "";


    let grados = Math.floor(Math.random() * 5000 + 3000);
    ruleta.style.transform = `rotate(${grados}deg)`;

    fetch('/ruleta', {method: "POST"})
    .then(res => res.json())
    .then(data => {

        setTimeout(() => {
            imgGanador.src = data.ganador;
            imgGanador.style.display = "block";
            tituloGanador.innerText = "premio ganador"

        }, 4000);
    })
    .catch(err => console.error(err));


});