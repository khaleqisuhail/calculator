from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Resimlerin kaydedileceği klasör
os.makedirs('images', exist_ok=True)

# Sabit değerler
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 70
BUTTON_SPACING = 5
DISPLAY_HEIGHT = 100
MARGIN = 20
COLS = 4

# Resim boyutları
IMG_WIDTH = MARGIN * 2 + COLS * BUTTON_WIDTH + (COLS - 1) * BUTTON_SPACING
IMG_HEIGHT = MARGIN * 2 + DISPLAY_HEIGHT + BUTTON_SPACING + 5 * BUTTON_HEIGHT + 4 * BUTTON_SPACING

def create_calculator_image(filename, previous_text="", current_text=""):
    """Hesap makinesi görselini oluştur"""
    # Resim oluştur
    img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), color='white')
    draw = ImageDraw.Draw(img)
    
    # Gradient arka planı simüle et
    # Açık mavi renk: #00d0ff, Turuncu renk: #ff5e00
    for y in range(IMG_HEIGHT):
        ratio = y / IMG_HEIGHT
        # Mavi'dan Turuncu'ya geçiş
        r = int(0 + ratio * 255)
        g = int(208 - ratio * 100)
        b = int(255 * (1 - ratio))
        draw.line([(0, y), (IMG_WIDTH, y)], fill=(r, g, b))
    
    # Display kutusu
    display_x = MARGIN
    display_y = MARGIN
    display_width = IMG_WIDTH - 2 * MARGIN
    display_height = DISPLAY_HEIGHT
    
    # Display arka planı (koyu renkli)
    draw.rectangle(
        [display_x, display_y, display_x + display_width - 1, display_y + display_height - 1],
        fill=(80, 60, 60),
        outline='black',
        width=2
    )
    
    # Display metni
    try:
        font_small = ImageFont.truetype("arial.ttf", 16)
        font_large = ImageFont.truetype("arial.ttf", 28)
    except:
        font_small = ImageFont.load_default()
        font_large = ImageFont.load_default()
    
    # Önceki işlemi yaz
    if previous_text:
        draw.text(
            (display_x + 10, display_y + 10),
            previous_text,
            font=font_small,
            fill=(173, 216, 230)  # Açık mavi
        )
    
    # Mevcut sayıyı yaz
    current_display = current_text if current_text else "0"
    draw.text(
        (display_x + 10, display_y + 50),
        current_display,
        font=font_large,
        fill='white'
    )
    
    # Butonlar
    buttons = [
        [('AC', 2), ('DEL', 1), ('/', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('+', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('-', 1)],
        [('.', 1), ('0', 1), ('=', 2)]
    ]
    
    try:
        font_button = ImageFont.truetype("arial.ttf", 24)
    except:
        font_button = ImageFont.load_default()
    
    btn_y = display_y + display_height + BUTTON_SPACING
    
    for row in buttons:
        btn_x = MARGIN
        for button_text, span in row:
            width = span * BUTTON_WIDTH + (span - 1) * BUTTON_SPACING
            
            # Button arka planı
            draw.rectangle(
                [btn_x, btn_y, btn_x + width - 1, btn_y + BUTTON_HEIGHT - 1],
                fill=(255, 255, 255, 200),
                outline='black',
                width=1
            )
            
            # Button metni
            text_bbox = draw.textbbox((0, 0), button_text, font=font_button)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = btn_x + (width - text_width) // 2
            text_y = btn_y + (BUTTON_HEIGHT - text_height) // 2
            
            # Operasyon butonları farklı renk
            text_color = 'black'
            if button_text in ['+', '-', '*', '/', 'AC', 'DEL', '=']:
                text_color = '#333333'
            
            draw.text((text_x, text_y), button_text, font=font_button, fill=text_color)
            
            btn_x += width + BUTTON_SPACING
        
        btn_y += BUTTON_HEIGHT + BUTTON_SPACING
    
    img.save(filename)
    print(f"✅ {filename} oluşturuldu")

# 1. Boş durum
create_calculator_image('images/calculator_1_empty.png')

# 2. Sayı girişi (5 girişi)
create_calculator_image('images/calculator_2_number.png', current_text="5")

# 3. İşlem seçimi (5 + )
create_calculator_image('images/calculator_3_operation.png', previous_text="5  +", current_text="")

# 4. İkinci sayı (5 + 3)
create_calculator_image('images/calculator_4_calculation.png', previous_text="5  +", current_text="3")

# 5. Sonuç (= sonrası)
create_calculator_image('images/calculator_5_result.png', previous_text="", current_text="8")

print("\n✅ Tüm görsel resimleri başarıyla oluşturuldu!")
