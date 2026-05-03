import TreatmentBlock from "@/components/TreatmentBlock";
import IMG from "@/lib/assets";

const items = [
  { type: "image", src: IMG.dubaiSkyline, label: "Dubai · Reference", caption: "Inspiración" },
  { type: "image", src: IMG.laserMachine, label: "Lipo Láser", caption: "Tecnología" },
  { type: "image", src: IMG.bodyAbdomen, label: "Abdomen", caption: "Antes · Después" },
  { type: "video", src: IMG.videoLegs, label: "Piernas", caption: "Proceso" },
  { type: "image", src: IMG.rfHeads, label: "Radiofrecuencia RF", caption: "Cabezales" },
  { type: "image", src: IMG.bodyLegs, label: "Piernas", caption: "Firmeza" },
  { type: "image", src: IMG.chinAfter, label: "Papada", caption: "Neck tightening" },
  { type: "image", src: IMG.bodyWomanLuxe, label: "Silueta", caption: "Escultural" },
  { type: "image", src: IMG.tobaccoRoom, label: "Studio · Tobacco Room", caption: "Ambiente" },
  { type: "image", src: IMG.bodyBack, label: "Brazos", caption: "Definición" },
];

export default function TreatmentLipo() {
  return (
    <TreatmentBlock
      id="lipo-laser"
      testid="treatment-lipo"
      eyebrow="Signature · Body Sculpting"
      title="Lipo con"
      titleItalic="Láser."
      italicIntro="Esculpe localizadamente abdomen, brazos, piernas o papada con tecnología láser + ultrasonido + radiofrecuencia + terapia de luz de 7 colores. Reduce, moldea, reafirma y rejuvenece tu piel sin cirugía, sin dolor — resultados desde la primera sesión."
      areas={["Abdomen", "Brazos", "Piernas", "Papada"]}
      items={items}
      bgImage={IMG.tobaccoRoom}
      bodyAfter="El láser rojo (650nm) penetra la piel y actúa sobre las células de grasa, que el cuerpo elimina de forma natural a través del sistema linfático. Luego, la radiofrecuencia y la luz terapéutica reafirman la piel, mejoran estrías y dejan una apariencia más luminosa y rejuvenecida."
      bullets={[
        "Reduce medidas localizadas",
        "Reafirma y tensa la piel",
        "Mejora estrías y textura",
        "Sin dolor, sin cirugía, sin downtime",
      ]}
    />
  );
}
