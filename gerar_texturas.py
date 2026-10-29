from PIL import Image, ImageDraw
import os

base_item = "C:/Users/mklar/zombieapocalypse/src/main/resources/assets/zombieapocalypse/textures/item"
base_entity = "C:/Users/mklar/zombieapocalypse/src/main/resources/assets/zombieapocalypse/textures/entity"

MARROM = (101, 67, 33)
MARROM_ESCURO = (70, 45, 20)
CINZA = (128, 128, 128)
CINZA_ESCURO = (64, 64, 64)
VERMELHO = (200, 0, 0)
VERDE = (0, 150, 0)
AZUL = (0, 100, 200)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE_DOENTE = (100, 150, 50)
VERMELHO_SANGUE = (150, 0, 0)
ROSA_DOENTE = (180, 140, 140)
PELE_MORTA = (140, 130, 120)
PELE_MORTA_ESCURO = (100, 90, 80)
MARROM_SUJO = (110, 90, 70)

def salvar_item(nome, img):
    caminho = os.path.join(base_item, nome)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    img.save(caminho, "PNG")
    print("Salvo item: " + nome)

def salvar_entidade(nome, img):
    caminho = os.path.join(base_entity, nome)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    img.save(caminho, "PNG")
    print("Salvo entidade: " + nome)

def sombra_canto(img, d, cor_sombra, margem=3):
    """Adiciona sombreado nas bordas para dar relevo (pixel art simples)."""
    w, h = img.size
    for i in range(margem):
        alpha = 255 - int((i / margem) * 200)
        cor = (cor_sombra[0], cor_sombra[1], cor_sombra[2], alpha)
        d.line([i, i, w - 1 - i, i], fill=cor)
        d.line([i, i, i, h - 1 - i], fill=cor)
        d.line([w - 1 - i, i, w - 1 - i, h - 1 - i], fill=cor_sombra)
        d.line([i, h - 1 - i, w - 1 - i, h - 1 - i], fill=cor_sombra)

# ===== ITENS =====

# nail_bat - Taco com pregos
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([14, 12, 18, 32], fill=MARROM)
d.rectangle([10, 8, 22, 16], fill=MARROM_ESCURO)
d.rectangle([11, 10, 13, 12], fill=CINZA)
d.rectangle([19, 10, 21, 12], fill=CINZA)
d.rectangle([11, 14, 13, 16], fill=CINZA)
d.rectangle([19, 14, 21, 16], fill=CINZA)
salvar_item("nail_bat.png", img)

# medical_kit - Kit médico branco com cruz vermelha
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([4, 4, 28, 28], fill=BRANCO, outline=CINZA_ESCURO)
d.rectangle([14, 6, 18, 26], fill=VERMELHO)
d.rectangle([6, 14, 26, 18], fill=VERMELHO)
salvar_item("medical_kit.png", img)

# smoke_grenade - Granada de fumaça cinza
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.ellipse([8, 8, 24, 24], fill=CINZA_ESCURO, outline=CINZA)
d.rectangle([14, 6, 18, 10], fill=VERMELHO)
d.rectangle([15, 24, 17, 28], fill=CINZA_ESCURO)
salvar_item("smoke_grenade.png", img)

# zombie_detector - Detetor cinza com tela verde
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([6, 6, 26, 26], fill=CINZA)
d.rectangle([8, 8, 24, 20], fill=(0, 200, 0))
d.rectangle([12, 20, 20, 24], fill=CINZA_ESCURO)
salvar_item("zombie_detector.png", img)

# zombie_bait - Isca verde com cérebro
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.ellipse([10, 8, 22, 20], fill=VERDE_DOENTE)
d.rectangle([14, 20, 18, 28], fill=MARROM)
d.arc([12, 10, 20, 18], 0, 180, fill=CINZA_ESCURO, width=2)
salvar_item("zombie_bait.png", img)

# canned_food - Lata enlatada prata
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([10, 8, 22, 28], fill=(200, 200, 200), outline=CINZA_ESCURO)
d.rectangle([10, 6, 22, 10], fill=CINZA_ESCURO)
d.rectangle([12, 12, 20, 16], fill=VERMELHO)
salvar_item("canned_food.png", img)

# bandage - Bandagem branca
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.ellipse([8, 8, 24, 24], fill=BRANCO, outline=CINZA_ESCURO)
d.line([8, 16, 24, 16], fill=CINZA_ESCURO, width=2)
d.line([16, 8, 16, 24], fill=CINZA_ESCURO, width=2)
salvar_item("bandage.png", img)

# antidote - Frasco azul com líquido verde
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([12, 10, 20, 26], fill=AZUL, outline=CINZA_ESCURO)
d.rectangle([13, 12, 19, 22], fill=VERDE)
d.rectangle([14, 6, 18, 10], fill=CINZA)
salvar_item("antidote.png", img)

