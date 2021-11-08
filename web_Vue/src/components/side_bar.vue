<template>
  <div id="side_bar" class="side_bar">

      <h1 class="title">CRM</h1>
      <hr class="line" style="width: 256px;
  height: 1px;
  left: 0px;
  top: 60px;">
      <div class="tabs">
        <profile class="MouseOver"/>
        <dashboard class="MouseOver"/>
        <tasks class="MouseOver"/>
        <contacts class="MouseOver"/>
        <deals class="MouseOver"/>
        <settings class="MouseOver"/>
      </div>
      <hr class="line" style="width: 256px;
  height: 1px;
  left: 0px;
  top: 300px;">

  </div>


</template>

<script>

import Tasks from "./side_bar_components/tasks";
export default {
  components: {Task_statuses, Settings, Deals, Contacts, Tasks, Dashboard, Profile},
  data() {
    return {}
  },
  methods: {},
}

import Dashboard from "./side_bar_components/dashboard";
import Profile from "./side_bar_components/profile";
import Contacts from "./side_bar_components/contacts";
import Deals from "./side_bar_components/deals";
import Settings from "./side_bar_components/settings";
import Task_statuses from "./side_bar_components/task_statuses";

</script>

<style scoped>
.test {position: absolute;
  top:35%;
  left: 350px;}
.btn {
  position: absolute;
  top:40%;
  left: 350px;
}
.MouseOver:hover {
  border-radius: 4%;
  background: #e3ecf3;
}

.side_bar {
  position: absolute;
  width: 256px;
  height: 98%;
  left: 8px;
  /*filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));*/
  box-shadow: 4px 4px 12px #8f8f8f;
}

.title {
  position: absolute;
  width: 69px;
  height: 26px;
  left: 24px;
  top: -12px;
  font-family:"Ebrima";
  font-style: normal;
  font-weight: 600;
  font-size: 48px;
  line-height: 25px;
  /* Accent blue */

  color: #6794b0;

}

.tabs {
 position: absolute;
  right: 105%;
  top: -2%;
}

.line {
  position: absolute;

  border: 0px;

  background: #dedede;
}

</style>
