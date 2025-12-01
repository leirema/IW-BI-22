<template>
  <section>
    <h2>La salud mental y el colapso del sistema público: ¿problema médico o consecuencia política de vivir agotados?</h2>

    <p>
      El debate se mueve entre dos explicaciones que ni siquiera se miran de frente. Una interpreta la crisis de salud mental como un fenómeno médico: aumento de diagnósticos, falta de profesionales, listas de espera imposibles y un sistema público incapaz de absorber la demanda. Bajo este marco, la prioridad es reforzar recursos, mejorar ratios y actuar con prudencia institucional.

      La otra lectura sostiene que el malestar no nace en las consultas, sino en la estructura social: precariedad laboral, cuidados invisibles, sobrecarga emocional, desigualdad de género y un ritmo económico que tritura a cualquiera. Aquí la ansiedad no se “cura” con terapia, sino reformando las condiciones de vida.

      Entre ambos extremos, los discursos mediáticos navegan con diferentes grados de sensibilidad o evasión. Algunos visibilizan el problema sin señalar culpables; otros denuncian la medicalización del agotamiento; y otros reducen la cuestión a responsabilidad individual o hábitos personales. El resultado es un debate con objetividad media-baja: los datos son sólidos, pero la interpretación se fragmenta entre enfoques sanitarios, políticos y culturales.
    </p>

    <ul>
      <li>El Dirio ABC enfatiza el conflicto político</li>
      <li>La sexta empuja una narrativa emocional</li>
      <li>El país se centra en datos duros</li>
    </ul>

    <SocialButtons :title="'Comparativa sobre la salud mental'"
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
      "headline": "Comparativa de sesgos: Conflicto sobre la salud mental",
      "description": "Debate sobre donde yace el colpaso del sistema sannitario.",
      "url": window.location.href
    };

    const script = document.createElement("script");
    script.type = "application/ld+json";
    script.text = JSON.stringify(jsonLd);
    document.head.appendChild(script);
  }
};
</script>
