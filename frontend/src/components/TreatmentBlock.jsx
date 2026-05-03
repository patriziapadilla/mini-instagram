import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import Carousel from "@/components/Carousel";

export default function TreatmentBlock({
  id,
  eyebrow,
  title,
  titleItalic,
  italicIntro,
  areas = [],
  items = [],
  bullets = [],
  bodyAfter,
  testid = "treatment",
  reversed = false,
  bgImage,
}) {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });
  const bgY = useTransform(scrollYProgress, [0, 1], [0, 140]);
  const bgOpacity = useTransform(scrollYProgress, [0, 0.3, 0.7, 1], [0, 0.18, 0.18, 0]);

  return (
    <section
      id={id}
      ref={ref}
      data-testid={testid}
      className="relative py-24 sm:py-32 border-t border-[var(--line)] overflow-hidden"
    >
      {bgImage && (
        <motion.div
          style={{ y: bgY, opacity: bgOpacity }}
          className="absolute inset-0 -z-10"
          aria-hidden
        >
          <img src={bgImage} alt="" className="w-full h-full object-cover" />
        </motion.div>
      )}

      <div className="max-w-[1400px] mx-auto px-5 sm:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-14">
          <motion.div
            className={`${reversed ? "lg:col-start-7" : ""} lg:col-span-6`}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 1, ease: [0.2, 0.7, 0.2, 1] }}
          >
            <div className="text-[0.72rem] tracking-[0.3em] uppercase text-[var(--ink)]/60 mb-5">
              {eyebrow}
            </div>
            <h2 className="font-display font-light text-5xl sm:text-6xl lg:text-[5.5rem] leading-[0.96] tracking-[-0.01em]">
              {title}
              {titleItalic && (
                <>
                  <br />
                  <span className="italic font-normal">{titleItalic}</span>
                </>
              )}
            </h2>
          </motion.div>

          <motion.div
            className={`${reversed ? "lg:col-start-1 lg:row-start-1" : ""} lg:col-span-6 flex flex-col justify-end gap-5`}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 1, delay: 0.1, ease: [0.2, 0.7, 0.2, 1] }}
          >
            <p className="font-display italic text-lg sm:text-xl text-[var(--ink)]/85 leading-snug max-w-[52ch]">
              {italicIntro}
            </p>
            {areas.length > 0 && (
              <div className="flex flex-wrap gap-x-5 gap-y-2 text-xs sm:text-sm tracking-[0.28em] uppercase text-[var(--ink)]/80">
                {areas.map((a, i) => (
                  <span key={a} className="flex items-center gap-5">
                    {a}
                    {i < areas.length - 1 && <span className="opacity-40">·</span>}
                  </span>
                ))}
              </div>
            )}
          </motion.div>
        </div>

        <Carousel items={items} testid={`${testid}-carousel`} />

        <div className="mt-16 grid grid-cols-1 lg:grid-cols-12 gap-8">
          {bodyAfter && (
            <motion.p
              className="lg:col-span-7 text-base sm:text-lg leading-relaxed text-[var(--ink)]/90 max-w-[68ch]"
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-80px" }}
              transition={{ duration: 0.9 }}
            >
              {bodyAfter}
            </motion.p>
          )}
          {bullets.length > 0 && (
            <ul className="lg:col-span-5 grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-2 text-sm text-[var(--ink)]/85">
              {bullets.map((b, i) => (
                <motion.li
                  key={b}
                  className="flex gap-2 items-start"
                  initial={{ opacity: 0, x: 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.6, delay: i * 0.06 }}
                >
                  <span className="mt-[0.55rem] w-1 h-1 rounded-full bg-[var(--ink)] shrink-0" />
                  <span>{b}</span>
                </motion.li>
              ))}
            </ul>
          )}
        </div>

        <div className="mt-10 flex flex-wrap gap-3">
          <a href="#agendar" data-testid={`${testid}-reservar`} className="btn-pill cta-arrow">
            Reservar <span className="arr">→</span>
          </a>
          <a
            href="https://wa.me/17866900960"
            target="_blank"
            rel="noreferrer"
            data-testid={`${testid}-consultar`}
            className="btn-pill ghost cta-arrow"
          >
            Consultar <span className="arr">↗</span>
          </a>
        </div>
      </div>
    </section>
  );
}
