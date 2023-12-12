const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalLabel = document.getElementById('exampleModalLabel')
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=>addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const questions = modalBtn.getAttribute('data-questions')
    const time = modalBtn.getAttribute('data-time')
    const pass = modalBtn.getAttribute('data-pass')

    modalLabel.innerHTML = `Тест ${name}`
    modalBody.innerHTML = `
        <p><h2>Инструкция</h2></p>
        С помощью этого теста оценивается Ваш навык работы в WebTutor.<br>
        Тест состоит из ряда вопросов.<br>
        Ваша задача - выбрать все правильные ответы на вопрос.<br>
        <br>
        Во время работы с тестом, пожалуйста, помните о следующем.<br>
        Тест состоит из ${questions} заданий<br>
        На выполнение теста у Вас будет ${time} минут<br>
        Вам необходимо работать максимально быстро и точно.<br>
        Убедитесь, что Вас ничего не будет отвлекать.<br>
        Если Вы затрудняетесь с ответом, выберите наиболее верный, с Вашей точки зрения, вариант, но избегайте беспорядочного угадывания.<br>
        Если Вы прервете выполнение теста, обратно к нему вернуться будет невозможно.<br>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))