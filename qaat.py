from PIL import Image, ImageDraw, ImageFont
from pilmoji import Pilmoji
import arabic_reshaper
from bidi.algorithm import get_display
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FONT_PATH = os.path.join(BASE_DIR, "sultan-nahia.ttf")
OUTPUT_PATH = os.path.join(BASE_DIR, "arabic_text.png")


def create_arabic_image(text):
    if not os.path.exists(FONT_PATH):
        raise FileNotFoundError(f"الخط غير موجود: {FONT_PATH}")

    img = Image.new("RGB", (1400, 400), "white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONT_PATH, 50)

    # تشكيل النص العربي
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)

    x = 20
    y = (400 - 50) // 2

    # رسم النص دفعة واحدة
    with Pilmoji(img) as pilmoji:
        pilmoji.text((x, y), bidi_text, font=font, fill="black")

    img.save(OUTPUT_PATH)
    print("تم حفظ الصورة في:", OUTPUT_PATH)


create_arabic_image("🥰🥰 ᯓ𓆩𖡡𓏺.ضيـ꯭ــاء꯭ۦ٭||𝓓𝓮𝔂𝓪'𝓪.𓏺𖡡𓆪")
