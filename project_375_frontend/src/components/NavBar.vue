<template>
  <div class="nav-bar">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <ul>
      <li class="home"><router-link :to = "{ name:'home' }" exact><i class="fa fa-home"></i> ГЛАВНАЯ</router-link></li>
      <li class="entry"><router-link :to = "{ name:'login' }">ВОЙТИ</router-link></li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'NavBar',
  }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand);
  .nav-bar {
    background-color: #2f3033;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    overflow: hidden;
  }
  .nav-bar ul {
    list-style: none;
    margin:0 5%;
    padding: 0;
    text-align: center;
    color: white;
  }
  .nav-bar ul li {
    display: inline-block;
    margin: 0 5px;
    padding: 25px;
  }
  .home {
    float: left;
  }
  .entry {
    float: right;
  }
  .nav-bar:after {
    content: '';
    display: block;
    clear: both;
  }
  .nav-bar ul li a {
    text-decoration: none;
    font-family: 'Quicksand', sans-serif;
    font-size: 16px;
    font-weight: bold;
    color: white;
    padding: 10px;
    border-radius: 5px;
  }
  .nav-bar ul li a:hover {
    background-color: #2ea44f;
  }
  .router-link-active {
    background-color: #2ea44f;
  }
</style>
