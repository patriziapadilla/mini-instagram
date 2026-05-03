import { useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import { ArrowLeft, ArrowRight, Play } from "lucide-react";

export default function Carousel({ items = [], testid = "carousel" }) {
  const ref = useRef(null);

  const scrollBy = (dir) => {
    const el = ref.current;
    if (!el) return;
    const card = el.querySelector("[data-card]");
    const step = card ? card.clientWidth + 24 : 320;
    el.scrollBy({ left: dir * step, behavior: "smooth" });
  };

  return (
    <div data-testid={testid} className="relative">
      <div
        ref={ref}
        className="no-scrollbar flex gap-6 overflow-x-auto snap-x snap-mandatory pb-6 -mx-5 sm:-mx-8 px-5 sm:px-8"
      >
        {items.map((it, i) => (
          <Card key={i} item={it} idx={i} testid={`${testid}-card-${i}`} />
        ))}
      </div>

      {items.length > 1 && (
        <div className="flex items-center justify-end gap-2 mt-2">
          <button
            data-testid={`${testid}-prev`}
            aria-label="anterior"
            onClick={() => scrollBy(-1)}
            className="w-11 h-11 rounded-full border border-[var(--ink)]/30 hover:bg-[var(--ink)] hover:text-[var(--cream)] transition-all flex items-center justify-center"
          >
            <ArrowLeft size={18} />
          </button>
          <button
            data-testid={`${testid}-next`}
            aria-label="siguiente"
            onClick={() => scrollBy(1)}
            className="w-11 h-11 rounded-full border border-[var(--ink)]/30 hover:bg-[var(--ink)] hover:text-[var(--cream)] transition-all flex items-center justify-center"
          >
            <ArrowRight size={18} />
          </button>
        </div>
      )}
    </div>
  );
}

function Card({ item, idx, testid }) {
  const cardRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: cardRef,
    offset: ["start end", "end start"],
  });
  const y = useTransform(scrollYProgress, [0, 1], [40, -40]);
  const scale = useTransform(scrollYProgress, [0, 0.5, 1], [0.96, 1, 0.98]);

  return (
    <motion.article
      ref={cardRef}
      data-card
      data-testid={testid}
      style={{ y, scale }}
      whileHover={{ y: -8, transition: { duration: 0.5 } }}
      className="snap-start shrink-0 w-[80%] sm:w-[48%] lg:w-[32%] rounded-[28px] overflow-hidden relative bg-[var(--cream-2)] border border-[var(--line)] shadow-[0_8px_40px_rgba(0,0,0,0.06)]"
    >
      <div className="aspect-[4/5] relative overflow-hidden group">
        {item.type === "video" && item.src ? (
          <video
            src={item.src}
            className="w-full h-full object-cover transition-transform duration-[1.4s] group-hover:scale-[1.06]"
            muted
            loop
            playsInline
            autoPlay
            poster={item.poster}
          />
        ) : item.src ? (
          <img
            src={item.src}
            alt={item.label || "D'Royal Spa"}
            className="w-full h-full object-cover transition-transform duration-[1.4s] group-hover:scale-[1.06]"
            loading="lazy"
          />
        ) : (
          <div className="sky-card w-full h-full" />
        )}

        {item.type === "video" && (
          <div className="absolute bottom-4 left-4 w-11 h-11 rounded-full bg-[var(--ink)]/85 text-[var(--cream)] flex items-center justify-center backdrop-blur-sm">
            <Play size={16} />
          </div>
        )}

        <div className="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-black/40 to-transparent pointer-events-none" />
      </div>

      <div className="p-5 flex items-center justify-between">
        <div>
          <div className="text-[0.7rem] tracking-[0.24em] uppercase text-[var(--ink)]/55">
            {item.caption || "Resultado"}
          </div>
          <div className="font-display text-lg">{item.label || "—"}</div>
        </div>
        <span className="text-xs text-[var(--ink)]/60">
          {String(idx + 1).padStart(2, "0")}
        </span>
      </div>
    </motion.article>
  );
}
