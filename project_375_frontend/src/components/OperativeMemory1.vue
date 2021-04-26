<template>
<body class="session-user">
  <NavBar2></NavBar2>
  <div class="header">

    <div id="sidebar-menu" class="sidebar-menu">
    <ul id="menu" class="menu">
      <li><router-link :to = "{ name:'mypage' }">Мой профиль</router-link></li>
      <div>
          <li class="item-toggle">
            <a href="#" class="submenu" @click="showSubmenu">Тесты на память</a>
          <ul>
            <li><a href="#">Общий тест на память</a></li>
            <li><a href="#">Тест на долговременную память</a></li>
            <li><router-link :to = "{ name:'operativememory1' }">Тест на оперативную память 1</router-link></li>
            <li><router-link :to = "{ name:'operativememory2' }">Тест на оперативную память 2</router-link></li>
          </ul>
          </li>
      </div>
          <li><a href="#" class="submenu">Тесты на внимание</a></li>
          <li><a href="#" class="submenu">Тесты на утомляемость</a></li>
          <li><a href="#" class="submenu">Тесты на депрессию</a></li>

          <li><a href="#">Тренажеры памяти</a></li>
          <li><a href="#">Тренажеры внимания</a></li>
          <li><router-link :to = "{ name:'statistics' }">Статистика</router-link></li>
          <li><a href="https://t.me/miem375_bot">Telegram бот</a></li>
    </ul>
  </div>

  </div>

  <div class="container-tests">
    <div class="test_1">
      <h1>Тесты > Тесты на память > Тест на оперативную память 1</h1>
      <br>
      <br>
      <hr>
      <br>
      <br>
      <div id="condition">
      <p>В течение 5 секунд медленно прочтите появившиеся числа, постарайтесь их запомнить.
        После их исчезновения Ваша задача - в уме сложить первое число со вторым, полученную
        сумму записать; второе число сложить с третьим, сумму записать; третье число сложить
        с четвертым, четвертое с пятым, снова записать сумму...
        <br>Например, если появились числа 12345, то ответ должен быть 3579.
        <br>Время для вычислений - 15 секунд.</p>
      <br>
      <br>
      <button id="start-button" value="Начать" class="btn btn-block btn-primary" @click="start_1">Начать</button>
    </div>
    <div id="components" class="comp_1">
        <ul>
          <ul>
          <li id="num1">{{ number1 }}</li>
          <li id="num2">{{ number2 }}</li>
          <li id="num3">{{ number3 }}</li>
          </ul>
        </ul>
      </div>
      <div id="entry_place" class="ep_1">
        <input required v-model.number="input_1" type="number" name="place">
        <button id="check-button" class="btn btn-block btn-primary" @click="check_1">Отправить</button>
      </div>
      <button id="correct_1" class="btn btn-1 btn-primary">Верно!</button>
      <button id="uncorrect_1" class="btn btn-1 btn-primary_2">Неверно!</button>
    </div>
    <div class="test_2">
      <h1>Тесты > Тесты на память > Тест на оперативную память 2</h1>
      <br>
      <br>
      <hr>
      <br>
      <br>
      <div id="condition_2">
      <p>В течение 30 секунд запомните 12 чисел, а затем в течение 1 минуты введите их в соответствующие поля. Пройдите тест 4 раза.</p>
      <br>
      <br>
      <button id="start-button_2" value="Начать" class="btn btn-block btn-primary" @click="start_2">Начать</button>
    </div>
    <div id="components_2" class="comp_2">
        <ul>
          <ul>
          <li id="num1_2">{{ number1_2 }}</li>
          <li id="num2_2">{{ number2_2 }}</li>
          <li id="num3_2">{{ number3_2 }}</li>
          <li id="num4_2">{{ number4_2 }}</li>
