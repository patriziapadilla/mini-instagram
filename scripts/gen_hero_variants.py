"""Generate 2 time-of-day variants of hero-dubai — SAME scene, different skies."""
import asyncio, os, base64
from dotenv import load_dotenv
from emergentintegrations.llm.chat import LlmChat, UserMessage

load_dotenv("/app/backend/.env")
api_key = os.getenv("EMERGENT_LLM_KEY")

BASE = """Cinematic editorial photograph for ultra-luxury Dubai penthouse spa website, warm royal-gentle champagne palette, 16:9 ultra-wide.

IDENTICAL COMPOSITION TO PREVIOUS FRAME (CRUCIAL):
The exact SAME penthouse room, SAME young elegant woman reclining on the SAME champagne-cream linen chaise lounge, SAME white plush spa bathrobe, SAME lipo laser pads with RED LED LIGHTS glowing on her abdomen, SAME antique brass vase with white peonies on the left, SAME cream French chair, SAME brass candle, SAME rolled towels, SAME ivory plaster walls with gold leaf, SAME travertine floor, SAME gauze cream drapes softly billowing, SAME floor-to-ceiling panoramic window on the RIGHT HALF showing the Dubai skyline with supertall skyscrapers piercing through a sea of clouds.
The camera position, lens (28mm wide), framing, model pose — EVERYTHING MUST BE PIXEL-IDENTICAL to the previous golden-hour frame.

ONLY CHANGE: THE SKY and LIGHT TEMPERATURE outside the window.
"""

VARIANTS = {
    "hero-dubai-sunset.png": """
SUNSET VARIANT:
Outside the window: the sky is a deep dramatic SUNSET — burning orange, rose-pink, coral, crimson gradient horizon, the sun a low glowing amber disc JUST ABOVE the sea of clouds (sun visibly descending, about to touch the cloud line).
The clouds are now painted in warm fiery tones: peach, coral, blush, gold.
The Dubai skyscrapers silhouette slightly darker, backlit by the sunset.
Interior: warm amber / rose light reflected inside the room, the gauze drapes glow peachy, candles appear a touch brighter, gold accents intensify. Model's skin has warm golden-pink kiss. The red LEDs on abdomen still active.
Mood: romantic, contemplative, end-of-day, warm embrace.
Palette: sunset orange #ff9066, coral #f4a078, rose #e88b8b, deep amber #d68a4a, champagne cream interior #f5e9d3 — NO blue, NO neon.
""",
    "hero-dubai-night.png": """
NIGHT + MOON VARIANT:
Outside the window: the sky is deep royal indigo-navy fading to inky black at top, with a LARGE LUMINOUS FULL MOON high in the sky casting silver-gold light. The sea of clouds below glows soft silvery-cream from the moonlight.
The Dubai skyscrapers sparkle with thousands of tiny warm golden window lights (city alive at night), their silhouettes defined against the night sky.
Interior: the room is now lit primarily by the warm gold candles, antique brass lamp casting amber glow, soft moonlight streaming in through the window creating silver highlights on the drapes and model's skin. The red LEDs on abdomen are the brightest accent, glowing more prominently.
Mood: intimate, luxurious, nocturnal ritual, quiet royal silence.
Palette: deep indigo #1a2a5c, navy #0d1a3a, moon silver #e8e6d8, warm candlelight gold #e8c789, cream interior #efe2cf, red LED accent. The interior STAYS warm cream (candlelit), only the sky/window view is cool-toned night.
"""
}

STYLE_TAIL = """
PHOTOGRAPHIC STYLE:
Hasselblad H6D, 28mm lens, f/4 deep focus, Kodak Portra 800, subtle analog grain, gentle vignette. Hyperrealistic photographic. NOT illustrative.

Absolutely NO text, NO logos, NO watermarks. ONE continuous photographic frame that tells the story: 'the same luxurious Dubai spa ritual, at a different hour of the day — the room breathes, the sky changes'.
"""

async def gen(name, variant_prompt):
    chat = LlmChat(
        api_key=api_key,
        session_id=f"droyal-hero-{name}",
        system_message="You are a master cinematic editorial photographer for Vogue Arabia, Architectural Digest Middle East, and Aman Resorts."
    )
    chat.with_model("gemini", "gemini-3.1-flash-image-preview").with_params(modalities=["image", "text"])
    prompt = BASE + variant_prompt + STYLE_TAIL
    msg = UserMessage(text=prompt)
    text, images = await chat.send_message_multimodal_response(msg)
    if images:
        out = f"/app/home-3d/mockups/{name}"
        with open(out, "wb") as f:
            f.write(base64.b64decode(images[0]["data"]))
        print(f"OK -> {out}")
    else:
        print(f"FAIL {name}: {(text or '')[:300]}")

async def main():
    await asyncio.gather(*[gen(n, p) for n, p in VARIANTS.items()])

asyncio.run(main())
