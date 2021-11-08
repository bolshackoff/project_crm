<template>
  <div class="profile">
    <h1 class="name">Имя Фамилия</h1>
    <img class="profile_photo" src="../assets/logo.png">
  </div>
</template>

<script>
export default {
  name: "profile"
}
</script>

<style scoped>
.profile {
  position: absolute;
  width: 208px;
  height: 46px;
  left: 24px;
  top: 104px;
}

.profile_photo {
  position: absolute;
  width: 46px;
  height: 46px;
  left: 20px;
}

.name {
  font-size: large;
  font-family: 'Ebrima';
  position: absolute;
  width: 146px;
  height: 16px;
  left: 80px;
}
</style>