</ul>
          <ul>
          <li id="num5_2">{{ number5_2 }}</li>
          <li id="num6_2">{{ number6_2 }}</li>
          <li id="num7_2">{{ number7_2 }}</li>
          <li id="num8_2">{{ number8_2 }}</li>
          </ul>
          <ul>
          <li id="num9_2">{{ number9_2 }}</li>
          <li id="num10_2">{{ number10_2 }}</li>
          <li id="num11_2">{{ number11_2 }}</li>
          <li id="num12_2">{{ number12_2 }}</li>
          </ul>
        </ul>
      </div>
      <div id="entry_place_2" class="ep_2">
        <ul>
          <ul>
        <li><input required v-model.number="input_1_2" type="number" name="place"></li>
        <li><input required v-model.number="input_2_2" type="number" name="place"></li>
        <li><input required v-model.number="input_3_2" type="number" name="place"></li>
        <li><input required v-model.number="input_4_2" type="number" name="place"></li>
          </ul>
          <ul>
        <li><input required v-model.number="input_5_2" type="number" name="place"></li>
        <li><input required v-model.number="input_6_2" type="number" name="place"></li>
        <li><input required v-model.number="input_7_2" type="number" name="place"></li>
        <li><input required v-model.number="input_8_2" type="number" name="place"></li>
          </ul>
          <ul>
        <li><input required v-model.number="input_9_2" type="number" name="place"></li>
        <li><input required v-model.number="input_10_2" type="number" name="place"></li>
        <li><input required v-model.number="input_11_2" type="number" name="place"></li>
        <li><input required v-model.number="input_12_2" type="number" name="place"></li>
          </ul>
        </ul>
        <button id="check-button_2" class="btn btn-block btn-primary" @click="check_2">Отправить</button>
      </div>
      <button id="correct_2" class="btn btn-1 btn-primary">Верно!</button>
      <button id="uncorrect_2" class="btn btn-1 btn-primary_2">Неверно!</button>
    </div>
  </div>

  <div class="footer"></div>
</body>

</template>

<script>
import $ from 'jquery'
import NavBar2 from '../components/Navbar2'
export default {
  name: 'OperativeMemory1',
  components: {
    NavBar2
  },
  data () {
    return {
      number1: 2,
      number2: 3,
      number3: 2,
      number1_2: 1,
      number2_2: 2,
      number3_2: 3,
      number4_2: 4,
      number5_2: 5,
      number6_2: 6,
      number7_2: 12,
      number8_2: 16,
      number9_2: 17,
      number10_2: 10,
      number11_2: 11,
      number12_2: 12
    }
  },
  methods: {
    showSubmenu () {
      if ($(this).hasClass('active')) {
        $(this).next().slideUp('easeOutExpo')
        $(this).removeClass('active')
      } else {
        $(this).next('#submenu')
        $(this).addClass('active')
        $(this).next().slideDown('easeOutExpo')
      }
    },
    start_1 () {
      $('#components').show()
      $('#components').delay(5000).fadeOut(0)
      $('#start-button').delay(5000).fadeOut(0)
      $('#entry_place').delay(5000).fadeIn(0)
      $('#entry_place').delay(15000).fadeOut(0)
    },
    start_2 () {
      $('#components_2').show()
      $('#components_2').delay(30000).fadeOut(0)
      $('#start-button_2').delay(30000).fadeOut(0)
      $('#entry_place_2').delay(30000).fadeIn(0)
      $('#entry_place_2').delay(60000).fadeOut(0)
    },
    check_1 () {
      $('#entry_place').hide()
      let result = parseInt(String(this.number1 + this.number2) + String(this.number2 + this.number3))
      if (result === parseInt(this.input_1)) {
        $('#correct_1').show()
      } else {
        $('#uncorrect_1').show()
      }
    },
    check_2 () {
      $('#entry_place_2').hide()
      if (parseInt(this.number1_2) === parseInt(this.input_1_2) && parseInt(this.number2_2) === parseInt(this.input_2_2) &&
      parseInt(this.number3_2) === parseInt(this.input_3_2) && parseInt(this.number4_2) === parseInt(this.input_4_2) &&
      parseInt(this.number5_2) === parseInt(this.input_5_2) && parseInt(this.number6_2) === parseInt(this.input_6_2) &&
      parseInt(this.number7_2) === parseInt(this.input_7_2) && parseInt(this.number8_2) === parseInt(this.input_8_2) &&
      parseInt(this.number9_2) === parseInt(this.input_9_2) && parseInt(this.number10_2) === parseInt(this.input_10_2) &&
      parseInt(this.number11_2) === parseInt(this.input_11_2) && parseInt(this.number12_2) === parseInt(this.input_12_2))  {
        $('#correct_2').show()
      } else {
        $('#uncorrect_2').show()
      }
    }
  }
}
</script>

