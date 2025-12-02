document.querySelectorAll('.open-google').forEach(btn => {
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        document.getElementById('modal-google').classList.add('show');
    });
});

document.getElementById('modal-google').addEventListener('click', function (e) {
    if (e.target === this) {
        this.classList.remove('show');
    }
});
