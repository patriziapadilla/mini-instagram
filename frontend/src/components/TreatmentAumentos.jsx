import TreatmentBlock from "@/components/TreatmentBlock";
import IMG from "@/lib/assets";

const items = [
  { type: "video", src: IMG.videoSpa, label: "Vacuum Therapy", caption: "Explainer" },
  { type: "image", src: IMG.bodyGlute, label: "Glúteos", caption: "Antes · Después" },
  { type: "image", src: IMG.glutes, label: "Firmeza natural", caption: "Resultado" },
  { type: "image", src: IMG.breastShape, label: "Senos", caption: "Aumento natural" },
  { type: "image", src: IMG.bodyLegs, label: "Piernas firmes", caption: "Tonificación" },
];

export default function TreatmentAumentos() {
  return (
    <TreatmentBlock
      id="aumentos"
      testid="treatment-aumentos"
      eyebrow="Aumentos · Vacuum Therapy"
      title="Aumentos sin"
      titleItalic="Cirugía."
      italicIntro="Tecnología vacuum + láser que activa el tejido adiposo y estimula la circulación, aumentando volumen natural en glúteos y senos. Sin implantes, sin inyecciones."
      areas={["Glúteos", "Senos"]}
      items={items}
      bgImage={IMG.luxuryLounge}
      bodyAfter="Copas de succión activan el tejido adiposo, estimulan circulación y aumentan volumen natural — potenciando forma, firmeza y luminosidad de la piel."
      bullets={[
        "Aumenta volumen natural",
        "Activa tejido adiposo",
        "Mejora circulación",
        "Reafirma y levanta",
      ]}
    />
  );
}
