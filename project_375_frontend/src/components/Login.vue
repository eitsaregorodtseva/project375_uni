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
          <form>
            <label for="login_field" class="auth-form-label">
              Логин
            </label>
            <input v-model="login" type="text" id="login_field" class="form-control input-block" autofocus="autofocus"/>
            <label for="password" class="auth-form-label">
              Пароль
              <router-link :to="{name: 'passwordreset'}" class="label-link">Забыли пароль?</router-link>
            </label>
            <input v-model="password" type="password" id="password" class="form-control input-block" autofocus="autofocus"/>
            <input type="submit" name="commit" value="Войти" class="btn btn-block btn-primary" @click="loginUser">
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
import axios from 'axios';
import NavBar from '../components/Navbar'
export default {
    name: "Login",
    components: {
            NavBar
        },
    data() {
        return {
            login: this.login,
            password: this.password,
        }
    },
        methods: {
            goCabinet() {
                this.$router.push({name: "cabinet"})
            },
            loginUser: function () {
                axios({
                        method: 'POST',
                        url: 'http://localhost:8000/accounts/login/',
                        params: {
                            login: this.login,
                            password: this.password
                        },

                        headers: {
                            'Content-Type': 'application/json'
                        },
                        xhrFields: {
                            withCredentials: true
                        }
                }
                )
                    .then(response => {
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
            },
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
.label-link {
  float: right;
  font-size: 12px;
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