# riot_plate - Placa metálica cinza
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([8, 6, 24, 26], fill=(180, 180, 180), outline=CINZA_ESCURO)
d.line([12, 10, 20, 10], fill=CINZA_ESCURO, width=2)
d.line([12, 14, 20, 14], fill=CINZA_ESCURO, width=2)
salvar_item("riot_plate.png", img)

# riot_helmet - Capacete cinza
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.ellipse([10, 6, 22, 18], fill=(160, 160, 160), outline=CINZA_ESCURO)
d.rectangle([12, 16, 20, 28], fill=(160, 160, 160), outline=CINZA_ESCURO)
salvar_item("riot_helmet.png", img)

# riot_chestplate - Peitoral cinza
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([8, 8, 24, 26], fill=(160, 160, 160), outline=CINZA_ESCURO)
d.rectangle([10, 12, 22, 20], fill=(140, 140, 140))
salvar_item("riot_chestplate.png", img)

# riot_leggings - Calças cinza
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([10, 8, 16, 28], fill=(160, 160, 160), outline=CINZA_ESCURO)
d.rectangle([16, 8, 22, 28], fill=(160, 160, 160), outline=CINZA_ESCURO)
salvar_item("riot_leggings.png", img)

# riot_boots - Botas cinza
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([10, 20, 16, 32], fill=(140, 140, 140), outline=CINZA_ESCURO)
d.rectangle([16, 20, 22, 32], fill=(140, 140, 140), outline=CINZA_ESCURO)
salvar_item("riot_boots.png", img)

# ===== TEXTURAS DE ENTIDADES (64x64) =====

def textura_zumbi(cor_base, cor_cabeca, cor_corpo, mancha_sangue=False):
    img = Image.new("RGBA", (64, 64), (0,0,0,0))
    d = ImageDraw.Draw(img)
    # Fundo transparente
    # Cabeça (mapeamento padrão do zombie 64x64: 8,8,56,32)
    d.rectangle([8, 8, 56, 32], fill=cor_cabeca)
    # Sombreado da cabeça (relevo)
    d.rectangle([8, 8, 56, 16], fill=(max(0, cor_cabeca[0]-20), max(0, cor_cabeca[1]-20), max(0, cor_cabeca[2]-20)))
    # Olhos (escuros)
    d.rectangle([16, 18, 24, 24], fill=PRETO)
    d.rectangle([40, 18, 48, 24], fill=PRETO)
    # Boca
    d.rectangle([28, 26, 36, 30], fill=PRETO)
    # Corpo (16,32,48,56)
    d.rectangle([16, 32, 48, 56], fill=cor_corpo)
    d.rectangle([16, 32, 48, 40], fill=(max(0, cor_corpo[0]-25), max(0, cor_corpo[1]-25), max(0, cor_corpo[2]-25)))
    # Pernas
    d.rectangle([16, 56, 24, 64], fill=cor_corpo)
    d.rectangle([40, 56, 48, 64], fill=cor_corpo)
    # Braços
    d.rectangle([0, 32, 16, 56], fill=cor_corpo)
    d.rectangle([48, 32, 64, 56], fill=cor_corpo)
    # Roupas rasgadas / detalhes sujos
    d.line([16, 32, 48, 32], fill=CINZA_ESCURO, width=1)
    d.line([16, 56, 24, 56], fill=CINZA_ESCURO, width=1)
    d.line([40, 56, 48, 56], fill=CINZA_ESCURO, width=1)
    if mancha_sangue:
        d.rectangle([20, 36, 30, 42], fill=VERMELHO_SANGUE)
        d.rectangle([38, 38, 46, 44], fill=VERMELHO_SANGUE)
        d.rectangle([12, 14, 20, 18], fill=VERMELHO_SANGUE)
    return img

# zombie_runner - cinza verde claro (mais rápido)
salvar_entidade("zombie_runner.png", textura_zumbi((100, 100, 80), (80, 80, 60), (90, 90, 70)))

# zombie_tank - cinza marrom escuro (mais resistente)
salvar_entidade("zombie_tank.png", textura_zumbi((90, 75, 60), (70, 55, 40), (80, 65, 50)))

# zombie_infected - verde doente (aplica infecção)
salvar_entidade("zombie_infected.png", textura_zumbi((120, 150, 80), (100, 130, 60), (110, 140, 70)))

# zombie_night - azul escuro (mais perigoso à noite)
salvar_entidade("zombie_night.png", textura_zumbi((60, 60, 100), (40, 40, 80), (50, 50, 90)))

