<template>
  <div id="app">
    <header class="app-header">
      <h1>ContraPunto SPA</h1>
      <nav>
        <a href="/" @click.prevent="$router.push('/')">Inicio</a>
        <a href="/comparativas" @click.prevent="$router.push('/comparativas')">Comparativas</a>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>

    <footer class="app-footer">
      <p>Versión ligera de ContraPunto para la práctica de IW.</p>
    </footer>
  </div>
</template>

<script>
  // JSON-LD
  export default {
    mounted() {
      const jsonLd = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "ContraPunto SPA",
        "url": window.location.origin,
        "description": "Versión demo del proyecto ContraPunto para representar sesgos mediáticos."
      };

      const script = document.createElement("script");
      script.type = "application/ld+json";
      script.text = JSON.stringify(jsonLd);
      document.head.appendChild(script);
    }
  };
</script>

