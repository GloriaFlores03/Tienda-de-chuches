function rotateImage(element) {
    element.classList.toggle('rotate');
}


let idleTimer;
    const idleTime = 120000;

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