# zombie_destroyer - cinza sujo (quebra blocos)
salvar_entidade("zombie_destroyer.png", textura_zumbi((100, 90, 80), (80, 70, 60), (90, 80, 70)))

# zombie_explosive - vermelho sangue (explode ao morrer) — com manchas de sangue
salvar_entidade("zombie_explosive.png", textura_zumbi((150, 50, 40), (130, 30, 20), (140, 40, 30), mancha_sangue=True))

# zombie_archer - verde oliva (ataca à distância)
salvar_entidade("zombie_archer.png", textura_zumbi((100, 120, 80), (80, 100, 60), (90, 110, 70)))

# zombie padrão (apocalipse) — cinza pele morta
salvar_entidade("zombie.png", textura_zumbi((140, 130, 120), (110, 100, 90), (120, 110, 100), mancha_sangue=True))

# Animais apocalípticos

# wild_dog - marrom sujo com focinho e olhos
img = Image.new("RGBA", (64, 64), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 64, 64], fill=MARROM_SUJO)
d.rectangle([16, 16, 48, 40], fill=(90, 70, 50))
d.rectangle([20, 40, 44, 56], fill=(100, 80, 60))
# Focinho
d.rectangle([24, 34, 40, 42], fill=(150, 130, 110))
# Olhos
d.rectangle([22, 20, 26, 24], fill=PRETO)
d.rectangle([38, 20, 42, 24], fill=PRETO)
salvar_entidade("wild_dog.png", img)

# crow - cinza escuro (ave) com asas e bico
img = Image.new("RGBA", (64, 64), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 64, 64], fill=(50, 50, 60))
d.rectangle([16, 16, 48, 32], fill=(30, 30, 40))  # corpo
d.rectangle([0, 24, 64, 40], fill=(40, 40, 50))  # asas
d.rectangle([28, 30, 36, 34], fill=(150, 100, 50))  # bico
d.rectangle([26, 18, 30, 22], fill=PRETO)  # olho
salvar_entidade("crow.png", img)

# plague_rat - cinza esverdeado doente com rabo
img = Image.new("RGBA", (64, 64), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 64, 64], fill=(110, 120, 100))
d.rectangle([32, 16, 60, 32], fill=(90, 100, 80))  # corpo/traseiro
d.rectangle([16, 32, 48, 56], fill=(100, 110, 90))  # frente
d.rectangle([58, 24, 64, 40], fill=(90, 100, 80))  # rabo
d.rectangle([20, 22, 24, 26], fill=PRETO)  # olho
d.rectangle([40, 22, 44, 26], fill=PRETO)  # olho
salvar_entidade("plague_rat.png", img)

# ===== NOVOS MOBS DO APOCALIPSE =====

# zombie_brute - Zumbi Bruto (elite pesado)
salvar_entidade("zombie_brute.png", textura_zumbi((60, 60, 55), (45, 45, 40), (50, 50, 45), mancha_sangue=False))

# zombie_behemoth - Zumbi Behemoth (chefe gigante)
salvar_entidade("zombie_behemoth.png", textura_zumbi((80, 80, 75), (60, 60, 55), (65, 65, 60), mancha_sangue=True))

# ===== NOVOS ITENS =====

# water_bottle - Garrafa d'Água azul com tampa
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([8, 6, 24, 30], fill=(0, 120, 200), outline=CINZA_ESCURO)
d.rectangle([12, 10, 20, 16], fill=(150, 220, 255))
d.rectangle([11, 26, 21, 28], fill=CINZA)
salvar_item("water_bottle.png", img)

# energy_drink - Latas de energia vermelhas/cinza
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([8, 8, 24, 28], fill=(60, 60, 60), outline=CINZA_ESCURO)
d.rectangle([9, 10, 23, 12], fill=(200, 60, 60))
d.rectangle([10, 14, 22, 16], fill=(220, 220, 220))
d.rectangle([11, 18, 21, 20], fill=(200, 60, 60))
d.rectangle([12, 22, 20, 26], fill=(180, 60, 60))
salvar_item("energy_drink.png", img)

# flashlight - Lanterna com fonte de luz (bússola)
img = Image.new("RGBA", (32, 32), (0,0,0,0))
d = ImageDraw.Draw(img)
d.rectangle([12, 6, 20, 30], fill=(200, 200, 200), outline=CINZA_ESCURO)
d.rectangle([13, 8, 19, 10], fill=(150, 150, 150))
d.rectangle([13, 26, 19, 28], fill=(150, 150, 150))
d.rectangle([16, 2, 16, 6], fill=(220, 220, 0))  # luz
salvar_item("flashlight.png", img)

print("\n=== TODAS AS TEXTURAS CRIADAS COM SUCESSO! ===")