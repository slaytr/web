<template>
  <div id="app">
    <header class="body-header">
      <img class="body-header-logo" src="@/assets/wizard-icon.png" alt="logo"/>
      <div class="body-header-text-logo">Bill Li</div>
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link> |
        <router-link to="/development">Development</router-link>
      </div>
    </header>
    <router-view/>
  </div>
</template>

<style lang="scss">
$white : #FAFAFA;
$titles : #001f52;

body {
  margin: 0;
}

.body-header {
  height: 60px;
  background-color: $white;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: row;
  align-items: center;
}

.body-header-logo {
  width: 60px;
  height: 60px;
  opacity: 0.9;
  margin: 0 10px;
}

.body-header-text-logo {
  font-family: "Roboto";
  font-size: 28px;
  color: $titles;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 30px;

  a {
    text-decoration: none;
    font-weight: bold;
    color: #2c3e50;
    padding: 0 10px;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
