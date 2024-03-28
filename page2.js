
i = 0
m = 0

id = "123"
mdp = "789"

function hello(){
    let baliseidt = document.getElementById("idt")
    let idt = baliseidt.value

    let balisepsrd = document.getElementById("psrd")
    let psrd = balisepsrd.value

    if(idt == id)
        i = 1
        console.log(i)

    if(psrd == mdp)
        m = 1
        console.log(m)

    if(i == m)
        console.log('good')
        window.open("main2.py","_blank", null);
}



