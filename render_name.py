from PIL import Image, ImageDraw, ImageFont
import cairosvg
import io

name = "𝑨𝒃𝒅𝒖𝒍𝒍𝒂𝒉 𝑨𝒍𝒔𝒂𝒍𝒂𝒎"

svg = f'''
<svg width="500" height="80" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="black"/>
  <text x="50%" y="50%"
        font-size="36"
        fill="white"
        text-anchor="middle"
        dominant-baseline="middle">
    {name}
  </text>
</svg>
'''

png = cairosvg.svg2png(bytestring=svg.encode())

img = Image.open(io.BytesIO(png))
img.save("name.png")

print("✔ تم إنشاء الصورة")
