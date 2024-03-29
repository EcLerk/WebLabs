
function updateDateTime() {
    var now = new Date();

    var options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    };

    var formattedDateTime = now.toLocaleString('en-us', options); //в местном часовом поясе
    var targetElement = document.getElementById("time-display");

    if (targetElement) {
        targetElement.innerText = formattedDateTime;
    }
}

setInterval(updateDateTime, 1000); //обновление через 1 сек



// 2 прокрутка
const imageContainer = document.getElementById("imageContainer");
const animationTimeInput = document.getElementById("animationTime");

if (imageContainer) {
    const images = imageContainer.childNodes;
    images.forEach(image => {
        image.addEventListener("mouseover", function () {
            images.forEach(i => {
                if (i.style) {
                    i.style.animationPlayState = "paused";
                }
            });
        });
        image.addEventListener("mouseout", function () {
            images.forEach(i => {
                if (i.style) {
                    i.style.animationPlayState = "running";
                }
            });
        });
        image.addEventListener("click", function () {
            window.open("http://127.0.0.1:8000/");
        });
    });
}

//таймер для прокрутки
if (animationTimeInput) {
    animationTimeInput.addEventListener("input", function () {
        const animationTime = animationTimeInput.value + "s";
        document.documentElement.style.setProperty("--animation-time", animationTime);
    });
}


//3 scroll
const leftEffect = document.getElementById("left_effect");
const rightEffect = document.getElementById("right_effect");
const text = document.getElementById("text");
const moon = document.getElementById("moon");

if (leftEffect && rightEffect && text && moon) {
    window.addEventListener("scroll", function () {
        let value = window.scrollY;
        leftEffect.style.left = `-${value / 0.5}px`;
        rightEffect.style.left = `${value / 0.35}px`;
        text.style.bottom = `-${value}px`;
        moon.style.height = `${window.innerHeight - value}px`;
    });
}


//4
// document.addEventListener("DOMContentLoaded", function () {
//     const parallax = document.getElementById("parallax");
//     const walk = {x: 100, y: 50};
//
//     if (parallax) {
//         parallax.addEventListener("mousemove", function (e) {
//             const width = parallax.offsetWidth;
//             const height = parallax.offsetHeight;
//
//             let {offsetX: x, offsetY: y} = e;
//
//             const xWalk = Math.round((e.x / width / 2 * walk.x) - (walk.x / 2));
//             const yWalk = Math.round((e.y / height / 2  * walk.y) - (walk.y / 2));
//
//             parallax.style.transform = `rotateY(${-xWalk}deg) rotateX(${yWalk}deg)`;
//         });
//     }
// });

const body = document.querySelector("body"),
  article = document.querySelector("article"),
  walk = { x: 20, y: 15 },
  articleText = document.querySelector(".article__text");

function parallax(e) {
  const width = article.offsetWidth,
    height = article.offsetHeight;

  let { offsetX: x, offsetY: y } = e;

  const xWalk = Math.round((e.x / width / 2) * walk.x - walk.x / 2),
    yWalk = Math.round((e.y / height / 2) * walk.y - walk.y / 2);

  article.style.transform = `rotateY(${-xWalk}deg) rotateX(${yWalk}deg)`;
}

body.addEventListener("mousemove", parallax);

//5 шрифт текст
const fontSizeInput = document.getElementById("fontSize");
const textColorInput = document.getElementById("textColor");
const backgroundColorInput = document.getElementById("backgroundColor");

if (fontSizeInput) {
    fontSizeInput.addEventListener("input", function () {
        const fontSize = fontSizeInput.value + "px";
        document.body.style.fontSize = fontSize;
    });
}
if (textColorInput) {
    textColorInput.addEventListener("input", function () {
        const textColor = textColorInput.value;
        document.body.style.color = textColor;
    });
}
if (backgroundColorInput) {
    backgroundColorInput.addEventListener("input", function () {
        const backgroundColor = backgroundColorInput.value;
        document.body.style.backgroundColor = backgroundColor;
    });
}

// 7
const ageCalculator = document.getElementById("ageCalculator")
if (ageCalculator) {
  ageCalculator.addEventListener("submit", function (e) {
    e.preventDefault();

    const birthDateInput = document.getElementById("birthdate");
    const birthDate = new Date(birthDateInput.value);
    const currentDate = new Date();

    var age = currentDate.getFullYear() - birthDate.getFullYear();
    const monthDiff = currentDate.getMonth() - birthDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && currentDate.getDate() < birthDate.getDate())) {
      age--;
    }
    if (age < 0) {
      document.getElementById("ageResult").innerText = `Invalid data!`;
      return;
    } else {
      document.getElementById("ageResult").innerText = `Your age: ${age} y.o.`;
    }

    const daysOfWeek = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];
    const dayOfWeek = daysOfWeek[birthDate.getDay()];

    if (age < 18) {
        alert("You need your parents' permission to use this site!");
    } else {
        document.getElementById("dayOfWeek").textContent = `You were born on ${dayOfWeek}`;
        alert("Welcome to this site!");
    }
  });
}


