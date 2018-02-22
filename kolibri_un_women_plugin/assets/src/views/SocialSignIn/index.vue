<template>

  <div id="social-sign-in">
    <p class="heading">{{ $tr('orAlternatively') }}</p>

    <a
      href="/user/login/google-oauth2/"
      class="button secondary raised google-button"
    >
      <file-svg
        src="./google.svg"
        slot="icon"
      />
      {{ $tr('signInWithGoogle') }}
    </a>

    <br>

    <a
      href="/user/login/facebook/"
      class="button secondary raised facebook-button"
    >
        <file-svg
          src="./facebook.svg"
          slot="icon"
        />
        {{ $tr('signInWithFacebook') }}
    </a>

    <br>

    <a
      href="/user/login/twitter/"
      class="button secondary raised twitter-button"
    >
        <file-svg
          src="./twitter.svg"
          slot="icon"
        />
        {{ $tr('signInWithTwitter') }}
    </a>

  </div>

</template>


<script>

  export default {
    name: 'socialSignIn',
    $trs: {
      orAlternatively: 'Or alternatively:',
      signInWithGoogle: 'Sign in with Google',
      signInWithFacebook: 'Sign in with Facebook',
      signInWithTwitter: 'Sign in with Twitter',
    },
  };

</script>


<style lang="stylus" scoped>

  @require '~kolibri.styles.buttonAndLinkStyles'

  .heading
    color: white

  $google = #DC4E41
  $facebook = #3B5998
  $twitter = #1DA1F2

  #social-sign-in
    .button.secondary.raised
      min-width: 245px
      text-align: left
      svg
        vertical-align: text-bottom
        margin-right: 8px
        height: 20px
        fill: white
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
