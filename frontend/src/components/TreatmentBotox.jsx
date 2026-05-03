import TreatmentBlock from "@/components/TreatmentBlock";
import IMG from "@/lib/assets";

const items = [
  { type: "image", src: IMG.faceModel, label: "Rostro natural", caption: "Resultado" },
  { type: "image", src: IMG.facialTreatment, label: "Facial RF", caption: "Cabezales" },
  { type: "image", src: IMG.faceClose, label: "Piel luminosa", caption: "Antes · Después" },
  { type: "image", src: IMG.faceLaser, label: "Láser Frente", caption: "Premium" },
  { type: "image", src: IMG.faceGlow, label: "Glow natural", caption: "Botox Natural" },
];

export default function TreatmentBotox() {
  return (
    <TreatmentBlock
      id="botox-natural"
      testid="treatment-botox"
      reversed
      eyebrow="Rejuvenecimiento · Facial"
      title="Botox Natural"
      titleItalic="con Láser."
      italicIntro="Hydromicrodermabrasion + D'Cool + Radiofrecuencia + Terapia de luz de 7 colores que regenera las células madres, eliminando líneas de expresión y pigmentación — ideal para rejuvenecer de forma natural, sin agujas, sin inyecciones, sin tiempo de recuperación."
      areas={["Ojos", "Cara", "Cuello"]}
      items={items}
      bodyAfter="Láser que actúa hasta 3 mm de profundidad, estimulando la regeneración de la piel. Se sella con frío para calmar y potenciar resultados."
      bullets={[
        "Estimula colágeno y elastina",
        "Regenera la piel en profundidad",
        "Limpieza facial profunda",
        "Reduce líneas y manchas",
        "Rejuvenece la piel",
      ]}
    />
  );
}
