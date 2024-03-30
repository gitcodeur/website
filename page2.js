i = 14.23
m = 5.78

id = "bfr78"
mdp = "789"

function hello(){

    let baliseidt = document.getElementById("idt")
    let idt = baliseidt.value

    let balisepsrd = document.getElementById("psrd")
    let psrd = balisepsrd.value

    if(idt == id)
        i = 26.7

    if(psrd == mdp)
        m = 26.7

    if(i == m){
        console.log('good');
        window.open("main2.exe","_blank", null);
        location.reload()
    }
    else{
        alert("Tu t'es trompé.e")
    }
