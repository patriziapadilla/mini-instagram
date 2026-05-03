import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import { Star } from "lucide-react";
import IMG from "@/lib/assets";

export default function Hero() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start start", "end start"],
  });

  const y = useTransform(scrollYProgress, [0, 1], [0, 180]);
  const scale = useTransform(scrollYProgress, [0, 1], [1.05, 1.18]);
  const opacity = useTransform(scrollYProgress, [0, 0.8], [0.45, 0.1]);
  const titleY = useTransform(scrollYProgress, [0, 1], [0, -120]);
  const titleOpacity = useTransform(scrollYProgress, [0, 0.7], [1, 0]);

  return (
    <section
      id="inicio"
      ref={ref}
      data-testid="hero-section"
      className="relative min-h-[100svh] pt-28 sm:pt-36 pb-16 overflow-hidden"
    >
      {/* Parallax hero image (Dubai rascacielos) */}
      <motion.div
        style={{ y, scale, opacity }}
        className="absolute inset-0 -z-10"
        aria-hidden
      >
        <img
          src={IMG.dubaiSkyline}
          alt=""
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-[var(--cream)]/55" />
        <div className="absolute inset-0 bg-gradient-to-b from-[var(--cream)]/40 via-transparent to-[var(--cream)]" />
      </motion.div>

      <div className="relative max-w-[1400px] mx-auto px-5 sm:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="flex flex-wrap items-center gap-3 text-[0.72rem] tracking-[0.24em] uppercase text-[var(--ink)]/75 mb-8"
        >
          <span>D'Royal Spa · Miami</span>
          <span className="opacity-40">/</span>
          <span>Belleza inteligente · Sin cirugía</span>
        </motion.div>

        <motion.h1
          data-testid="hero-title"
          style={{ y: titleY, opacity: titleOpacity }}
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.1, ease: [0.2, 0.7, 0.2, 1] }}
          className="font-display font-light text-[14vw] sm:text-[10vw] lg:text-[9rem] leading-[0.9] tracking-[-0.02em] text-[var(--ink)]"
        >
          D'Royal<br />
          <span className="italic font-normal">Spa.</span>
        </motion.h1>

        <div className="mt-10 grid grid-cols-1 lg:grid-cols-12 gap-10 items-end">
          <motion.div
            className="lg:col-span-6"
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.9, delay: 0.15 }}
          >
            <p className="font-display italic text-xl sm:text-2xl leading-snug text-[var(--ink)]/90 max-w-[42ch]">
              Tecnología avanzada para moldear y rejuvenecer tu cuerpo — sin agujas,
              sin cirugía, con resultados desde la primera sesión.
            </p>
          </motion.div>

          <motion.div
            className="lg:col-span-6 flex flex-col gap-5 items-start lg:items-end"
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.9, delay: 0.25 }}
          >
            <div className="flex flex-wrap gap-3">
              <a href="#agendar" data-testid="hero-agendar-btn" className="btn-pill cta-arrow">
                Agendar cita <span className="arr">→</span>
              </a>
              <a
                href="https://wa.me/17866900960"
                target="_blank"
                rel="noreferrer"
                data-testid="hero-whatsapp-btn"
                className="btn-pill ghost"
              >
                WhatsApp
              </a>
            </div>

            <div className="flex items-center gap-3 text-sm text-[var(--ink)]/85">
              <div className="flex">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} size={14} className="fill-[var(--ink)] text-[var(--ink)]" />
                ))}
              </div>
              <span>Calificación 5★ · Miami</span>
              <span className="opacity-40">·</span>
              <span>$90 1ra sesión</span>
            </div>
          </motion.div>
        </div>

        <motion.div
          className="mt-16 border-t border-[var(--line)] pt-6 flex flex-wrap items-center justify-between gap-4 text-[0.7rem] sm:text-xs tracking-[0.32em] uppercase text-[var(--ink)]/75"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 1, delay: 0.35 }}
        >
          <span>Brickell</span>
          <span className="opacity-30">·</span>
          <span>Downtown</span>
          <span className="opacity-30">·</span>
          <span>Doral</span>
          <span className="opacity-30">·</span>
          <span>Miami Beach</span>
          <span className="opacity-30">·</span>
          <span className="hidden sm:inline">100% In-home</span>
        </motion.div>
      </div>
    </section>
  );
}
