from PIL import Image

def add_watermark(input_path, watermark_path, output_path, position=(0, 0)):
    # Otwieramy obraz wejściowy i konwertujemy go na RGBA (z kanałem alfa)
    image = Image.open(input_path).convert("RGBA")
    
    # Otwieramy znak wodny (watermark) i konwertujemy na RGBA
    watermark = Image.open(watermark_path).convert("RGBA")
    
    # Zmieniamy rozmiar znaku wodnego, żeby pasował do obrazka (np. na połowę rozmiaru)
    watermark = watermark.resize((image.width // 2, image.height // 2))
    
    # Nakładamy znak wodny na obraz w określonej pozycji, używając maski (przezroczystości)
    image.paste(watermark, position, mask=watermark.split()[3])  # Używamy czwartego kanału (alfa)

    # Zapisujemy wynikowy obraz jako PNG, ponieważ PNG obsługuje przezroczystość
    image.save(output_path, format="PNG")

# Przykład użycia
add_watermark("test2.png", "watermark.jpg", "waterkrowa.png")





