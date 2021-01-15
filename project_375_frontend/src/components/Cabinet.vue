<template>
<body class="session-user">
  <NavBar></NavBar>
  <div class="header">
    <div class="header-user"></div>
    <div class="header-diagram"></div>
    <div class="header-bot"></div>
  </div>
  <div class="sidebar-tests"></div>
  <div class="container-tests"></div>
  <div class="sidebar-diagram"></div>
  <div class="footer"></div>
</body>

</template>

<script>
    import NavBar from '../components/Navbar'
    export default {
        name: "Cabinet",
        components: {
            NavBar
        },
    }
</script>

<style scoped>
.session-user {
  background-color: #fff;
  color: #24292e;
  padding: 15px 20px;
  text-align: center;
  border-radius: 5px;
  margin-bottom: 15px;
  text-shadow: none;
  border: 0;
}
.header-user {
  width: 20%;
  background: red;
  height: 300px;
  float: left;
}
.header-diagram {
  width: 60%;
  height: 300px;
  float: left;
  background: #2c3e50;
}
.header-bot {
  width: 20%;
  background: red;
  height: 300px;
  float: right;
}
.sidebar-tests {
  width: 20%;
  height: 300px;
  background: #2ea44f;
  float: left;
}
.container-tests {
  width: 60%;
  height: 1000px;
  background: blueviolet;
  float: left;
}
.sidebar-diagram {
  width: 20%;
  height: 300px;
  background: #2ea44f;
  float: right;
}
</style>
