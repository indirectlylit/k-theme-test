<template>

  <div>
    <img
      class="kolibri-logo"
      src="./icons/kolibri-logo.svg"
    >
    <img
      v-if="useWhiteText"
      src="./icons/unw-white-text.svg"
      class="unw-logo"
    >
    <img
      v-else
      src="./icons/unw.svg"
      class="unw-logo"
    >
  </div>

</template>


<script>

  export default {
    props: {
      useWhiteText: {
        type: Boolean,
        required: false,
        default: false,
      },
    },
  };

</script>


<style lang="stylus" scoped>

  .kolibri-logo
    width: 40%

  .unw-logo
    margin-left: 10%
    width: 50%

</style>
