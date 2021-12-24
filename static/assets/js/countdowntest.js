

const times = [
  [7, 0, "red"], [9, 0, "yellow"]
]

console.log(times)

const timer = document.getElementById('time');
const mass_time = document.getElementById('mass_time');


  setInterval(function tick() {
     const now = new Date();
     const nextShip = times.find(it => it[0] > now.getHours() || it[0] == now.getHours() &&  it[1] >= now.getMinutes()) || times[0];

    let hours = nextShip[0] - now.getHours();
    let minutes = nextShip[1] - now.getMinutes();

    let mass_hours = nextShip[0];
    let mass_minutes = nextShip[1];

    if(minutes < 0) { minutes += 60; hours -= 1 }
    if(hours < 0) { hours += 24; }

    const seconds = 60 - now.getSeconds();

    if (mass_hours >= 12) {
      var timing = "PM";
    } else {
      var timing = "AM";
    }

    if (mass_minutes == 0) {
      var minz = "00";
    } else {
      var minz = mass_minutes
    }

    timer.innerHTML = `${hours}:${minutes}:${seconds}`;
    timer.style.color = nextShip[2];

    mass_time.innerHTML = `${mass_hours}:${minz} ${timing}`;

  }, 1000);