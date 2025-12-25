from playwright.sync_api import sync_playwright
from PIL import Image
import io

NAME = "🥰🥰 ᯓ𓆩𖡡𓏺.ضيـ꯭ــاء꯭ۦ٭||𝓓𝓮𝔂𝓪'𝓪.𓏺𖡡𓆪"
OUTPUT = "arabic_text.png"

HTML = f"""
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0;
    width: 1400px;
    height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
  }}
  .name {{
    font-size: 60px;
    direction: rtl;
    unicode-bidi: plaintext;
    font-family:
      "Noto Sans Arabic",
      "Amiri",
      "DejaVu Sans",
      "Segoe UI Emoji",
      "Noto Color Emoji",
      sans-serif;
    white-space: nowrap;
  }}
</style>
</head>
<body>
  <div class="name">{NAME}</div>
</body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--single-process",
        ]
    )

    page = browser.new_page(
        viewport={"width": 1400, "height": 400}
    )

    page.set_content(HTML)
    page.wait_for_timeout(500)

    png_bytes = page.locator(".name").screenshot()
    browser.close()

img = Image.open(io.BytesIO(png_bytes))
img.save(OUTPUT)

print("✔ تم إنشاء الصورة بنجاح:", OUTPUT)
