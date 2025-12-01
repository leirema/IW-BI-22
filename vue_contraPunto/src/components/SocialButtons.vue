<template>
  <div class="social-buttons">
    <a :href="twitterUrl"
       target="_blank"
       rel="noopener"
       class="btn social twitter">
      Compartir en Twitter
    </a>

    <a :href="facebookUrl"
       target="_blank"
       rel="noopener"
       class="btn social facebook">
      Compartir en Facebook
    </a>
  </div>
</template>

<script>
export default {
  props: ['title', 'url'],
  computed: {
    twitterUrl() {
      return `https://twitter.com/intent/tweet?text=${encodeURIComponent(this.title)}&url=${encodeURIComponent(this.url)}`;
    },
    facebookUrl() {
      return `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(this.url)}`;
    }
  }
};
</script>
