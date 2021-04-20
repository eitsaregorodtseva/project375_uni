<template>
  <div class="nav-bar">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <ul>
      <li class="menus"><i class="fa fa-times-circle"></i></li>


      <li class="logout"><router-link :to = "{ name:'home' }">ВЫЙТИ</router-link></li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'NavBar2',
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
    margin:0 2%;
    padding: 0;
    text-align: center;
    color: white;
  }
  .nav-bar ul li {
    display: inline-block;
    margin: 0 5px;
    padding: 20px;
    padding-left: 0px;
  }
  .home {
    float: left;
    padding: 300px;
  }
  .logout {
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
    background-color: red;
  }
   .notification {
     position: relative;
     padding: 15px 26px;
   }
   .notification .number {
     width: 25px;
     height: 25px;
     border-radius: 50%;
     position: absolute;
     top: -10px;
     right: -10px;
     padding: 3px 5px;
     background: red;
     color: white;
   }
  .menus {
font-size: 18px;
font-weight: bold;
    float: left;
}

</style>
