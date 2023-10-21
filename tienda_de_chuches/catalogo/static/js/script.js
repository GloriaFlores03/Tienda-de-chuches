function rotateImage(element) {
    element.classList.toggle('rotate');
}


let idleTimer;
    //const idleTime = 180000; // 2 minutos en milisegundos (120000)

    function resetTimer() {
        clearTimeout(idleTimer);
        idleTimer = setTimeout(logoutUser, idleTime);
    }

    function logoutUser() {
        alert('Se ha desconectado por inactividad.');
        window.location.href = "/catalogo/login/";
    }

    document.addEventListener('mousemove', resetTimer);
    document.addEventListener('keypress', resetTimer);
    
    resetTimer();