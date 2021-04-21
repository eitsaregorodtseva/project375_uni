<template>
  <body class="session-information">
  <NavBar2></NavBar2>
    <div id="sidebar-menu" class="sidebar-menu">
    <ul id="menu" class="menu">
      <li><a href="#">Мой профиль</a></li>
      <div>
          <li class="item-toggle">
            <a href="#" class="submenu">Тесты на память</a>
          <ul>
            <li><a href="#">Общий тест на память</a></li>
            <li><a href="#">Тест на долговременную память</a></li>
            <li><a href="#">Тест на оперативную память</a></li>
          </ul>
          </li>
      </div>
          <li><a href="#" class="submenu">Тесты на внимание</a></li>
          <li><a href="#" class="submenu">Тесты на утомляемость</a></li>
          <li><a href="#" class="submenu">Тесты на депрессию</a></li>

          <li><a href="#">Тренажеры памяти</a></li>
          <li><a href="#">Тренажеры внимания</a></li>
          <li><a href="#">Статистика</a></li>
          <li><a href="#">Telegram бот</a></li>
    </ul>
  </div>
  <div class="container-statistics">
  <div class="main-header">
    <h1>Статистика</h1>
    <br>
    <br>
    <hr>
    <br>
    <br>
  </div>
  <div class="statistics">
  <div class="graphs">
    <div class="header"><h1>Статистика по месяцам</h1></div>
    <LineChart></LineChart>
  </div>
  <div class="graphs">
    <div class="header"><h1>Статистика прохождения</h1></div>
    <BarChart></BarChart>
  </div>
  <div class="test_memory">
    <div class="header"><h1>Тест на оперативную память 1</h1></div>
    <BarTests></BarTests>
  </div>
  <div class="test_memory">
    <div class="header"><h1>Тест на оперативную память 2</h1></div>
    <BarTests></BarTests>
  </div>
  </div>
  </div>
  <div class="footer"></div>
</body>
</template>

<script>
import NavBar2 from './Navbar2'
import LineChart from './Graphs/LineChart.js'
import BarChart from './Graphs/PieChart.js'
import BarTests from './Graphs/BarTests.js'
export default {
  components: {
    LineChart,
    BarChart,
    BarTests,
    NavBar2
  }
}
</script>

<style>
 .session-information {
  background-color: #fff;
  color: #24292e;
  text-align: center;
  border-radius: 5px;
  margin-bottom: 15px;
  text-shadow: none;
  border: 0;
}
.main-header {
  font-family: 'Quicksand', sans-serif;
  font-size: 20px;
  padding-top: 50px;
}
.container-statistics {
  padding: 50px;
  width: 80%;
  height: 1000px;
  float: left;
}
.sidebar-menu {
  float: left;
  background-color: #2f3033;
  text-align: left;
  color: #2f3033;
  height: 1500px;
}
.sidebar-menu ul {
  list-style: none;
	background-color: #2f3033;
	width: 260px;
  border-bottom: none;
	color: #fff;
  margin: 0px;
  padding: 0px;
}
.sidebar-menu ul li {
	position: relative;
}
.sidebar-menu u li:hover {
	background-color: #2ea44f;
}
.sidebar-menu ul li:hover ul {
	display: block;
}
.sidebar-men ul li:hover ul li ul {
	display: none;
}
.sidebar-menu ul li a {
	color: #fff;
	padding: 10px 20px;
	display: block;
	text-decoration: none;
	font-weight: bold;
  font-family: 'Quicksand', sans-serif;
  font-size: 16px;
}
.sidebar-menu ul li a:hover {
	background-color: #2ea44f;
	color: #fff;
}
.sidebar-men ul li ul li:hover ul {
	display: block;
}
.sidebar-menu ul li ul {
	position: absolute;
	left: 30px;
	top: 0px;
	display: none;
  margin: 0;
  padding: 0;
}
.sidebar-menu li a {
  font-family: 'Quicksand', sans-serif;
  font-size: 20px;
  text-align: left;
  padding-left: 100px;
}
.submenu {
  display: none;
}
.open-list > ul {
  display: none;
  list-style: none;
}
.open-list:hover > ul {
    display: block;
}
form {
  display: block;
  margin-top: 0em;
}
p {
  margin-top: 0;
  margin-bottom: 10px;
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}
body {
  margin: 0;
  display: block;
  font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;
  font-size: 14px;
  line-height: 1.5;
  color: #24292e;
  background-color: #fff;
}
* {
  box-sizing: border-box;
}
div {
  display: block;
}
label {
  font-weight: 600;
  cursor: default;
}
.statistics {
  float: left;
  display: inline-block;
}
.graphs {
  width: 50%;
  padding: 0px 50px 100px 50px;
  margin-inside: 15px;
  float: left;
}
.test_memory{
  width: 100%;
  padding: 50px 50px 50px 40px;
  align-content: center;
}
</style>
