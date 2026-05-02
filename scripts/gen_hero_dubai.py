"""Hero DUBAI — penthouse window open over sea of clouds + skyscrapers."""
import asyncio, os, base64
from dotenv import load_dotenv
from emergentintegrations.llm.chat import LlmChat, UserMessage

load_dotenv("/app/backend/.env")
api_key = os.getenv("EMERGENT_LLM_KEY")

PROMPT = """Cinematic editorial photograph for ultra-luxury Dubai penthouse spa website hero, warm royal-gentle champagne palette, 16:9 ultra-wide.

SCENE — ONE FRAME, NO COMPOSITING:
A young elegant woman with glowing skin reclines gracefully on a champagne-cream linen chaise lounge INSIDE a sky-high Dubai penthouse suite. She wears a pristine WHITE PLUSH SPA BATHROBE, monogrammed luxury hotel terry cloth, open over her abdomen.
On her toned abdomen: flat rectangular LIPO LASER PADS with BRIGHT RED LED LIGHTS GLOWING actively — visible red laser dots, medical-aesthetic device in session. Soft beige fabric strap. Gentle red LED reflections on skin.
Her head rests on a silk pillow, eyes gently closed, serene.

COMPOSITION — CRUCIAL:
The entire RIGHT HALF of the frame is a MASSIVE FLOOR-TO-CEILING PANORAMIC WINDOW, open wide, gauze cream drapes softly billowing inward. The window frames a BREATHTAKING DUBAI SKYLINE AT SEA OF CLOUDS HEIGHT:
- The tops of ultra-modern Dubai supertall skyscrapers (Burj Khalifa silhouette, Cayan Tower, Princess Tower, Marina 101) piercing UP through a dense sea of soft cream-gold clouds
- We are clearly ABOVE the clouds — the clouds form a horizontal ocean layer at mid-window height
- Warm golden-hour light, peach and champagne tones in the sky, sun low behind clouds
- Distance hazy, atmospheric, dreamlike
The window is the STAR of the composition — it must take 50% of the canvas.

LEFT THIRD — INTERIOR:
Warm ivory plaster wall with subtle gold leaf detail, pale travertine marble floor, antique brass vase with fresh white peonies, a brass tray with rolled white towels, a golden candle, an ornate cream upholstered French chair slightly visible. Soft negative space for headline text overlay.

CAMERA PERSPECTIVE — CRUCIAL:
Wide-angle 28mm cinematic shot, camera positioned INSIDE the room, ~4 meters back from the window, slightly above eye level. The viewer feels like they are standing in the room gazing past the model toward the breathtaking view. This wide perspective MUST support a later digital zoom-in toward the window (i.e. the window must be sharp and detailed so zooming in still looks premium).

LIGHTING:
Soft warm golden-hour light streams IN through the window from the clouds/skyline outside, backlighting the model and making the drapes glow translucent. Warm gold accent lamp inside top-left. Cream ambient light, champagne tones throughout, NO harsh shadows.

COLOR PALETTE (strict):
Champagne #f5e9d3, ivory cream #ebd8b8, warm tan #d9c4a0, antique gold #c9a875, peach-cream sky #f2d9b0, soft cloud pink #e8c6a0, espresso #5c4a3a, red LED on pads.
NO black backgrounds, NO blue, NO purple, NO neon, NO cold tones.

PHOTOGRAPHIC STYLE:
Hasselblad H6D, 28mm lens, f/4 for deep focus (both the interior AND the skyline sharp), ISO 200, Kodak Portra 800 aesthetic, subtle analog grain, gentle vignette. Hyperrealistic. NOT illustrative.

REFERENCE:
Architectural Digest Dubai penthouse feature + Vogue Arabia editorial + Aman spa brochure + Burj Al Arab royal suite imagery + Christopher Nolan Tenet "penthouse above clouds" frames.

Absolutely NO text, NO logos, NO typography, NO watermarks.
One continuous photographic frame that tells the story: 'an in-home luxury lipo laser ritual floating above the clouds of Dubai at golden hour'.
"""

async def main():
    chat = LlmChat(
        api_key=api_key,
        session_id="droyal-hero-dubai-v1",
        system_message="You are a master cinematic editorial photographer for Vogue Arabia, Architectural Digest Middle East, Aman Resorts, and ultra-luxury skyscraper residential brochures (Burj Al Arab, Palazzo Versace, One Za'abeel)."
    )
    chat.with_model("gemini", "gemini-3.1-flash-image-preview").with_params(modalities=["image", "text"])
    msg = UserMessage(text=PROMPT)
    text, images = await chat.send_message_multimodal_response(msg)
    if images:
        out = "/app/home-3d/mockups/hero-dubai.png"
        with open(out, "wb") as f:
            f.write(base64.b64decode(images[0]["data"]))
        print(f"OK -> {out}")
    else:
        print(f"FAIL: {(text or '')[:400]}")

asyncio.run(main())
