import TreatmentBlock from "@/components/TreatmentBlock";
import IMG from "@/lib/assets";

const items = [
  { type: "image", src: IMG.iceBlue, label: "CoolSculpting", caption: "Criolipólisis" },
  { type: "image", src: IMG.rfHeads, label: "Radiofrecuencia RF", caption: "Cabezales" },
  { type: "image", src: IMG.abdomenAfter, label: "Abdomen 360", caption: "Antes · Después" },
  { type: "image", src: IMG.bodySilhouette, label: "Body contouring", caption: "Tratamiento" },
  { type: "image", src: IMG.frostBody, label: "Frost therapy", caption: "-9°C a -11°C" },
];

export default function TreatmentCoolsculpting() {
  return (
    <TreatmentBlock
      id="coolsculpting"
      testid="treatment-coolsculpting"
      reversed
      eyebrow="Criolipólisis · Fat Freezing"
      title="Cool"
      titleItalic="Sculpting."
      italicIntro="Criolipólisis médica que congela y elimina células de grasa resistente — segura, no invasiva y con resultados graduales que se mantienen en el tiempo."
      areas={["Abdomen", "Flancos", "Muslos", "Brazos"]}
      items={items}
      bodyAfter="Enfriamiento controlado (-9 a -11 °C) que cristaliza las células grasas sin dañar tejidos vecinos. El cuerpo las elimina naturalmente en las siguientes semanas, moldeando la silueta de forma progresiva."
      bullets={[
        "Elimina grasa resistente",
        "No invasivo, sin agujas",
        "Resultados duraderos",
        "Sin tiempo de recuperación",
      ]}
    />
  );
}
