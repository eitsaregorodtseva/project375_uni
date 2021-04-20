<template>
  <body class="session-authentication">
  <NavBar></NavBar>
  <div class="application-main">
    <main id="">
      <div class="auth-form px-3" id="login">
        <div class="auth-form-header p-0">
          <h1>Вход</h1>
        </div>
        <div class="auth-form-body mt-3">
          <h2 v-if="wrongCred">Wrong credentials entered!. Please enter your correct details.</h2>
          <form @submit.prevent="loginUser">
            <label for="login_field" class="auth-form-label">
              Логин
            </label>
            <input required v-model="login" type="text" id="login_field" class="form-control input-block" autofocus="autofocus"/>
            <label for="password" class="auth-form-label">
              Пароль
            </label>
            <input required v-model="password" type="password" id="password" class="form-control input-block" autofocus="autofocus"/>
            <button type="submit" class="btn btn-block btn-primary">Войти</button>
            <div class="social">
              <a href="#" class="vk btn">
                <i class="fa fa-vk fa-fw"></i>
              </a>

              <a href="#" class="fb btn">
                <i class="fa fa-facebook fa-fw"></i>
              </a>
              <a href="#" class="google btn">
                <i class="fa fa-google fa-fw"></i>
              </a>
            </div>
          </form>
        </div>
        <p class="login-callout mt-3">
        Нет аккаунта?
        <router-link :to="{name: 'registration'}">Зарегистрироваться.</router-link>
      </p>
    </div>
      </main>
    </div>
  </body>
</template>

<script>
import NavBar from '../components/Navbar'
export default {
  name: 'Login',
  components: {
    NavBar
  },
  data () {
        return {
            login: '',
            password: '',
            wrongCred: false
        }
    },
    methods: {
        goCabinet () {
            this.$router.push({name: 'cabinet'})
        },
        loginUser () {
            this.$store.dispatch('loginUser', {
                login: this.login,
                password: this.password
            })
            .then(() => {
              this.wrongCred = false
              this.$router.push({ name: 'cabinet' })
            })
          .catch(err => {
            console.log(err)
            this.wrongCred = true // if the credentials were wrong set wrongCred to true
          })
        }

    }
}
</script>

<style scoped>
.session-authentication {
  background-color: #fff;
  color: #24292e;
  padding: 15px 20px;
  text-align: center;
  #border: 1px solid #d8dee2;
  border-radius: 5px;
  margin-bottom: 15px;
  text-shadow: none;
  border: 0;
}
.application-main {
  margin-top: 80px;
}
.auth-form {
  width: 340px;
  margin: 0 auto;
}
.auth-form-header {
  margin-bottom: 15px;
  color: #24292e;
  text-align: center;
  text-shadow: none;
  background-color: initial;
  border: 0;
}
.auth-form-body {
  border: 1px solid;
  border: #eaecef;
  border-radius: 5px;
  padding: 20px;
  font-size: 14px;
  background-color: #f6f8fa;
  margin-top: 5px;
  margin-bottom: 15px;
}
.auth-form-label {
  display: block;
  margin-bottom: 7px;
  text-align: left;
}
.input-block {
  margin-top: 5px;
  margin-bottom: 15px;
  display: block;
  width: 100%;
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
.login-callout {
  padding: 15px 20px;
  text-align: center;
  border: 1px solid #d8dee2;
  border-radius: 5px;
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
.btn-primary {
  color: #fff;
  background-color: #2ea44f;
  border-color: rgba(27, 31, 35, 0.15);
  box-shadow: inset 0 1px 0 hsla(0, 0%, 100%, 0.03);
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
.px-3 {
  padding-right: 16px!important;
  padding-left: 16px!important;
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
.vk {
  background-color: #3B5998;
  color: white;
}
.fb {
  background-color: #3B5998;
  color: white;
}
.google {
  background-color: #dd4b39;
  color: white;
}
</style>
