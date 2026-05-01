"""Generate 4 remaining D'Royal Spa cinematic images, royal gentle palette."""
import asyncio, os, base64
from dotenv import load_dotenv
from emergentintegrations.llm.chat import LlmChat, UserMessage

load_dotenv("/app/backend/.env")
api_key = os.getenv("EMERGENT_LLM_KEY")

BASE_PALETTE = """
COLOR PALETTE (royal gentle, NO black, NO harsh dark):
Soft champagne #f5e9d3, ivory cream #ebd8b8, warm tan #d9c4a0, antique gold #c9a875,
dusty rose accents #c2a39a, soft espresso #5c4a3a for darkest tones (NOT pure black).
Bright warm cream atmosphere, NOT dark.
NO blue, NO purple, NO neon, NO cool tones, NO pure black.

PHOTOGRAPHIC STYLE:
Hasselblad medium format 80mm f/2.8, ISO 200, Kodak Portra 400 film stock,
subtle vignette, fine analog grain, sharp focus on subject, creamy bokeh.

REFERENCE AESTHETIC:
Vogue Living, Architectural Digest spa feature, Aman Resorts brochure,
Loro Piana cashmere ad, Le Sirenuse Capri editorial, Hermès skincare campaign.
Hyperrealistic photographic, NOT illustrative, NOT 3D-rendered.

SETTING (consistent across all images):
A bright airy luxury private spa suite in soft champagne and ivory cream tones.
Warm ivory plaster walls, pale travertine marble floor, cream linen drapes filtering soft daylight,
fresh white peonies in antique brass vase, brass tray with rolled white towels, golden candlelight,
ornate cream upholstered French chair, gilt-framed mirror, hint of vintage gold leaf detail.

LIGHTING:
Soft natural cream daylight from a left side window, warm golden lamp accent from upper right.
Bright but gentle, no harsh shadows.

The subject MUST wear a pristine WHITE LUXURY MONOGRAMMED 'D'ROYAL SPA' BATHROBE 
(thick cotton terry, long sleeves, gold monogram embroidery on chest), open over the treatment area.

Wide ultra-wide 16:9 composition with deep negative space on the LEFT for headline text overlay.
Subject positioned in right two-thirds of frame.

Absolutely NO text in image, NO logos visible (except subtle DR monogram on robe), NO typography, 
NO watermarks, NO captions. Pure cinematic photographic atmosphere.
"""

PROMPTS = [
    (
        "treatment-lipo",
        """Cinematic editorial photo for D'Royal Spa LIPO CON LÁSER section.
Subject: a young elegant woman with smooth glowing skin reclining on a champagne linen chaise lounge,
gentle peaceful smile, eyes half-closed in serene relaxation.
She wears the white monogrammed D'Royal Spa bathrobe open to expose her toned abdomen.
Multiple LIPO LASER PADS placed across her abdomen and waist with BRIGHT RED LED LIGHTS GLOWING and
ACTIVELY emitting visible red laser dots. Premium soft beige fabric strap securing the pads gently.
Subtle red glow from LEDs reflecting on her skin showing the device is ACTIVE.
Camera angle: medium-close shot, her face and abdomen both clearly in frame.
Focus is on the ACTIVE TREATMENT PADS with red LEDs being clearly visible and dramatic.
""" + BASE_PALETTE
    ),
    (
        "treatment-aumentos",
        """Cinematic editorial photo for D'Royal Spa AUMENTOS SIN CIRUGÍA CON LÁSER (vacuum therapy for breast and glute enhancement) section.
Subject: a young elegant woman lying face-down on a luxury cream linen massage table,
back arched gracefully, eyes closed in serene relaxation, peaceful smile.
She wears the white monogrammed D'Royal Spa bathrobe lowered to expose her bare shoulders and back area, 
draped tastefully over her hips and lower body for modesty.
On her glute/lower back area, multiple GLASS VACUUM CUPS / SUCTION CUPS in clear glass with brass rims,
gently lifted by suction (cellulite cupping vacuum therapy aesthetic),
2-3 cups visible attached to her glute area, premium brass tubes connecting them to a sleek elegant 
gold-and-cream electronic vacuum device on a side brass tray.
Camera angle: side-overhead view showing her relaxed face AND the cups.
Focus on the cups gently sculpting/lifting the area.
NO nudity, modest tasteful editorial framing, like a Vogue Beauty magazine spread.
""" + BASE_PALETTE
    ),
    (
        "treatment-botox-laser",
        """Cinematic editorial photo for D'Royal Spa BOTOX CON LÁSER section (NEW non-needle laser+RF technology for facial rejuvenation).
Subject: a young elegant woman lying back on a cream linen spa table,
head resting on a soft cream pillow, eyes gently closed in serene relaxation.
She wears the white monogrammed D'Royal Spa bathrobe.
A handheld GOLD-AND-WHITE elegant laser facial wand (sleek modern device with glowing AMBER GOLDEN LIGHT at the tip)
is held by gloved professional hands hovering close to her cheek/forehead, emitting a soft warm GOLDEN LASER GLOW
that bathes her face in beautiful amber light.
NO needles, NO syringes, NO injections — emphasize the NON-INVASIVE laser treatment.
Visible warm golden light beam from the wand creating dreamy volumetric glow on her perfect glowing skin.
Camera angle: close-up beauty shot, her face and the laser wand both in frame.
Focus: the dramatic warm golden laser light treating her skin.
""" + BASE_PALETTE
    ),
    (
        "treatment-results",
        """Cinematic editorial photo for D'Royal Spa RESULTADOS REALES (real before/after results) section.
Subject: a young elegant woman with gorgeous toned sculpted body, standing in a confident graceful pose,
hands gently on her hips, eyes looking off-camera with serene confident expression, peaceful smile.
She wears a beautifully draped silk-cream lingerie set or seamless beige tank-and-shorts athleisure
(modest tasteful editorial, NOT lingerie underwear, like Vogue Body editorial),
showing off her sculpted abdomen, slim waist, toned arms and legs, lifted glutes naturally curving.
She stands in profile/three-quarter pose against the cream royal-gentle spa interior.
The lighting beautifully sculpts every contour of her body, showing the perfect natural sculpted results.
Camera angle: full body editorial shot, like a fitness magazine cover.
Focus: her complete sculpted figure in beautiful natural light.
She looks like an aspirational client AFTER completing D'Royal Spa treatments.
""" + BASE_PALETTE
    ),
]

async def gen_one(name: str, prompt: str) -> str:
    chat = LlmChat(
        api_key=api_key,
        session_id=f"droyal-{name}",
        system_message="You are a master cinematic editorial photographer specializing in luxury beauty, aesthetic medicine, spa imagery for Vogue Beauty, Harper's Bazaar, Aman Resorts, Loro Piana, Hermès skincare campaigns."
    )
    chat.with_model("gemini", "gemini-3.1-flash-image-preview").with_params(modalities=["image", "text"])
    msg = UserMessage(text=prompt)
    text, images = await chat.send_message_multimodal_response(msg)
    if not images:
        return f"FAIL {name}: {(text or '')[:150]}"
    out = f"/app/home-3d/mockups/{name}.png"
    with open(out, "wb") as f:
        f.write(base64.b64decode(images[0]["data"]))
    return f"OK {name} -> {out}"


async def main():
    results = await asyncio.gather(*[gen_one(n, p) for n, p in PROMPTS])
    for r in results:
        print(r)


asyncio.run(main())