<style scoped>
.session-user {
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
  padding: 0;
}
.sidebar-menu {
  float: left;
  background-color: #2f3033;
  text-align: left;
  color: #2f3033;
height: 1000px;
}
.container-tests {
  padding: 50px;
  width: 70%;
  height: 1000px;
  float: left;
}
.sidebar-tests ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 300px;
  background-color: #f1f1f1;
}
.sidebar-tests li a {
  display: block;
  color: #000;
  padding: 15px 0 8px 16px;
  text-decoration: none;
  text-align: center;
  font-family: 'Quicksand', sans-serif;
  font-size: 16px;
}
.sidebar-tests li a:hover {
  background-color: #2ea44f;
  color: white;
}
.sidebar-tests li .p12 {
  background-color: #2ea44f;
  color: white;
}
.active {
  background-color: #4CAF50;
  color: white;
}
.btn {
  margin-top: 20px;
  transition: .2s cubic-bezier(.3,0,.5,1);
  transition-property: color,background-color,border-color;
  position: relative;
  display: inline-block;
  padding: 5px 16px;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border: 1px solid;
  border-radius: 6px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}
.btn-block {
  display: block;
  width: 100%;
  text-align: center;
}
.btn-1 {
  display: block;
  width: 100%;
  text-align: center;
}
.btn-primary {
  color: #fff;
  background-color: #2ea44f;
  border-color: rgba(27, 31, 35, 0.15);
  box-shadow: inset 0 1px 0 hsla(0, 0%, 100%, 0.03);
}
.btn-primary_2 {
  color: #fff;
  background-color: #f44336;
  border-color: rgba(27, 31, 35, 0.15);
  box-shadow: inset 0 1px 0 hsla(0, 0%, 100%, 0.03);
}
.extremum-slide {
	border:1px solid;
	padding:50px;
	display:none;
}
.comp_1 ul {
  text-align: center;
  list-style: none;
}
.comp_1 ul li {
  display: inline-block;
  background-color: #3B5998;
  width: 20%;
  text-align: center;
  color: white;
}
.comp_2 ul {
  text-align: center;
  list-style: none;
}
.comp_2 ul li {
  display: inline-block;
  background-color: #3B5998;
  width: 20%;
  text-align: center;
  color: white;
}
.comp_2 ul li input{
  width: 1px;
}
.ep_1 {
  text-align: center;
  padding: 50px;
}
.ep_2 ul{
  text-align: center;
  list-style: none;
}
.ep_2 ul li {
  display: inline-block;
  width: 20%;
  text-align: center;
  color: white;
}
#components {
  display: none;
}
#entry_place {
  display: none;
}
#correct_1 {
  display: none;
}
#uncorrect_1 {
  display: none;
}
#components_2 {
  display: none;
}
#entry_place_2 {
  display: none;
}
#correct_2 {
  display: none;
}
#uncorrect_2 {
  display: none;
}
.sidebar-menu ul{
	list-style: none;
	background-color: #2f3033;
	width: 280px;
  border-bottom: none;
	color: #fff;
  margin: 0;
  padding: 0;
}
.sidebar-menu ul li{
	position: relative;
}
.sidebar-menu u li:hover{
	background-color: #2ea44f;
}
.sidebar-menu ul li:hover ul{
	display: block;
}
.sidebar-men ul li:hover ul li ul{
	display: none;
}
.sidebar-menu ul li a{
	color: #fff;
	padding: 10px 20px;
	display: block;
	text-decoration: none;
	font-weight: bold;
  font-family: 'Quicksand', sans-serif;
  font-size: 16px;
}
.sidebar-menu ul li a:hover{
	background-color: #2ea44f;
	color: #fff;
}
.sidebar-menu ul li ul li:hover ul{
	display: block;
}
.sidebar-menu ul li ul{
	position: absolute;
	left: 280px;
	top: 0px;
	display: none;
  margin: 0;
  padding: 0;
}
  .container-tests {
    font-family: 'Quicksand', sans-serif;
    font-size: 20px;
    text-align: left;
    padding-left: 100px;
  }
