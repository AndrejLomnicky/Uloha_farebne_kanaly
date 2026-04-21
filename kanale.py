from PIL import Image

# 1. Otvoríme súbor s obrázkom
img = Image.open("priroda.jpg")

# 2. Rozdelíme RGB obrázok na tri samostatné farebné zložky (kanály)
# Premenné r, g, b teraz obsahujú čiernobiele verzie (režim "L")
# intenzity každej farby.
r, g, b = img.split()

# 3. Vytvoríme nový obrázok, ktorý bude obsahovať iba červenú zložku
# Image.new("L", img.size) vytvorí úplne čierne "plátno" (nulovú intenzitu)
# Image.merge spojí: pôvodnú červenú + čiernu (namiesto G) + čiernu (namiesto B)
red_img = Image.merge("RGB", (r, Image.new("L", img.size), Image.new("L", img.size)))

# 4. To isté urobíme pre zelenú (červená a modrá budú čierne)
green_img = Image.merge("RGB", (Image.new("L", img.size), g, Image.new("L", img.size)))

# 5. A pre modrú (červená a zelená budú čierne)
blue_img = Image.merge("RGB", (Image.new("L", img.size), Image.new("L", img.size), b))

# 6. Zobrazenie výsledných jednofarebných obrázkov
red_img.show()
green_img.show()
blue_img.show()