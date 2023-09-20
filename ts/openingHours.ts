// Define opening and closing times for weekdays and Saturday
const weekdayOpeningTime: number = 10;
const weekdayClosingTime: number = 16;
const saturdayOpeningTime: number = 12;
const saturdayClosingTime: number = 15;

// Function to update the "currently open" status based on the current date
function updateCurrentlyOpen(date: Date): void {
  let currentlyOpenText: HTMLElement | null = document.getElementById("currently-open-text");

  // If the element doesn't exist, return
  if (currentlyOpenText == null) return;

  let text: string = "";

  // Check if the business is currently open
  if (isCurrentlyOpen(date)) {
    text = 'Just&nbsp;nu:&nbsp;<span class="text-success">Öppet</span>';
  } else if (!isClosedDay(date) && !hasOpened(date)) {
    // Check if today is not closed and the business hasn't opened yet
    text = ` <span>Vi öppnar klockan ${getOpeningTime(date.getDay())} idag </span>`;
  } else {
    // set the time of day used to check if open
    // all open days are open at 13:XX
    date.setHours(13);
    let iterations: number = 0;
    do {
      date.setDate(date.getDate() + 1);
      iterations += 1;
    } while (!isCurrentlyOpen(date));

    let day: number = date.getDay();

    if (iterations == 1) {
      text = `Vi öppnar klockan ${getOpeningTime(day)} imorgon`;
    } else {
      text = `Vi öppnar klockan ${getOpeningTime(day)} på ${getDayName(day)}`;
    }
  }

  currentlyOpenText.innerHTML = text;
}

// Function to check if the business is currently open
function isCurrentlyOpen(date: Date): boolean {
  let day: number = date.getDay();
  let hour: number = date.getHours();

  if (isClosedDay(date)) return false;

  let openingTime: number = getOpeningTime(day);
  let closingTime: number = getClosingTime(day);

  return hour >= openingTime && hour < closingTime;
}

// Function to check if the business has opened for the day
function hasOpened(date: Date): boolean {
  let day: number = date.getDay();
  let hour: number = date.getHours();

  if (isClosedDay(date)) {
    return false;
  } else if (isSunday(date.getDay())) {
    return true;
  }

  if (isWeekday(day)) {
    return hour >= weekdayOpeningTime;
  } else if (isSaturday(day)) {
    return hour >= saturdayOpeningTime;
  } else {
    return false;
  }
}


// Function to check if the day is a closed day (holidays, etc.)
function isClosedDay(date: Date): boolean {
  const closedDays: { month: number; dayOfTheMonth: number }[] = [
  {
    month: 0,
    dayOfTheMonth: 1,
  },
  {
    month: 0,
    dayOfTheMonth: 6,
  },
  {
    month: 4,
    dayOfTheMonth: 1,
  },
  {
    month: 5,
    dayOfTheMonth: 6,
  },
  {
    month: 11,
    dayOfTheMonth: 24,
  },
  {
    month: 11,
    dayOfTheMonth: 25,
  },
  {
    month: 11,
    dayOfTheMonth: 26,
  },
  {
    month: 11,
    dayOfTheMonth: 31,
  },
];

  let dayMonth: { month: number; dayOfTheMonth: number } = {
    month: date.getMonth(),
    dayOfTheMonth: date.getDate(),
  };

  for (let i: number = 0; i < closedDays.length; i++) {
    if (
      closedDays[i].month == dayMonth.month &&
      closedDays[i].dayOfTheMonth == dayMonth.dayOfTheMonth
    )
      return true;
  }
  return false;
}

// Function to get the opening time for a given day
function getOpeningTime(day: number): number {
  if (isWeekday(day)) return weekdayOpeningTime;
  if (isSaturday(day)) return saturdayOpeningTime;
  return -1; // No opening time defined for this day
}

// Function to get the closing time for a given day
function getClosingTime(day: number): number {
  if (isWeekday(day)) return weekdayClosingTime;
  if (isSaturday(day)) return saturdayClosingTime;
  return -1; // No closing time defined for this day
}

// Function to check if a day is a weekday
function isWeekday(day: number): boolean {
  return day >= 1 && day <= 5;
}

// Function to check if a day is a Saturday
function isSaturday(day: number): boolean {
  return day == 6;
}

// Function to check if a day is a Sunday
function isSunday(day: number): boolean {
  return day == 0;
}

// Function to get the name of the day based on the day number
function getDayName(day: number): string {
  switch (day) {
    case 0:
      return "söndag";
    case 1:
      return "måndag";
    case 2:
      return "tisdag";
    case 3:
      return "onsdag";
    case 4:
      return "torsdag";
    case 5:
      return "fredag";
    case 6:
      return "lördag";
    default:
      return "";
  }
}

// Update the "currently open" status every 5 seconds
window.setInterval(() => updateCurrentlyOpen(new Date()), 5000);

// Initially update the "currently open" status
updateCurrentlyOpen(new Date());

