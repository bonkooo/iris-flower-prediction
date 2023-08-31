const clrbtn = document.querySelector(".clear-button");
const petalLengthInput = document.querySelector("#petal-length");
const petalWidthInput = document.querySelector("#petal-width");
const sepalLengthInput = document.querySelector("#sepal-length");
const sepalWidthInput = document.querySelector("#sepal-width");

clrbtn.addEventListener("click", function () {
    petalLengthInput.value = '';
    petalWidthInput.value = '';
    sepalLengthInput.value = '';
    sepalWidthInput.value = '';
});