// 8 обратный отсчет
document.addEventListener("DOMContentLoaded", function () {
    function startCountdown() {
        const currentTime = new Date().getTime();

        if (sessionStorage.getItem("countdownStartTime")) {
            const startTime = parseInt(sessionStorage.getItem("countdownStartTime"), 10);
            const elapsedTime = currentTime - startTime;
            const remainingTime = 60 * 60 * 1000 - elapsedTime;
            displayTime(remainingTime);
        } else {
            sessionStorage.setItem("countdownStartTime", currentTime.toString());
            displayTime(60 * 60 * 1000);
        }
    }
    function displayTime(remainingTime) {
        const element = document.getElementById("countdown");
        if (!element) {
            return;
        }

        if (remainingTime <= 0) {
            document.getElementById("countdown").innerText = "00:00 -_-";
            return;
        }

        const minutes = Math.floor(remainingTime / 60000);
        const seconds = Math.floor((remainingTime % 60000) / 1000);

        if (element) {
            if (seconds < 10) {
                element.innerText = `${minutes}:0${seconds}`;
            } else {
                element.innerText = `${minutes}:${seconds}`;
            }
        }

        if (remainingTime > 0) {
            setTimeout(() => displayTime(remainingTime - 1000), 1000);
        }
    }
    startCountdown();
});

// 9 таблица
const generateTableButton = document.getElementById("generateTable");
const transposeTableButton = document.getElementById("transposeTable");
const addRowButton = document.getElementById("addRow");
const addColumnButton = document.getElementById("addColumn");

if (generateTableButton) {
    generateTableButton.addEventListener("click", function () {
        const size = document.getElementById("tableSize").value;
        if (size <= 0 || size > 30) {
            return;
        }

        const table = document.getElementById("table");
        table.innerHTML = "";

        for (let i = 0; i < size; i++) {
            const row = document.createElement("tr");
            for (let j = 0; j < size; j++) {
                createCell(row);
            }
            table.appendChild(row);
        }
   });
}
if (transposeTableButton) {
    transposeTableButton.addEventListener("click", function () {
        const table = document.getElementById("table");
        if (table.innerHTML === "") {
            return;
        }

        const clonedTable = table.cloneNode(true);
        table.innerHTML = "";

        var rows = clonedTable.getElementsByTagName("tr");
        const rowsCount = rows[0].childElementCount;
        const columnsCount = rows.length;

        for (let i = 0; i < rowsCount; i++) {
            const row = document.createElement("tr");
            for (let j = 0; j < columnsCount; j++) {
                var columns = rows[j].getElementsByTagName("td");
                var cell = columns[i].cloneNode(true);
                cell.addEventListener("click", cellSelection);
                row.appendChild(cell);
            }
            table.appendChild(row);
        }
    });
}
if (addRowButton) {
    addRowButton.addEventListener("click", function () {
        const table = document.getElementById("table");

        var size = 0;
        if (table.innerHTML === "") {
             size = parseInt(tableSize.value);
        } else {
             size = table.getElementsByTagName("tr")[0].childElementCount;
        }

        const row = document.createElement("tr");
        for (let i = 0; i < size; i++) {
            const cell = document.createElement("td");
            cell.textContent = Math.floor(Math.random() * 100);
            cell.addEventListener("click", cellSelection);
            row.appendChild(cell);
        }
        table.appendChild(row);
    });
}
if (addColumnButton) {
    addColumnButton.addEventListener("click", function () {
        if (table.innerHTML === "") {
            const row = document.createElement("tr");
            createCell(row);
            table.appendChild(row);
            return;
        }

        var rows = table.getElementsByTagName("tr");
        for (let i = 0; i < rows.length; i++) {
            createCell(rows[i]);
        }
    });
}

