<template>
    <div class="home">
      <NavBar></NavBar>
      <div class="body">
      </div>
    </div>
</template>

<script>
    import NavBar from '../components/Navbar'
    export default {
        name: "Home",
        components: {
            NavBar
        },
        methods: {
            goCabinet() {
                this.$router.push({name: "cabinet"})
            },
        },
    }
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand) ;
  .home {
    margin: 0;
    padding: 0;
  }
  .body {
    background-color: white;
    text-align: center;
    color: white;
    font-family: 'Quicksand', sans-serif;
    padding: 0;
    margin: 78px 0;
  }
</style>
