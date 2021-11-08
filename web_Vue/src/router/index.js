import Vue from 'vue'
import Router from 'vue-router'
import side_bar from "../components/side_bar";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'side_bar',
      component: side_bar
    }
  ]
})
