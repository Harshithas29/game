<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>Tap The Box Game</title>



<style>

body {

&nbsp; text-align: center;

&nbsp; font-family: Arial, sans-serif;

&nbsp; background: #f2f2f2;

}



h1 {

&nbsp; margin-top: 20px;

}



\#gameArea {

&nbsp; width: 400px;

&nbsp; height: 400px;

&nbsp; margin: 20px auto;

&nbsp; position: relative;

&nbsp; background: white;

&nbsp; border: 3px solid black;

&nbsp; border-radius: 10px;

}



\#box {

&nbsp; width: 50px;

&nbsp; height: 50px;

&nbsp; background: red;

&nbsp; position: absolute;

&nbsp; display: none;

&nbsp; cursor: pointer;

&nbsp; border-radius: 8px;

}



button {

&nbsp; padding: 10px 20px;

&nbsp; font-size: 16px;

&nbsp; cursor: pointer;

}

</style>

</head>



<body>



<h1>Tap The Box!</h1>

<p>Time: <span id="time">30</span> seconds</p>

<p>Score: <span id="score">0</span></p>

<button id="startBtn">Start Game</button>



<div id="gameArea">

&nbsp; <div id="box"></div>

</div>



<script>

const box = document.getElementById("box");

const startBtn = document.getElementById("startBtn");

const scoreDisplay = document.getElementById("score");

const timeDisplay = document.getElementById("time");

const gameArea = document.getElementById("gameArea");



let score = 0;

let timeLeft = 30;

let moveInterval;

let timerInterval;



function moveBox() {

&nbsp; const maxX = gameArea.clientWidth - box.clientWidth;

&nbsp; const maxY = gameArea.clientHeight - box.clientHeight;



&nbsp; const randomX = Math.floor(Math.random() \* maxX);

&nbsp; const randomY = Math.floor(Math.random() \* maxY);



&nbsp; box.style.left = randomX + "px";

&nbsp; box.style.top = randomY + "px";

}



box.addEventListener("click", () => {

&nbsp; score++;

&nbsp; scoreDisplay.textContent = score;

&nbsp; moveBox();

});



startBtn.addEventListener("click", () => {

&nbsp; score = 0;

&nbsp; timeLeft = 30;

&nbsp; scoreDisplay.textContent = score;

&nbsp; timeDisplay.textContent = timeLeft;



&nbsp; box.style.display = "block";

&nbsp; moveBox();



&nbsp; moveInterval = setInterval(moveBox, 800);



&nbsp; timerInterval = setInterval(() => {

&nbsp;   timeLeft--;

&nbsp;   timeDisplay.textContent = timeLeft;



&nbsp;   if (timeLeft <= 0) {

&nbsp;     clearInterval(moveInterval);

&nbsp;     clearInterval(timerInterval);

&nbsp;     box.style.display = "none";

&nbsp;     alert("Game Over! Your score: " + score);

&nbsp;   }

&nbsp; }, 1000);

});

</script>



</body>

</html>

















