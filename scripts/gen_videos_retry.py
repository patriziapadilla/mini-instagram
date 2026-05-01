"""Retry the 3 failed videos."""
import os, time
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from emergentintegrations.llm.openai.video_generation import OpenAIVideoGeneration

load_dotenv("/app/backend/.env")
api_key = os.environ['EMERGENT_LLM_KEY']

BASE = """Cinematic medical visualization, hyperrealistic.
Warm cream and gold palette only. NO blue NO cold tones, NO black backgrounds.
Slow motion, professional aesthetic medicine educational video.
NO text, NO logos, NO labels, NO watermarks, pure cinematic visualization."""

VIDEOS = [
    ("explainer-ultrasound",
     f"""Macro view of human skin surface and underlying fat tissue layer in warm cream tones.
Concentric sound wave ripples (ultrasonic cavitation) emanate downward into the tissue from a handheld device.
The waves cause golden fat cells in the deeper layer to vibrate, form micro-bubbles inside, and gradually break apart releasing soft golden liquid.
Skin surface remains intact while the fat cells dissolve below.
Slow motion scientific animation. {BASE}"""),
    
    ("explainer-coolsculpting",
     f"""Macro view of skin surface with a cooling applicator placed on it.
Visible cold mist (white frost particles, NEVER blue — cream-white frost only) emerges from the applicator and penetrates into the underlying fat tissue.
Round golden fat cells in the hypodermis crystallize, harden into ice-like structures, then gradually dissolve and shrink.
Surrounding muscle and skin tissue stays warm cream colored, untouched.
Slow motion. {BASE}"""),
    
    ("explainer-vacuum-glutes",
     f"""Macro view of glute area cross-section showing skin, fat layer, and muscle in warm cream tones.
A large clear glass vacuum cup pressed gently to the skin surface creates visible suction.
The skin and fat tissue lift upward gently into the cup creating a beautiful natural lifting effect.
Underneath, fat cells become activated, blood flow increases (visible warm golden pulsing).
The glute contour visibly rounds and lifts naturally. {BASE}"""),
]


def gen_one(item):
    name, prompt = item
    print(f"[{name}] retry...")
    try:
        gen = OpenAIVideoGeneration(api_key=api_key)
        video_bytes = gen.text_to_video(
            prompt=prompt, model="sora-2", size="1280x720", duration=4, max_wait_time=600
        )
        if not video_bytes:
            print(f"[{name}] FAIL: no bytes")
            return name, False
        out = f"/app/home-3d/mockups/{name}.mp4"
        gen.save_video(video_bytes, out)
        print(f"[{name}] OK -> {out}")
        return name, True
    except Exception as e:
        print(f"[{name}] ERR: {e}")
        return name, False


def main():
    start = time.time()
    with ThreadPoolExecutor(max_workers=3) as ex:
        results = list(ex.map(gen_one, VIDEOS))
    print(f"\nDone in {time.time()-start:.1f}s")
    print(results)


if __name__ == "__main__":
    main()
