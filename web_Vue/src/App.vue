<template>
  <div id="app">
    <side_bar/>
  </div>
</template>

<script>
import Side_bar from "./components/side_bar";
export default {
  name: 'App',
  components: {Side_bar}
}
</script>

<style>

#app {
  font-family: 'Ebrima' , sans-serif;
}
body  {
  background: #fcfcfc;}
</style>
