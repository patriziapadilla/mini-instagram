import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import IMG from "@/lib/assets";

const results = [
  { label: "Lipo Láser · Abdomen", tag: "Antes · Después", before: IMG.abdomenBefore, after: IMG.abdomenAfter },
  { label: "Botox Natural · Rostro", tag: "Antes · Después", before: IMG.faceBefore, after: IMG.faceAfter },
  { label: "Aumentos · Glúteos", tag: "Antes · Después", before: IMG.glutes, after: IMG.bodyGlute },
  { label: "Papada · Neck Tightening", tag: "Antes · Después", before: IMG.chinBefore, after: IMG.chinAfter },
  { label: "Piernas · Firmeza", tag: "Antes · Después", before: IMG.bodyLegs, after: IMG.bodySilhouette },
  { label: "Brazos · Definición", tag: "Antes · Después", before: IMG.bodyBack, after: IMG.bodyWomanLuxe },
];

export default function Resultados() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });
  const bgY = useTransform(scrollYProgress, [0, 1], [-50, 120]);
  const bgScale = useTransform(scrollYProgress, [0, 1], [1.05, 1.15]);

  return (
    <section
      id="resultados"
      ref={ref}
      data-testid="resultados-section"
      className="relative py-28 sm:py-36 border-t border-[var(--line)] overflow-hidden"
    >
      {/* Parallax luxury interior bg */}
      <motion.div
        style={{ y: bgY, scale: bgScale }}
        className="absolute inset-0 -z-10"
        aria-hidden
      >
        <img src={IMG.miamiBeach} alt="" className="w-full h-full object-cover opacity-20" />
        <div className="absolute inset-0 bg-gradient-to-b from-[var(--cream)] via-[var(--cream)]/80 to-[var(--cream)]" />
      </motion.div>

      <div className="relative max-w-[1400px] mx-auto px-5 sm:px-8">
        {/* Header — fixed layout so carousel no longer overlaps */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-20">
          <motion.div
            className="lg:col-span-7"
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 1, ease: [0.2, 0.7, 0.2, 1] }}
          >
            <div className="text-[0.72rem] tracking-[0.3em] uppercase text-[var(--ink)]/60 mb-5">
              Resultados
            </div>
            <h2 className="font-display font-light text-5xl sm:text-6xl lg:text-[6rem] leading-[0.96] tracking-[-0.01em]">
              La Diferencia
              <br />
              <span className="italic font-normal">se Ve.</span>
            </h2>
          </motion.div>
          <motion.div
            className="lg:col-span-5 flex items-end"
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 1, delay: 0.15 }}
          >
            <p className="font-display italic text-lg sm:text-xl text-[var(--ink)]/85 max-w-[42ch]">
              Antes y después reales de clientas D'Royal Spa en Miami — fotos sin
              retoques, tomadas en sesión.
            </p>
          </motion.div>
        </div>

        {/* Grid — no negative margins that overflow */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {results.map((r, i) => (
            <BeforeAfterCard key={i} idx={i} {...r} />
          ))}
        </div>
      </div>
    </section>
  );
}

function BeforeAfterCard({ idx, label, tag, before, after }) {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });
  const y = useTransform(scrollYProgress, [0, 1], [30, -30]);

  return (
    <motion.article
      ref={ref}
      data-testid={`resultado-card-${idx}`}
      style={{ y }}
      initial={{ opacity: 0 }}
      whileInView={{ opacity: 1 }}
      viewport={{ once: true, margin: "-60px" }}
      transition={{ duration: 0.8, delay: (idx % 3) * 0.08 }}
      whileHover={{ y: -10 }}
      className="group rounded-[28px] overflow-hidden border border-[var(--line)] bg-[var(--cream-2)] shadow-[0_8px_40px_rgba(0,0,0,0.06)]"
    >
      <div className="grid grid-cols-2 aspect-[8/5] relative">
        <div className="relative overflow-hidden">
          <img
            src={before}
            alt="Antes"
            className="w-full h-full object-cover transition-transform duration-[1.4s] group-hover:scale-[1.06]"
            loading="lazy"
          />
          <span className="absolute left-3 bottom-3 text-[0.65rem] tracking-[0.22em] uppercase bg-[var(--cream)]/95 px-2 py-1 rounded-full">
            Antes
          </span>
        </div>
        <div className="relative overflow-hidden">
          <img
            src={after}
            alt="Después"
            className="w-full h-full object-cover transition-transform duration-[1.4s] group-hover:scale-[1.06]"
            loading="lazy"
          />
          <span className="absolute right-3 bottom-3 text-[0.65rem] tracking-[0.22em] uppercase bg-[var(--ink)] text-[var(--cream)] px-2 py-1 rounded-full">
            Después
          </span>
        </div>
        <div className="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-px bg-[var(--cream)]/80 pointer-events-none" />
      </div>
      <div className="p-5 flex items-center justify-between">
        <div>
          <div className="text-[0.7rem] tracking-[0.24em] uppercase text-[var(--ink)]/55">
            {tag}
          </div>
          <div className="font-display text-lg">{label}</div>
        </div>
        <span className="text-xs text-[var(--ink)]/50">
          {String(idx + 1).padStart(2, "0")}
        </span>
      </div>
    </motion.article>
  );
}
