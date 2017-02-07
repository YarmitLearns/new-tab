var d = new Date();
function setDate(d=d, diff=0){
    display1 = document.getElementById('now_date_name');
    var d_name_opt = {weekday: 'long'}
    display1.innerHTML = d.toLocaleDateString('en-US', d_name_opt);

    display2 = document.getElementById('now_date');
    isoDate = d.toISOString();
    cropped_isoDate = isoDate.slice(0,10)
    display2.innerHTML = cropped_isoDate;

    severDate = document.getElementById('selectedDate');
    serverDate.value = cropped_isoDate;
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

// var d = new Date();
// function setDate(date=d){

//     curDateName = document.getElementById('now_date_name');
//     var d_name_opt = {weekday: 'long'}
//     curDateName.innerHTML = d.toLocaleDateString('en-US', d_name_opt);

//     curDate = document.getElementById('now_date');
//     isoDate = d.toISOString();
//     cropped_isoDate = isoDate.slice(0,10)
//     curDate.innerHTML = cropped_isoDate;

//     selectedDate = document.getElementById('selectedDate');
//     selectedDate.value = cropped_isoDate;
    
// }

// function addDaysToDate(date, days){
//     var result = new Date(date);
//     result.setDate(result.getDate() + days);
//     var dd = result.getDate();
//     var mm = result.getMonth() + 1; // January starts at 0.
//     var yyyy = result.getFullYear();

//     if (dd < 10){
//         dd = '0' + dd
//     }
//     if (mm < 10){
//         mm = '0' + mm
//     }

//     var d = new Date(yyyy, mm, dd);
//     console.log("hi")
//     setDate();
// }

// setDate();
// previousDate = document.getElementById('previousDate');
// previousDate.addEventListener('click', addDaysToDate(d, -1), false)


// var d_opt = {year: 'numeric', month: 'numeric', day:'numeric'}

// dateDisplay = document.getElementById('dateDisplay');
// dateDisplay.innerHTML = d.toDateString();