function createCell(row) {
    const cell = document.createElement("td");
    cell.textContent = Math.floor(Math.random() * 100);
    cell.addEventListener("click", cellSelection);
    row.appendChild(cell);
}
function cellSelection(e) {
    var maxSelection = document.getElementById("maxSelection").value;
    if (maxSelection > 30) {
        maxSelection = 30;
    } else if (maxSelection < 0) {
        maxSelection = 0;
    }

    const cell = e.target;
    const row = cell.parentElement;
    const rowCells = Array.from(row.cells);
    const cellIndex = rowCells.indexOf(cell);

    const selectedInRow = rowCells.filter(c => c.classList.contains("selected"));
    const columnCells = Array.from(cell.parentElement.parentElement.rows);
    const selectedInColumn = columnCells
        .map(r => r.cells[cellIndex])
        .filter(c => c.classList.contains("selected"));

    if (cell.classList.contains("selected")) {
        cell.classList.remove("selected");
    } else if (
        selectedInRow.length < maxSelection &&
        selectedInColumn.length < maxSelection &&
        !hasNeighborSelected(rowCells, cellIndex)
    ) {
        cell.classList.add("selected");
    }
}
function hasNeighborSelected(cells, i) {
    if (i > 0 && cells[i - 1].classList.contains("selected")) {
        return true;
    }
    if (i < cells.length - 1 && cells[i + 1].classList.contains("selected")) {
        return true;
    }
    return false;
}


// // 10
// const classFunctionActivator = document.getElementById("classFunctionActivator");
// if (classFunctionActivator) {
//     classFunctionActivator.addEventListener("click", function (e) {
//         e.preventDefault();
//         console.clear();
//
//         functionalInheritance();
//     });
// }
// function functionalInheritance() {
//     function withTimestamp(fn) {
//       return function() {
//         const timestamp = new Date().toLocaleString();
//         const result = fn.apply(this, arguments);
//         return `${timestamp}: ${result}`;
//       };
//     }
//
//     function Exercise(name, type) {
//         this.name = name;
//         this.type = type;
//     }
//     Exercise.prototype.getName = function() {
//         return this.name;
//     };
//     Exercise.prototype.setName = function(name) {
//         this.name = name;
//     };
//     Exercise.prototype.getType = function() {
//         return this.type;
//     };
//     Exercise.prototype.setType = function(type) {
//         this.type = type;
//     };
//     Exercise.prototype.getDetails = withTimestamp(function() {
//         return `Name: ${this.name}, Type: ${this.type}`;
//     });
//
//     function Acrobatic(name, type, coach) {
//         Exercise.call(this, name, type);
//         this.coach = coach;
//
//         this.getCoach = function () {
//             return this.coach;
//         }
//         this.setCoach = function (coach) {
//             this.coach = coach;
//         }
//     }
//     Acrobatic.prototype = Object.create(Exercise.prototype);
//     Acrobatic.prototype.bark = function() {
//         return `${this.name} barks!`;
//     };
//     Acrobatic.prototype.getDetails = function() {
//         const exerciseDetails = Exercise.prototype.getDetails.call(this);
//         return `${exerciseDetails}, Coach: ${this.getCoach()}`;
//     };
//
//     const myExercise = new Exercise("Jumping", "Group");
//     const myAcrobatic = new Acrobatic("Pilates", "Individual", "Edward Kallen");
//
//     console.log(myAcrobatic.getName());
//     myAcrobatic.setName("Pilates");
//     console.log(myAcrobatic.getName());
//     console.log(myExercise.getDetails());
//     console.log(myAcrobatic.getDetails());
//     console.log(myAcrobatic.bark());
// }


// 11.2
const searchButton = document.getElementById("searchButton");
if (searchButton) {
    const carsData = [
        new Map([ ["make", "Toyota"], ["number", "ABC123"], ["owner", "Shallow"] ]),
        new Map([ ["make", "Honda"], ["number", "XYZ789"], ["owner", "Rubin"] ]),
        new Map([ ["make", "Toyota"], ["number", "DEF456"], ["owner", "Sword"] ]),
        new Map([ ["make", "Nissan"], ["number", "A2KHG2"], ["owner", "Casper"] ])
    ];

    carsData.forEach(car =>
           console.log(`Make: ${car.get("make")}, Owner: ${car.get("owner")}, Number: ${car.get("number")}`));

    searchButton.addEventListener("click", function (e) {
        e.preventDefault();

        const carMake = document.getElementById("carMake").value;
        const resultsDiv = document.getElementById("resultsDiv");
        resultsDiv.innerHTML = "";

        const matchingCars = carsData.filter(car => car.get("make").toLowerCase() === carMake.toLowerCase());
        if (matchingCars.length === 0) {
            resultsDiv.innerHTML = "This make of car was not found.";
        } else {
            const resultList = document.createElement("ul");
            matchingCars.forEach(car => {
                const listItem = document.createElement("li");
                    listItem.textContent = `Owner: ${car.get("owner")}, Number: ${car.get("number")}`;
                    resultList.appendChild(listItem);
                });
            resultsDiv.appendChild(resultList);
        }
    });
}
