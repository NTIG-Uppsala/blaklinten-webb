function updateCurrentlyOpen(date) {
    let currentlyOpenText = document.getElementById("currently-open-text");
    if (currentlyOpenText == null)
        return;
    currentlyOpenText.innerText = isCurrentlyOpen(date) ? "Just nu har vi öppet" : "Stängt just nu";
}
function isCurrentlyOpen(date) {
    let day = date.getDay();
    let hour = date.getHours();
    let dayMonth = {
        month: date.getMonth(),
        dayOfTheMonth: date.getDate()
    };
    if (isClosedDay(dayMonth))
        return false;
    if (isWeekDay(day)) {
        return hour >= 10 && hour < 16;
    }
    else if (isSaturday(day)) {
        return hour >= 12 && hour < 15;
    }
    else {
        return false;
    }
}
function isClosedDay(dayMonth) {
    const closedDays = [
        {
            month: 0,
            dayOfTheMonth: 1
        },
        {
            month: 0,
            dayOfTheMonth: 6
        },
        {
            month: 4,
            dayOfTheMonth: 1
        },
        {
            month: 5,
            dayOfTheMonth: 6
        },
        {
            month: 11,
            dayOfTheMonth: 24
        },
        {
            month: 11,
            dayOfTheMonth: 25
        },
        {
            month: 11,
            dayOfTheMonth: 26
        },
        {
            month: 11,
            dayOfTheMonth: 31
        }
    ];
    return closedDays.includes(dayMonth);
}
function isWeekDay(day) {
    return day >= 1 && day <= 5;
}
function isSaturday(day) {
    return day == 6;
}
updateCurrentlyOpen(new Date());
