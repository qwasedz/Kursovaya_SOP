document.getElementById('logoutLink').addEventListener('click', function(event) {
    event.preventDefault(); // Отменить стандартное действие ссылки (переход по URL)

    // Открыть модальное окно подтверждения
    $('#confirmModal').modal('show');
});


document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.custom-menu-button');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const section = this.dataset.section;
            const sections = document.querySelectorAll('.section');
            sections.forEach(section => {
                section.style.display = 'none';
            });
            document.getElementById(section + '-section').style.display = 'block';
        });
    });
});



function downloadFile(event) {
    event.preventDefault();  // Отменяем стандартное поведение перехода по ссылке

    // Получаем URL файла
    var fileUrl = event.target.href;

    // Создаем ссылку на скачивание файла
    var link = document.createElement('a');
    link.href = fileUrl;
    link.download = '';  // Устанавливаем атрибут download для указания на скачивание файла

    // Добавляем ссылку на страницу и эмулируем клик по ней
    document.body.appendChild(link);
    link.click();

    // Удаляем ссылку из DOM
    document.body.removeChild(link);
}

function updateFileName(input) {
    const fileNameSpan = input.parentElement.querySelector('span');
    if (input.files.length > 0) {
        fileNameSpan.textContent = input.files[0].name;
    } else {
        fileNameSpan.textContent = '';
    }
}


document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.custom-menu-button');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const section = this.dataset.section;
            const sections = document.querySelectorAll('.section');
            sections.forEach(section => {
                section.style.display = 'none';
            });
            document.getElementById(section + '-section').style.display = 'block';
        });
    });
});
document.getElementById('logoutLink').addEventListener('click', function(event) {
    event.preventDefault(); // Отменить стандартное действие ссылки (переход по URL)

    // Открыть модальное окно подтверждения
    $('#confirmModal').modal('show');
});
