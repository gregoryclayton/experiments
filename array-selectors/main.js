
const wordBank = ["books","booking","bangers","words"]
const imageBank = ["image path","image path","image path","image path"]
const imageBank2 = ["image path","image path","image path"]
const colorBank = ["#000444","#222220","#ffffff","#000546","#450796","#576949"]


function yes() {

    const myImage = document.getElementById("myImage");
    myImage.setAttribute("src", imageBank[Math.floor(Math.random()*imageBank.length)]);
}

function no() {

    const myImage = document.getElementById("myImage");
    myImage.setAttribute("src", imageBank2[Math.floor(Math.random()*imageBank2.length)]);
}

function wording() {

    const wordSelector = document.getElementById("words");
    let newWordSelector = wordBank[Math.floor(Math.random()*wordBank.length)]
    
    wordSelector.innerHTML = newWordSelector;
}

function coloring() {

    const colorSelector = document.getElementById("color");
    colorSelector.style.backgroundColor = colorBank[Math.floor(Math.random()*colorBank.length)];
}