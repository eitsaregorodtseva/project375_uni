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
  <div class="container-profile">
  <div class="header">
    <div class="info-form-header p-0">
      <h1>Мой профиль</h1>
      <br>
      <br>
      <hr>
      <br>
      <br>
    </div>
  </div>
  <div class="child info-form" id="profile">
    <div class="info-form-body mt-3">
    <form>
    <label for="first_name_field" class="info-form-label">Имя</label>
    <input v-model="first_name" type="text" id="first_name_field" class="form-control input-block" autofocus="autofocus"/>
    <label for="second_name_field" class="info-form-label">Фамилия</label>
    <input v-model="second_name" type="text" id="second_name_field" class="form-control input-block" autofocus="autofocus"/>
    <label for="login_field" class="info-form-label">Логин</label>
    <input v-model="login" type="text" id="login_field" class="form-control input-block" autofocus="autofocus"/>
    <label for="email_field" class="info-form-label">Электронная почта</label>
    <input v-model="email" type="text" id="email_field" class="form-control input-block" autofocus="autofocus"/>
    <label for="birth_date_field" class="info-form-label">Дата рождения</label>
    <input v-model="birth_date" type="date" id="birth_date_field" class="form-control input-block" autofocus="autofocus"/>
    </form>
    </div>
    <img src="@/assets/man.png" height="200px">
  </div>
  </div>
  <div class="footer"></div>
</body>

</template>

<script>
import NavBar2 from '../components/Navbar2'
export default {
  name: 'Cabinet',
  components: {
    NavBar2
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<style scoped>
.session-information {
  font-family: 'Quicksand', sans-serif;
  font-size: 20px;
  background-color: #fff;
  color: #24292e;
  text-align: center;
  border-radius: 5px;
  margin-bottom: 15px;
  text-shadow: none;
  border: 0;
}
.header {
  margin: 0;
  padding-top: 0;
}
.container-profile {
  padding: 50px;
  width: 70%;
  height: 1000px;
  float: left;
}
.sidebar-menu {
  float: left;
  background-color: #2f3033;
  text-align: left;
  color: #2f3033;
  height: 1000px;
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
.child {
  display: inline-block;
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
.info-form {
  width: 900px;
  margin: 0 auto;
  padding-left: 0px;
  padding-top: 50px;
}
.info-form-header {
  margin-top: 15px;
  margin-bottom: 30px;
  color: #24292e;
  text-align: center;
  text-shadow: none;
  background-color: initial;
  border: 0;
  height: 100px;
}
.info-form-body {
  width: 650px;
  margin-left: 10px;
  padding: 5px;
  font-size: 14px;
  margin-bottom: 15px;
  float: left;
}
.info-form-label {
  display: block;
  margin-bottom: 7px;
  text-align: left;
}
.input-block {
  margin-top: 5px;
  margin-bottom: 15px;
  display: block;
  width: 50%;
}
.avatar {
  margin-left: 10px;
  padding: 10px;
  margin-top: 5px;
  margin-bottom: 15px;
}
.form-control {
  padding: 5px 12px;
  font-size: 14px;
  line-height: 20px;
  color: #24292e;
  vertical-align: middle;
  background-color: #fff;
  background-repeat: no-repeat;
  background-position: right 8px center;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  outline: none;
  box-shadow: inset 0 1px rgba(225,228,232,0.2);
}
.mt-3 {
  margin-top: 16px!important;
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
input {
  overflow: visible;
  font: inherit;
  margin: 0;
  -webkit-writing-mode: horizontal-tb !important;
  text-rendering: auto;
  letter-spacing: normal;
  word-spacing: normal;
  text-transform: none;
  text-indent: 0px;
  text-shadow: none;
  -webkit-rtl-ordering: logical;
  cursor: text;
  border-width: 2px;
  border-style: inset;
  border-color: rgb(118, 118, 118) rgb(133, 133, 133);
  border-image: initial;
}
.p-0 {
  padding: 0!important;
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
</style>

