



const studyBtn = document.getElementById("study-btn");
const breakBtn = document.getElementById("break-btn");


let timer;
let startTime;
let remainingTime = 1500; // 25min em segundos
let isPaused = false;
let isRunning = false;
let ciclos = 0;


let currentMode = "study"; // começa no estudo


function updateActiveMode(mode) {
  if (mode === "study") {
    studyBtn.classList.add("active");
    breakBtn.classList.remove("active");
  } else if (mode === "break") {
    breakBtn.classList.add("active");
    studyBtn.classList.remove("active");
  }
}


function startTimer() {
  updateActiveMode(currentMode);
  // resto do timer...
}


// quando acabar o ciclo, troca o modo:
function switchMode() {
  if (currentMode === "study") {
    currentMode = "break"; // vai para descanso
  } else {
    currentMode = "study"; // volta para estudo
  }
  startTimer();
}


updateActiveMode(currentMode); // currentMode = "study" ou "break"


const timerDisplay = document.getElementById("timer");
  const mainBtn = document.getElementById("main-btn");










  function updateDisplay() {
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;
    timerDisplay.textContent =
      `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
  }


  function toggleTimer() {
    if (!isRunning) {
      startStudy();
      mainBtn.textContent = "⏸️";
      isRunning = true;
      isPaused = false;
    } else if (!isPaused) {
      pauseTimer();
      mainBtn.textContent = "▶️";
    } else {
      resumeTimer();
      mainBtn.textContent = "⏸️";
    }
  }


function startStudy() {
  currentMode = "study"; // garante que está no modo estudo
  updateActiveMode(currentMode); // 🔹 atualiza o botão ativo


  if (!startTime) {
    startTime = new Date();
    document.getElementById("inicio").value = startTime.toTimeString().slice(0, 8);
  }
  remainingTime = 1500;
  clearInterval(timer);
  isPaused = false;
  timer = setInterval(() => {
    if (!isPaused && remainingTime > 0) {
      remainingTime--;
      updateDisplay();
      if (remainingTime === 0) {
        alert("Tempo de estudo finalizado! Escolha seu descanso.");
        ciclos++;
        document.getElementById("ciclos").value = ciclos;
        document.getElementById("fim").value = new Date().toTimeString().slice(0, 8);
        mainBtn.textContent = "▶️"; // volta pro play
        isRunning = false;
      }
    }
  }, 1000);
}


function startBreak(minutes) {
  currentMode = "break"; // garante que está no modo descanso
  updateActiveMode(currentMode); // 🔹 atualiza o botão ativo


  remainingTime = minutes * 60;
  clearInterval(timer);
  isPaused = false;
  isRunning = true;
  mainBtn.textContent = "⏸️";
  timer = setInterval(() => {
    if (!isPaused && remainingTime > 0) {
      remainingTime--;
      updateDisplay();
      if (remainingTime === 0) {
        alert("Descanso finalizado! Pode iniciar o próximo ciclo de estudo.");
        mainBtn.textContent = "▶️";
        isRunning = false;
      }
    }
  }, 1000);
}




  function pauseTimer() {
    isPaused = true;
  }


  function resumeTimer() {
    isPaused = false;
  }


  function resetTimer() {
    clearInterval(timer);
    remainingTime = 1500;
    updateDisplay();
    isRunning = false;
    isPaused = false;
    mainBtn.textContent = "▶️";
    startTime = null;
  }




  updateDisplay();


  document.querySelector('form').addEventListener('submit', function (e) {
    const fim = document.getElementById("fim").value;
    const inicio = document.getElementById("inicio").value;
    const ciclosVal = ciclos;


    document.getElementById("inicio").value = inicio;
    document.getElementById("fim").value = fim;
    document.getElementById("ciclos").value = ciclosVal;
  });


 




