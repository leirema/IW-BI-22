<template>
  <section>
    <h2>La polarización política y los medios de comunicación: ¿informan o moldean nuestra manera de pensar?</h2>

    <p>
      El debate sobre el papel de los medios en la polarización se mueve entre la defensa del periodismo como pilar democrático y la sospecha de que la información se ha convertido en un arma ideológica. Por un lado, una visión institucional sostiene que el principal peligro es la desinformación: bulos, saturación de contenidos y algoritmos que recompensan el enfrentamiento. Desde esta mirada, el problema es técnico y democrático a la vez: cómo garantizar rigor y pluralidad en un entorno comunicativo dominado por la velocidad y la intensidad emocional.

      En contraste, otra narrativa denuncia que la polarización no surge de manera espontánea, sino de la captura de los medios por intereses políticos o económicos. Para algunos, la causa sería la concentración empresarial; para otros, la hegemonía cultural de ciertas ideologías; y para otros, la instrumentalización de los medios públicos y privados para manufacturar opinión. Aquí el foco se desplaza hacia quién controla los relatos y cómo se construye la agenda pública.

      En medio de estas posiciones, los medios generalistas intentan proyectar neutralidad, pero sus tertulias y formatos de debate tienden al conflicto, reforzando dinámicas de trinchera. En conjunto, la objetividad es moderada-baja: los datos sobre polarización existen, pero cada medio los interpreta desde su propio marco, generando un paisaje fragmentado donde se mezclan análisis, opinión y espectáculo.
    </p>

    <ul>
      <li>El Dirio ABC enfatiza el conflicto político</li>
      <li>La sexta empuja una narrativa emocional</li>
      <li>El país se centra en datos duros</li>
    </ul>

    <SocialButtons :title="'Comparativa sobre la polarización política'"
                   :url="currentUrl" />
  </section>
</template>

<script>
import SocialButtons from '../components/SocialButtons.vue';

export default {
  components: { SocialButtons },
  data() {
    return {
      currentUrl: window.location.href
    }
  },
  mounted() {
    // JSON-LD
    const jsonLd = {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Comparativa de sesgos: Conflicto sobre la politica polarizada",
      "description": "Debate sobre la manipulación de los medios de comunicación.",
      "url": window.location.href
    };

    const script = document.createElement("script");
    script.type = "application/ld+json";
    script.text = JSON.stringify(jsonLd);
    document.head.appendChild(script);
  }
};
</script>
