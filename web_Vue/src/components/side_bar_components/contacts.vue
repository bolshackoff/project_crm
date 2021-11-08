<template>
  <div class="contacts">
    <img class="img_tabs" src="../assets/contacts.png">
    <p class="p_tabs">Contacts</p>
  </div>
</template>

<script>
export default {
  name: "contacts"
}
</script>

<style scoped>
.img_tabs {
  position: absolute;
  width: 20px;
  height: 20px;
  left: 24px;
  top: 20%;
}

.p_tabs {
  position: absolute;
  left: 56px;
  font-size: 13px;
  letter-spacing: 0.01em;
  top: -12%;
  color: #334D6E;
}

.contacts {
  position: absolute;
  width: 208px;
  height: 30px;
  left: 24px;
  top: 251px;
}
</style>
