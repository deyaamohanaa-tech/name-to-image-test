import os
import cairo
import gi

gi.require_version("Pango", "1.0")
gi.require_version("PangoCairo", "1.0")

from gi.repository import Pango, PangoCairo


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "sultan-nahia.ttf")
OUTPUT_PATH = os.path.join(BASE_DIR, "arabic_text.png")


def create_arabic_image(text):
    if not os.path.exists(FONT_PATH):
        raise FileNotFoundError(f"الخط غير موجود: {FONT_PATH}")

    WIDTH, HEIGHT = 1400, 400

    # إنشاء سطح Cairo
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    context = cairo.Context(surface)

    # خلفية بيضاء
    context.set_source_rgb(1, 1, 1)
    context.paint()

    # إنشاء Pango Layout
    layout = PangoCairo.create_layout(context)

    # تحميل الخط
    font_desc = Pango.FontDescription()
    font_desc.set_family("Cocon® Next Arabic")
    font_desc.set_size(50 * Pango.SCALE)

    layout.set_font_description(font_desc)

    # تعيين النص (Pango يتكفل بالعربي + bidi + shaping)
    layout.set_text(text, -1)

    # محاذاة
    layout.set_alignment(Pango.Alignment.LEFT)

    # حساب أبعاد النص
    ink_rect, logical_rect = layout.get_pixel_extents()

    x = 20
    y = (HEIGHT - logical_rect.height) // 2

    # تحريك المؤشر
    context.move_to(x, y)

    # رسم النص
    context.set_source_rgb(0, 0, 0)
    PangoCairo.show_layout(context, layout)

    # حفظ الصورة
    surface.write_to_png(OUTPUT_PATH)
    print("✔ تم حفظ الصورة في:", OUTPUT_PATH)


create_arabic_image(
    "🥰🥰 ᯓ𓆩𖡡𓏺.ضيـ꯭ــاء꯭ۦ٭||𝓓𝓮𝔂𝓪'𝓪.𓏺𖡡𓆪"
)
