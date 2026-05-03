import { motion } from "framer-motion";
import IMG from "@/lib/assets";

const areas = [
  { name: "Brickell", note: "Cita 24/7", img: IMG.brickell },
  { name: "Downtown", note: "Cita 24/7", img: IMG.downtown },
  { name: "Doral", note: "Cita 24/7", img: IMG.doral },
  { name: "Miami Beach", note: "Cita 24/7", img: IMG.miamiBeachHood },
];

export default function Areas() {
  return (
    <section
      id="areas"
      data-testid="areas-section"
      className="py-28 sm:py-36 border-t border-[var(--line)]"
    >
      <div className="max-w-[1400px] mx-auto px-5 sm:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-16">
          <motion.div
            className="lg:col-span-7"
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 1 }}
          >
            <div className="text-[0.72rem] tracking-[0.3em] uppercase text-[var(--ink)]/60 mb-5">
              Áreas de Servicio
            </div>
            <h2 className="font-display font-light text-5xl sm:text-6xl lg:text-[6rem] leading-[0.96] tracking-[-0.01em]">
              Llegamos a tu
              <br />
              <span className="italic font-normal">puerta.</span>
            </h2>
          </motion.div>
          <motion.p
            className="lg:col-span-5 flex items-end font-display italic text-lg sm:text-xl text-[var(--ink)]/85 max-w-[42ch]"
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 1, delay: 0.15 }}
          >
            Servicio 100% in-home en las zonas premium de Miami.
            Tú relajas, nosotros llevamos todo el equipo.
          </motion.p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {areas.map((a, i) => (
            <motion.div
              key={a.name}
              data-testid={`area-${a.name.toLowerCase().replace(/\s/g, "-")}`}
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.9, delay: i * 0.08 }}
              whileHover={{ y: -8 }}
              className="group relative rounded-[28px] overflow-hidden border border-[var(--line)] bg-[var(--cream-2)] aspect-[4/5]"
            >
              <img
                src={a.img}
                alt={a.name}
                className="absolute inset-0 w-full h-full object-cover transition-transform duration-[1.5s] group-hover:scale-[1.08]"
                loading="lazy"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-black/10 to-transparent" />
              <div className="relative h-full p-6 flex flex-col justify-between text-[var(--cream)]">
                <div className="text-4xl font-display font-light">0{i + 1}</div>
                <div className="flex items-end justify-between">
                  <div>
                    <div className="font-display text-2xl">{a.name}</div>
                    <div className="text-[0.65rem] tracking-[0.22em] uppercase opacity-80 mt-1">
                      {a.note}
                    </div>
                  </div>
                  <span className="opacity-90 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform duration-500">
                    ↗
                  </span>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
