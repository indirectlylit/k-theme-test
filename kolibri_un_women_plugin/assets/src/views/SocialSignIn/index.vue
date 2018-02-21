<template>

  <div id="social-sign-in">
    <p class="heading">{{ $tr('orAlternatively') }}</p>

    <k-external-link
      :text="$tr('signInWithGoogle')"
      appearance="raised-button"
      class="google-button"
      href="/user/login/google-oauth2/"
    />
    <br>
    <k-external-link
      :text="$tr('signInWithFacebook')"
      appearance="raised-button"
      class="facebook-button"
      href="/user/login/facebook/"
    />
    <br>
    <k-external-link
      :text="$tr('signInWithTwitter')"
      appearance="raised-button"
      class="twitter-button"
      href="/user/login/twitter/"
    />
  </div>

</template>


<script>

  import kExternalLink from 'kolibri.coreVue.components.kExternalLink';

  export default {
    name: 'socialSignIn',
    components: {
      kExternalLink,
    },

    $trs: {
      orAlternatively: 'Or alternatively:',
      signInWithGoogle: 'Sign in with Google',
      signInWithFacebook: 'Sign in with Facebook',
      signInWithTwitter: 'Sign in with Twitter',
    },
  };

</script>


<style lang="stylus" scoped>

  .heading
    color: white

  $google = #DC4E41
  $facebook = #3B5998
  $twitter = #1DA1F2


  #social-sign-in
    .button.secondary.raised
      &.google-button
        background-color: $google
        &:hover, &:focus
          background-color: darken($google, 10)
      &.facebook-button
        background-color: $facebook
        &:hover, &:focus
          background-color: darken($facebook, 10)
      &.twitter-button
        background-color: $twitter
        &:hover, &:focus
          background-color: darken($twitter, 10)

</style>
