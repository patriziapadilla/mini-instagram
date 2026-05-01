"""Generate 7 AI explainer videos in parallel for D'Royal Spa treatments."""
import os, sys, time
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from emergentintegrations.llm.openai.video_generation import OpenAIVideoGeneration

load_dotenv("/app/backend/.env")
api_key = os.environ['EMERGENT_LLM_KEY']

BASE = """Cinematic medical micro-photography visualization, scientific accuracy, hyperrealistic.
Warm royal-gentle palette: champagne #f5e9d3, antique gold #c9a875, cream, NO blue NO cold tones, NO black backgrounds.
Slow motion, dreamy, professional aesthetic medicine educational video.
NO text, NO logos, NO labels, NO TikTok overlays, pure cinematic visualization."""

VIDEOS = [
    ("explainer-ultrasound",
     f"""Cross-section view of human skin and fat cells in warm cream palette.
Visible sound wave ripples (ultrasonic cavitation 40kHz) penetrating skin layers and reaching round golden fat cells in the hypodermis.
The vibrations create gentle micro-bubbles that gradually break the fat cell membranes, releasing soft golden liquid that flows out.
The cells deflate slowly as their contents are released. {BASE}"""),
    
    ("explainer-rf",
     f"""Cross-section view of human skin in warm cream palette showing dermis with collagen fibers.
Warm radiofrequency energy waves (golden-amber radiating heat) penetrate from above into the dermis.
The collagen fibers begin to contract, tighten, and reorganize — visible as thin golden threads becoming denser, more defined, lifted.
Skin surface visibly tightens and smooths from above. New fresh collagen fibers form. {BASE}"""),
    
    ("explainer-coolsculpting",
     f"""Cross-section view of human skin in warm cream palette.
A cooling applicator placed on the skin surface emits visible cold mist (cream-white frost particles, NOT blue).
The cold reaches the round golden fat cells in the hypodermis layer, causing them to crystallize, harden, and gradually shrink.
The crystallized fat cells slowly dissolve and disappear over time, drained naturally.
Surrounding tissue (skin, muscle) remains untouched. {BASE}"""),
    
    ("explainer-vacuum-glutes",
     f"""Cross-section view of buttocks/glute area showing skin, fat layer, and muscle tissue in warm cream palette.
A large clear glass vacuum suction cup is placed on the skin surface with gentle visible suction.
The suction pulls skin and fat tissue upward gently, activating fat cells and stimulating blood flow (golden warm flow visible).
Adipocytes (fat cells) become activated, plumping up the area, increasing volume naturally.
Glute area visibly lifts and rounds from the suction. {BASE}"""),
    
    ("explainer-vacuum-breasts",
     f"""Cross-section view of breast tissue showing skin, glandular tissue, and supporting structures in warm cream palette.
A large clear glass vacuum suction cup is placed gently on the breast area with visible suction effect.
The gentle suction stimulates blood flow (warm golden flow visible), activates fatty and glandular tissue, encourages volume increase.
The breast contour visibly lifts and gains natural fullness from the activation. {BASE}"""),
    
    ("explainer-lymphatic",
     f"""Extended cross-section view showing skin, fat layer, and lymphatic vessels (visible as golden-green branching channels) in warm cream palette.
First: red laser light hits round fat cells melting them into golden liquid (lipo laser action).
Then: ultrasonic waves further break down remaining fat releasing more golden liquid.
Then: vacuum therapy on the skin surface creating gentle pressure that pushes the released golden fat liquid INTO the lymphatic vessels.
The golden fat liquid flows through the visible lymphatic channels, draining away naturally through the body's lymphatic system.
Beautiful flowing animation of the entire process. {BASE}"""),
    
    ("explainer-botox-natural",
     f"""Cross-section view of facial skin in warm cream palette showing dermis with mature collagen fibers and aging cells.
A handheld golden laser wand emits warm amber light onto the skin (NO needles, NO injections).
The laser combined with radiofrequency heat penetrates deep into the dermis.
Mature aging cells visibly regenerate — new fresh young cells appear, skin tightens, fine lines smooth out, glowing healthy radiance.
The collagen fibers reorganize and densify. New blood vessels form. Skin visibly rejuvenates from within. {BASE}"""),
]


def gen_one(item):
    name, prompt = item
    print(f"[{name}] STARTING...")
    try:
        gen = OpenAIVideoGeneration(api_key=api_key)
        video_bytes = gen.text_to_video(
            prompt=prompt,
            model="sora-2",
            size="1280x720",
            duration=4 if name != "explainer-lymphatic" else 8,
            max_wait_time=600
        )
        out = f"/app/home-3d/mockups/{name}.mp4"
        gen.save_video(video_bytes, out)
        print(f"[{name}] OK -> {out}")
        return name, True
    except Exception as e:
        print(f"[{name}] ERR: {e}")
        return name, False


def main():
    start = time.time()
    with ThreadPoolExecutor(max_workers=7) as ex:
        results = list(ex.map(gen_one, VIDEOS))
    elapsed = time.time() - start
    print(f"\nTotal time: {elapsed:.1f}s")
    print(f"Results: {results}")


if __name__ == "__main__":
    main()
