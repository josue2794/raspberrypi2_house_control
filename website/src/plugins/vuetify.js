import Vue from 'vue'
import {
  Vuetify,
  VApp,
  VNavigationDrawer,
  VFooter,
  VList,
  VBtn,
  VIcon,
  VGrid,
  VToolbar,
    VTextField,
    VDataTable,
    VSwitch,
    VAlert,
    VImg,
    VCard,

    VSubheader,
  transitions
} from 'vuetify'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
VTextField,
      VDataTable,
      VSwitch,
VAlert,
      VImg,
      VCard,
      VSubheader,
    transitions
  },
})
