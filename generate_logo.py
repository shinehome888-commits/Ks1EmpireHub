from PIL import Image, ImageDraw, ImageFont
import os

# ------------------- CONFIG -------------------
WIDTH, HEIGHT = 512, 512
BACKGROUND_COLOR = (0, 0, 0)        # Black
CROWN_COLOR = (212, 175, 55)       # Gold: #D4AF37
FLAME_COLOR = (211, 47, 47)        # Red: #D32F2F
TEXT_COLOR = (255, 255, 255)       # White
FONT_SIZE = 120

# ------------------- CREATE IMAGE -------------------
img = Image.new("RGBA", (WIDTH, HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(img)

# ------------------- LOAD FONT (OR USE DEFAULT) -------------------
try:
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
except IOError:
    font = ImageFont.load_default()

# ------------------- DRAW FLAME (TOP CENTER) -------------------
flame_points = [
    (WIDTH//2 - 30, 100),
    (WIDTH//2 - 20, 60),
    (WIDTH//2 + 20, 60),
    (WIDTH//2 + 30, 100),
    (WIDTH//2 + 25, 140),
    (WIDTH//2 + 15, 180),
    (WIDTH//2, 210),
    (WIDTH//2 - 15, 180),
    (WIDTH//2 - 25, 140),
]
draw.polygon(flame_points, fill=FLAME_COLOR)

# ------------------- DRAW CROWN (BELOW FLAME) -------------------
crown_base_y = 220
crown_width = 180
crown_height = 40
crown_teeth = 5

for i in range(crown_teeth):
    x = WIDTH//2 - crown_width//2 + i * (crown_width // (crown_teeth - 1))
    # Crown tooth
    draw.polygon([
        (x, crown_base_y),
        (x + 10, crown_base_y - 20),
        (x + 20, crown_base_y),
    ], fill=CROWN_COLOR)
    # Crown base
    draw.rectangle([x - 5, crown_base_y, x + 25, crown_base_y + crown_height], fill=CROWN_COLOR)

# ------------------- DRAW "KS1" TEXT (CENTERED) -------------------
text = "KS1"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (WIDTH - text_width) // 2
text_y = crown_base_y + crown_height + 30

draw.text((text_x, text_y), text, fill=TEXT_COLOR, font=font)

# ------------------- SAVE AS PNG (TRANSPARENT BG) -------------------
img.save("logo.png", "PNG")

print("✅ Logo generated: logo.png")
print("✅ Colors: Gold Crown, Red Flame, White Text on Black")
print("✅ Ready to upload to GitHub for KS1 Empire Hub!")
