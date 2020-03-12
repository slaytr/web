<template>
  <div class="home">
    <div class="home__bg">
      <img class="home__bg--image" src="../assets/landing.jpg" alt="glasses"/>
    </div>
    <div class="home__content">
      <div class="home__content--intro">
        <h1>Welcome!</h1>
        <p>This website is where all my ridiculous and rampant ideas are archived</p>
      </div>
      <img class="home__content--wizard" src="@/assets/wizard-icon.svg" alt="wizard"/>
    </div>
  </div>
</template>

<script>
// // @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
//
// export default {
//   name: 'Home',
//   components: {
//     HelloWorld
//   }
// }
</script>

<style lang="scss">
.home {
  position: relative;
  width: 100%;

  .home__bg--image {
    width: 100%;
  }
}

.home__content {
  position: absolute;
  top: 100px;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: calc(100% - 80px);
  padding: 40px;

  .home__content--intro {
    width: 600px;
    height: 160px;
    background-color: rgba(44, 52, 56, 0.7);

    font-size: 20px;
    line-height: 26px;
    color: #FAFAFA;
    padding: 20px 40px;
    border-radius: 20px;
    text-align: left;
  }

  .home__content--wizard {
    width: 400px;
    height: 400px;
  }
}
</style>