from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import io

# ===== اسم المستخدم المزخرف =====
name = "ضيـ꯭ــاء꯭ۦ٭||𝓓𝓮𝔂𝓪.𓏺"

# ===== HTML بسيط =====
html_content = f"""
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body {{
        margin: 0;
        padding: 0;
        background: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
      }}
      .name {{
        font-size: 50px;
        font-family: 'DejaVu Sans', 'Amiri', 'Noto Sans', sans-serif;
        color: black;
      }}
    </style>
  </head>
  <body>
    <div class="name">{name}</div>
  </body>
</html>
"""

# ===== إعداد Chrome Headless =====
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1000,150")

# إذا كنت تستخدم ChromeDriver في مسار خاص، عدّل هذا
driver = webdriver.Chrome(options=chrome_options)

# إنشاء ملف HTML مؤقت
with open("temp_name.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# فتح HTML
driver.get("file://" + "/full/path/to/temp_name.html")  # ضع المسار الكامل هنا
time.sleep(1)  # انتظر التحميل

# التقاط الشاشة
element = driver.find_element("css selector", ".name")
png = element.screenshot_as_png

# حفظ الصورة
img = Image.open(io.BytesIO(png))
img.save("name.png")
print("✔ تم إنشاء name.png بنجاح")

driver.quit()