.sidebar-menu li a{
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
.test_2{
  display: none;
}
.session-user {
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
  padding: 0;
}
.sidebar-menu {
  float: left;
  background-color: #2f3033;
  text-align: left;
  color: #2f3033;
height: 1000px;
}
.container-tests {
  padding: 50px;
  width: 70%;
  height: 1000px;
  float: left;
}
.sidebar-tests ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 300px;
  background-color: #f1f1f1;
}
.sidebar-tests li a {
  display: block;
  color: #000;
  padding: 15px 0 8px 16px;
  text-decoration: none;
  text-align: center;
  font-family: 'Quicksand', sans-serif;
  font-size: 16px;
}
.sidebar-tests li a:hover {
  background-color: #2ea44f;
  color: white;
}
.sidebar-tests li .p12 {
  background-color: #2ea44f;
  color: white;
}
.active {
  background-color: #4CAF50;
  color: white;
}
.btn {
  margin-top: 20px;
  transition: .2s cubic-bezier(.3,0,.5,1);
  transition-property: color,background-color,border-color;
  position: relative;
  display: inline-block;
  padding: 5px 16px;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border: 1px solid;
  border-radius: 6px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}
.btn-block {
  display: block;
  width: 100%;
  text-align: center;
}
.btn-1 {
  display: block;
  width: 100%;
  text-align: center;
}
.btn-primary {
  color: #fff;
  background-color: #2ea44f;
  border-color: rgba(27, 31, 35, 0.15);
  box-shadow: inset 0 1px 0 hsla(0, 0%, 100%, 0.03);
}
.btn-primary_2 {
  color: #fff;
  background-color: #f44336;
  border-color: rgba(27, 31, 35, 0.15);
  box-shadow: inset 0 1px 0 hsla(0, 0%, 100%, 0.03);
}
.extremum-slide {
	border:1px solid;
	padding:50px;
	display:none;
}
.comp_1 ul {
  text-align: center;
  list-style: none;
}
.comp_1 ul li {
  display: inline-block;
  background-color: #3B5998;
  width: 20%;
  text-align: center;
  color: white;
}
.comp_2 ul {
  text-align: center;
  list-style: none;
}
.comp_2 ul li {
  display: inline-block;
  background-color: #3B5998;
  width: 20%;
  text-align: center;
  color: white;
}
.comp_2 ul li input{
  width: 1px;
}
.ep_1 {
  text-align: center;
  padding: 50px;
}
.ep_2 ul{
  text-align: center;
  list-style: none;
}
.ep_2 ul li {
  display: inline-block;
  width: 20%;
  text-align: center;
  color: white;
}
#components {
  display: none;
}
#entry_place {
  display: none;
}
#correct_1 {
  display: none;
}
#uncorrect_1 {
  display: none;
}
#components_2 {
  display: none;
}
#entry_place_2 {
  display: none;
}
#correct_2 {
  display: none;
}
#uncorrect_2 {
  display: none;
}
.sidebar-menu ul{
	list-style: none;
	background-color: #2f3033;
	width: 280px;
  border-bottom: none;
	color: #fff;
  margin: 0;
  padding: 0;
}
.sidebar-menu ul li{
	position: relative;
}
.sidebar-menu u li:hover{
	background-color: #2ea44f;
}
.sidebar-menu ul li:hover ul{
	display: block;
}
.sidebar-men ul li:hover ul li ul{
	display: none;
}
.sidebar-menu ul li a{
	color: #fff;
	padding: 10px 20px;
	display: block;
	text-decoration: none;
	font-weight: bold;
  font-family: 'Quicksand', sans-serif;
  font-size: 16px;
}
.sidebar-menu ul li a:hover{
	background-color: #2ea44f;
	color: #fff;
}
.sidebar-menu ul li ul li:hover ul{
	display: block;
}
.sidebar-menu ul li ul{
	position: absolute;
	left: 280px;
	top: 0px;
	display: none;
  margin: 0;
  padding: 0;
}
  .container-tests {
    font-family: 'Quicksand', sans-serif;
    font-size: 20px;
    text-align: left;
    padding-left: 100px;
  }
.sidebar-menu li a{
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
</style>
