<template>
    <section>
        <h2>Bienvenido a ContraPunto</h2>
        <p>En un mundo saturado de información, esta plataforma te ayuda a ver más allá de los titulares. El objetivo es ofrecer una visión plural de la actualidad, mostrando cómo distintos medios narran los mismos hechos desde perspectivas diversas. Cada comparativa reúne noticias de varios comunicados sobre un mismo tema, para que puedas analizar diferencias en el enfoque, el tono y la orientación ideológica.

Las noticias no solo informan: también interpretan. Por eso, nuestro sistema identifica tres tipos de sesgos en cada informe:

Ideológico: la posición política del medio, entre lo progresista y lo conservador.
Emocional: el estilo narrativo, desde lo analítico (desmeluza datos y contexto), pasando por institucional (cita fuentes oficiales) y militante (defiende abiertamente una causa), hasta lo sensacionalista (dramatiza).
De enfoque: la perspectiva predominante, ya sea social (movimientos ciudadanos y minorias), económica (datos del mercado y fuentes financieras), política (institucional y élites) o cultural (territorial y resalta la identidad).
Al combinar estos factores, las comparativas permiten entender no solo lo que se dice, sino también cómo y desde dónde se cuenta.

En resumen, forma tu propio criterio: con las versiones, los matices y las intenciones detrás de cada noticia, tendrás una mirada más crítica y completa.</p>
    </section>
  <section>
    <h2>Comparativas más destacadas</h2>
    <div class="card-list">

      <!--Microdata -->
      <article 
        class="comparativa-card"
        itemscope
        itemtype="https://schema.org/Article"
      >
        <h3 itemprop="headline">La salud mental y el colapso del sistema público: ¿problema médico o consecuencia política de vivir agotados?</h3>
        <p itemprop="description">
          El debate se mueve entre dos explicaciones que ni siquiera se miran de frente. Una interpreta la crisis de salud mental como un fenómeno médico...
        </p>

        <button @click="$router.push('/comparativa1')">
          Ver análisis
        </button>
      </article>
    </div>
  </section>
</template>

<script>
export default {};
</script>
