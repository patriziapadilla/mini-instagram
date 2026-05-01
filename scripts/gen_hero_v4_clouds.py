"""Hero v4 — Royal Clouds: woman floating above Miami skyline in clouds with lipo treatment."""
import asyncio, os, base64
from dotenv import load_dotenv
from emergentintegrations.llm.chat import LlmChat, UserMessage

load_dotenv("/app/backend/.env")
api_key = os.getenv("EMERGENT_LLM_KEY")

PROMPT = """Cinematic surrealist editorial photograph for D'Royal Spa luxury Miami beauty brand HERO.
Wide ultra-wide 16:9 composition with deep negative space on the LEFT for headline text overlay.
Concept: "ROYAL CLOUDS" — divinity above the city, beauty queen aesthetic, Magritte surrealism meets Vogue Beauty.

CENTRAL SCENE (right two-thirds of frame):
A young elegant ethereal woman with smooth glowing skin, peaceful serene expression, eyes gently closed,
reclining gracefully on a CHAISE LONGUE made of soft fluffy white clouds floating in mid-air.
She wears a pristine WHITE LUXURY MONOGRAMMED 'D'ROYAL SPA' BATHROBE 
(thick cotton terry, gold DR monogram embroidery on chest) gently flowing in subtle wind.
Her abdomen is exposed showing LIPO LASER PADS in active session:
multiple flat rectangular medical lipo laser pads with BRIGHT RED LED LIGHTS GLOWING and 
ACTIVELY emitting visible red laser dots on her toned abdomen. Premium beige fabric strap secures the pads.
Subtle red glow from the LEDs reflecting on the surrounding clouds creating a magical effect.

SURREAL CLOUDSCAPE BACKGROUND (most important):
She floats above an ENDLESS SEA OF GOLDEN-CREAM CLOUDS at sunrise/golden hour.
In the distance behind her, the iconic MIAMI SKYLINE (Brickell skyscrapers, modern glass buildings) 
emerges DRAMATICALLY through the cloud cover — only the upper portions of skyscrapers visible above the clouds,
like islands rising from a celestial ocean.
Soft pink, peach and gold sky gradient at sunrise, warm sun glow at horizon.
A few delicate cloud wisps float around her at her level, drifting gently.
White peony petals floating in the air around her, suspended in the breeze (Magritte surrealism).
The atmosphere is ethereal, divine, dreamy, like a renaissance painting of a goddess on Olympus
crossed with a Vogue Beauty editorial.

LIGHTING:
Warm golden sunrise light from the upper right horizon casting soft amber glow on her body and the clouds.
Volumetric god-rays cutting through the cloud cover.
Bright soft cinematic lighting, NOT dark, NOT moody — bright divine atmosphere.
The red LEDs from her lipo pads add a subtle warm accent.

COLOR PALETTE:
Soft champagne #f5e9d3, ivory cream #ebd8b8, warm tan #d9c4a0, antique gold #c9a875,
peachy sunrise glow, pink peony accents, cream cloud whites,
warm cream skin tones. Subtle navy-gold of the distant skyline.
Bright warm divine atmosphere. NO black. NO harsh dark. NO cool blue tones.
Only warm royal gentle palette + sunrise gold/peach.

PHOTOGRAPHIC STYLE:
Hasselblad medium format, 85mm lens, f/2.8 shallow depth of field, ISO 200,
Kodak Portra 800 film stock aesthetic, subtle vignette, fine analog grain,
sharp focus on her face and the lipo pads with red LEDs,
dreamy soft bokeh on cloudscape and distant skyline.

REFERENCE AESTHETIC:
Magritte "Castle in the Pyrenees" surrealism, Versace beauty queen campaigns, 
Tom Ford perfume divine ads, Vogue editorial "above the clouds",
Ridley Scott commercial cinematography, Renaissance goddess paintings in modern beauty context.
Hyperrealistic photographic with surreal magical-realism element.
NOT cartoonish, NOT 3D-rendered, NOT illustration — must look like an actual photograph 
of someone really floating in the clouds (achieved via sophisticated photography/practical effects).

Absolutely NO text, NO logos visible (subtle DR monogram on robe is fine), NO watermarks, NO captions.
Pure cinematic surreal photographic atmosphere — a beauty queen receiving D'Royal Spa lipo laser ritual 
floating divinely above the Miami skyline at golden hour.
"""

async def main():
    chat = LlmChat(
        api_key=api_key,
        session_id="droyal-hero-v4-clouds",
        system_message="You are a master cinematic surrealist editorial photographer specializing in luxury beauty campaigns combining magical realism with Vogue editorial style, in the tradition of Tim Walker, Steven Klein, and Annie Leibovitz."
    )
    chat.with_model("gemini", "gemini-3.1-flash-image-preview").with_params(modalities=["image", "text"])
    msg = UserMessage(text=PROMPT)
    text, images = await chat.send_message_multimodal_response(msg)
    if images:
        out = "/app/home-3d/mockups/hero-v4-clouds.png"
        with open(out, "wb") as f:
            f.write(base64.b64decode(images[0]["data"]))
        print(f"OK -> {out}")
    else:
        print(f"FAIL: {(text or '')[:200]}")

asyncio.run(main())
