"""Generate 5 transition images for D'Royal Spa cinematic scroll."""
import asyncio, os, base64
from dotenv import load_dotenv
from emergentintegrations.llm.chat import LlmChat, UserMessage

load_dotenv("/app/backend/.env")
api_key = os.getenv("EMERGENT_LLM_KEY")

PALETTE = """COLOR PALETTE: champagne #f5e9d3, ivory cream #ebd8b8, antique gold #c9a875, peach sunrise, warm cream tones.
NO black, NO harsh dark, NO neon. Only warm royal gentle palette.
PHOTOGRAPHIC STYLE: Hasselblad medium format, cinematic, Kodak Portra 800 film grain, hyperrealistic.
Wide ultra-wide 16:9 composition. Absolutely NO text, NO logos, NO watermarks."""

PROMPTS = [
    (
        "transition-1-balcony",
        f"""Cinematic editorial photograph: VIEW FROM INSIDE A LUXURY SPA SUITE LOOKING OUT THROUGH AN OPEN FRENCH DOOR onto a balcony with the Miami skyline beyond.
Foreground: cream linen drapes gently flowing in a soft breeze, framing the doorway, brass door handles, marble floor with hint of cream chaise lounge.
Middle: a beautiful private balcony with cream marble railing, white peony plant in antique brass pot, brass deck chair with cream cushion.
Background: the iconic MIAMI SKYLINE at golden midday — Brickell skyscrapers shimmering in warm golden sunlight, Biscayne Bay glimmering, palm trees swaying.
Sky: brilliant blue with soft golden haze, scattered cumulus clouds.
Composition: deep three-dimensional depth — the camera is INSIDE the spa, looking through to the outdoor sunlit world. The frame creates strong depth perception.
{PALETTE}
"""
    ),
    (
        "transition-2-clouds",
        f"""Cinematic surrealist editorial photograph: STANDING ABOVE THE CLOUDS, a SEA OF FLUFFY GOLDEN-CREAM CLOUDS extending infinitely to the horizon.
The viewer is at cloud-top level. The cloud surface is soft, undulating, shimmering with sunrise light.
In the FAR DISTANCE, only the very TOPS of MIAMI SKYSCRAPERS (Brickell modern glass towers) emerge from the clouds like islands rising from a celestial ocean.
Soft white peony petals floating in mid-air, suspended.
Sky: dreamy peach-cream-gold sunrise gradient, soft volumetric god-rays of light.
Atmosphere: divine, ethereal, Magritte surrealism meets Vogue editorial.
NO subject, NO person — pure atmospheric cloudscape with the city skyline tips visible.
{PALETTE}
"""
    ),
    (
        "transition-3-descending",
        f"""Cinematic aerial editorial photograph: CAMERA DESCENDING THROUGH THE CLOUDS INTO THE CITY BELOW.
View: the camera is dropping down through a thinning cloud layer. Above, soft golden clouds. 
Below, just visible through the parting cloud cover: the MIAMI city skyline (Brickell, Downtown), streets, palm trees, ocean.
The city is bathed in warm late-afternoon gold light filtering through the parting clouds.
Strong vertical movement sense, cloud wisps swirling around the frame edges as if the camera is moving down through them.
Some white peony petals drifting alongside the camera.
A few buildings catching golden sunlight.
NO subject, NO person — pure aerial transitional atmosphere.
{PALETTE}
"""
    ),
    (
        "transition-4-sunset-moon",
        f"""Cinematic editorial photograph: THE EXACT MOMENT OF SUNSET TRANSITIONING TO MOONRISE OVER THE MIAMI SKYLINE.
View: from a luxury spa balcony with cream marble railing in the foreground.
Background sky: a magical split — on the right, the SUN SETTING in warm pink-orange-gold over the ocean, casting long warm shadows on Miami skyscrapers. On the left, the MOON RISING — full luminous moon ascending into deep peach-violet sky studded with the first stars of evening.
The skyline (Miami Brickell) is silhouetted against this dramatic dual-light sky, building windows beginning to glow with warm amber lights as evening falls.
Palm trees in silhouette swaying.
Atmosphere: poetic, magical-realism, time-lapse moment frozen.
NO black, sky has warm gradient throughout (peach, pink, gold, soft violet — but never harsh dark).
{PALETTE.replace('NO black, NO harsh dark, NO neon. Only warm royal gentle palette.', '')}
COLOR PALETTE: warm peach, pink, gold, soft violet, cream, with hints of dusty rose. NO neon, NO harsh blue.
"""
    ),
    (
        "transition-5-night",
        f"""Cinematic editorial photograph: THE LUXURY MIAMI SKYLINE AT NIGHT, viewed from a high-rise balcony.
Foreground: cream marble balcony railing, white peony plant in brass pot.
Background: stunning MIAMI BRICKELL SKYLINE GLOWING WITH THOUSANDS OF WARM AMBER LIGHTS in every skyscraper window. Biscayne Bay reflecting the city lights like liquid gold.
A luminous FULL MOON in the sky casting silver-cream light. Stars subtly visible.
Soft warm haze in the air.
Atmosphere: opulent, glamorous, Miami at its most luxurious.
Sky: soft dusty navy-violet (NEVER black), glowing with the city's warm light.
The whole image has a warm cream/gold/cream-violet palette — even the night sky is WARM, not cold.
NO neon harsh colors, all lights are warm amber/gold tones reflecting the spa's elegance.
{PALETTE.replace('NO black, NO harsh dark, NO neon. Only warm royal gentle palette.', '')}
COLOR PALETTE: warm cream, antique gold building lights, dusty violet sky, peach moonglow. NO harsh blue, NO neon.
"""
    ),
]

async def gen_one(name: str, prompt: str) -> str:
    chat = LlmChat(
        api_key=api_key, session_id=f"droyal-{name}",
        system_message="You are a master cinematic editorial photographer specializing in luxury beauty, Miami architecture, surrealist landscape, and atmospheric transitional imagery in the style of Tim Walker, Steven Klein, and David LaChapelle."
    )
    chat.with_model("gemini", "gemini-3.1-flash-image-preview").with_params(modalities=["image", "text"])
    msg = UserMessage(text=prompt)
    text, images = await chat.send_message_multimodal_response(msg)
    if not images:
        return f"FAIL {name}: {(text or '')[:120]}"
    out = f"/app/home-3d/mockups/{name}.png"
    with open(out, "wb") as f:
        f.write(base64.b64decode(images[0]["data"]))
    return f"OK {name}"


async def main():
    results = await asyncio.gather(*[gen_one(n, p) for n, p in PROMPTS])
    for r in results:
        print(r)


asyncio.run(main())
