window.addEventListener('click', function (event) {

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");

/*btn1.addEventListener("click", function(){
    if (event.target.closest('.counter_wrapper').isVisible) {
         btn1.hide();
    }
});*/


    let counter;
    // Проверка клика строго по кнопкам Плис или Минус
    if (event.target.dataset.action === 'plus' || event.target.dataset.action === 'minus') {
        // Находим обертку счетчика
        const counterWrapper = event.target.closest('.counter_wrapper');
        // Находим див с числом счетчика
        counter = counterWrapper.querySelector('[data-counter]');
    }
    // Проверяем элемент является ли он Плюс
    if (event.target.dataset.action === 'plus') {
        counter.innerText = ++counter.innerText;
    }
    // Проверяем элемент является ли он Минус
    if (event.target.dataset.action === 'minus') {
        if (parseInt(counter.innerText) > 1){
            counter.innerText = --counter.innerText;
        }
    }
});