var d = new Date();
function setDate(d=d, diff=0){
    display1 = document.getElementById('now_date');
    display1.innerHTML = d
}
function increaseDate(d=d, diff=1){
    console.log('i')
    d.setDate(d.getDate() + diff);
    setDate(d);
}
function decreaseDate(d=d, diff=1){
    console.log(d)
    d.setDate(d.getDate() - diff);
    setDate(d);
}
setDate(d);

decreaseButton = document.getElementById('previousDate');
decreaseButton.addEventListener('click', function(){decreaseDate(d,1)}, false);

increaseButton = document.getElementById('nextDate');
increaseButton.addEventListener('click', function(){increaseDate(d,1)}, false);


console.log("helllo");