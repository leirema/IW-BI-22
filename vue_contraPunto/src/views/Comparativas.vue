<template>
  <section>
    <h2>Todas las comparativas</h2>

    <div class="card-list">

      <!--Microdata -->
      <article class="comparativa-card"
               itemscope
               itemtype="https://schema.org/Article">
        <h3 itemprop="headline">La salud mental y el colapso del sistema público: ¿problema médico o consecuencia política de vivir agotados?</h3>
        <p itemprop="description">
          El debate se mueve entre dos explicaciones que ni siquiera se miran de frente. Una interpreta la crisis de salud mental como un fenómeno médico...
        </p>

        <button @click="$router.push('/comparativa1')">
          Ver análisis
        </button>
      </article>

      <article class="comparativa-card"
               itemscope
               itemtype="https://schema.org/Article">
        <h3 itemprop="headline">La polarización política y los medios de comunicación: ¿informan o moldean nuestra manera de pensar?</h3>
        <p itemprop="description">
          El debate sobre el papel de los medios en la polarización se mueve entre la defensa del periodismo como pilar democrático y la sospecha de que la información se ha convertido en un arma ideológica. Por un lado, una visión institucional sostiene que el principal peligro es la desinformación...
        </p>

        <button @click="$router.push('/comparativa2')">
          Ver análisis
        </button>
      </article>

    </div>
  </section>
</template>

<script>
export default {};
</script>
