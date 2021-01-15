<template>
  <body class="session-registration">
  <NavBar></NavBar>
  <div class="application-main">
    <main id="">
      <div class="registr-form px-3" id="login">
        <div class="registr-form-header p-0">
          <h1>Регистрация</h1>
        </div>
        <div class="registr-form-body mt-3">
          <form>
            <label for="login_field" class="registr-form-label">
              Логин
            </label>
            <input v-model="login" type="text" id="login_field" class="form-control input-block" autofocus="autofocus"/>

            <label for="first_name" class="registr-form-label">
              Имя
            </label>
            <input v-model="first_name" type="text" id="first_name" class="form-control input-block" autofocus="autofocus"/>

            <label for="last_name" class="registr-form-label">
              Фамилия
            </label>
            <input v-model="last_name" type="text" id="last_name" class="form-control input-block" autofocus="autofocus"/>

            <label for="email" class="registr-form-label">
              E-mail
            </label>
            <input v-model="email" type="text" id="email" class="form-control input-block" autofocus="autofocus"/>

            <label for="password" class="registr-form-label">
              Пароль
            </label>
            <input v-model="password" type="password" id="password" class="form-control input-block" autofocus="autofocus"/>

            <label for="password_confirmation" class="registr-form-label">
              Подтверждение пароля
            </label>
            <input v-model="password_confirmation" type="password" id="password_confirmation" class="form-control input-block" autofocus="autofocus"/>

            <input type="submit" name="commit" value="Создать аккаунт" class="btn btn-block btn-primary" @click="registrUser">
          </form>
        </div>
    </div>
      </main>
    </div>
  </body>
</template>

<script>
import axios from 'axios';
import NavBar from '../components/Navbar'
export default {
    name: "Registration",
    components: {
            NavBar
        },
    data() {
        return {
            login: this.login,
            first_name: this.first_name,
            last_name: this.last_name,
            email: this.email,
            password: this.password,
        }
    },
        methods: {
            goCabinet() {
                this.$router.push({name: "cabinet"})
            },
            registrUser: function () {
                axios({
                        method: 'POST',
                        url: 'http://localhost:8000',
                        params: {
                            login: this.login,
                            first_name: this.first_name,
                            last_name: this.last_name,
                            email: this.email,
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
        }
    }
</script>

<style scoped>
.session-registration {
  background-color: #fff;
  color: #24292e;
  padding: 15px 20px;
  text-align: center;
  border-radius: 5px;
  margin-bottom: 15px;
  text-shadow: none;
  border: 0;
}
.application-main {
  margin-top: 80px;
}
.registr-form {
  width: 340px;
  margin: 0 auto;
}
.registr-form-header {
  margin-bottom: 15px;
  color: #24292e;
  text-align: center;
  text-shadow: none;
  background-color: initial;
  border: 0;
}
.registr-form-body {
  border: 1px solid;
  color-border-secondary: #eaecef;
  border: #eaecef;
  border-radius: 5px;
  padding: 20px;
  font-size: 14px;
  background-color: #f6f8fa;
  margin-top: 5px;
  margin-bottom: 15px;
}
.registr-form-label {
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
  font-family: inherit;
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
