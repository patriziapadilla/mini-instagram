"""Generate 3 new educational AI videos with Sora 2:
- Luz de 7 Colores (chromotherapy on face)
- D'Cool / CoolSculpting (freezing fat cells)
- Vacuum activo (active suction cup over skin)
All abstract-scientific to pass moderation. Warm palette only.
"""
import os, time
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from emergentintegrations.llm.openai.video_generation import OpenAIVideoGeneration

load_dotenv("/app/backend/.env")
api_key = os.environ['EMERGENT_LLM_KEY']

BASE = """Cinematic scientific micro-photography visualization. Warm cream and gold palette.
NO blue, NO cold tones. Slow motion medical educational animation.
NO text, NO logos, NO labels, NO watermarks. Abstract only, no human skin shown."""

VIDEOS = [
    ("explainer-luz-7-colores",
     f"""Abstract medical chromotherapy animation: a soft golden sphere in warm cream void.
Seven waves of colored light — gold, amber, soft pink, champagne, coral, peach, warm white —
pulse out from the sphere one by one, each wave gently expanding outward with a soft glow.
Tiny golden particles follow each wave, dancing like dust in sunlight.
Elegant, slow, hypnotic. Pure abstract — no face or body. Warm palette only. {BASE}"""),

    ("explainer-dcool-facial",
     f"""Abstract scientific animation: small round golden spheres (fat cells) suspended in warm cream fluid.
Gentle crystalline frost patterns form slowly on the spheres — soft white-gold ice crystals bloom
across their surface. The spheres shrink, crack softly into golden particles, and flow away in a warm current.
Slow motion, dreamy, jewel-like. Cream-gold palette, no skin, no body. {BASE}"""),

    ("explainer-vacuum-active",
     f"""Abstract scientific animation: a transparent dome-shaped glass vessel filled with warm golden liquid.
Inside the vessel, visible upward suction creates a graceful swirl — liquid rises forming a gentle vortex,
golden particles spiral upward being drawn into the dome.
A soft pulsing rhythm shows activation. Cream-gold warm palette throughout.
Purely abstract — only the dome and the glowing swirl, no body or skin. {BASE}"""),
]


def gen_one(item):
    name, prompt = item
    try:
        gen = OpenAIVideoGeneration(api_key=api_key)
        video_bytes = gen.text_to_video(
            prompt=prompt,
            model="sora-2",
            size="1280x720",
            duration=4,
            max_wait_time=600,
        )
        if not video_bytes:
            print(f"[{name}] FAIL: no bytes")
            return False
        out = f"/app/home-3d/mockups/{name}.mp4"
        gen.save_video(video_bytes, out)
        print(f"[{name}] OK -> {out}")
        return True
    except Exception as e:
        print(f"[{name}] ERR: {e}")
        return False


def main():
    start = time.time()
    with ThreadPoolExecutor(max_workers=3) as ex:
        list(ex.map(gen_one, VIDEOS))
    print(f"\nDone in {time.time()-start:.1f}s")


if __name__ == "__main__":
    main()
