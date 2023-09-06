function updateCurrentlyOpen(date : Date) {
    let currentlyOpenText = document.getElementById("currently-open-text");
    
    if (currentlyOpenText == null)
        return;
    
    currentlyOpenText.innerText = isCurrentlyOpen(date) ? "Just nu har vi öppet" : "Stängt just nu";
}

function isCurrentlyOpen(date: Date) : boolean {
    let day = date.getDay();
    let hour = date.getHours();

    let dayMonth : DayMonth = {
        month: date.getMonth(),
        dayOfTheMonth: date.getDate()
    }

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

function isClosedDay(dayMonth: DayMonth) : boolean {
    const closedDays : DayMonth[] = [
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
    ]

    return closedDays.includes(dayMonth);
}

function isWeekDay(day: number) {
    return day >= 1 && day <= 5;
}

function isSaturday(day: number) {
    return day == 6;
}

interface DayMonth {
    month: number,
    dayOfTheMonth: number
}

updateCurrentlyOpen(new Date());
