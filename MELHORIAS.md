# 🧟 Melhorias — Zombie Apocalypse (Java + Bedrock)

Este documento resume as melhorias aplicadas ao mod para **Minecraft Java (Forge 1.20.1)** e **addon Bedrock**, com foco no fluxo de trabalho do **Blockbench**.

---

## 1. O que já existe no projeto

| Lado | Pasta/arquivo | Detalhes |
|------|---------------|----------|
| Java (Forge) | `src/main/java/com/mklar/zombieapocalypse/` | 10 variantes de zumbi, 3 animais, itens de sobrevivência, armário de motim, sistema de ondas, config TOML |
| Java (client) | `src/main/java/.../client/render/model/` | Modelos 3D codificados em Java (`ZombieModel`, `WildDogModel`, etc.) |
| Bedrock | `mcaddon/` | `manifest.json`, `entities/`, `items/`, `models/entity/*.geo.json`, `animations/`, `textures/` |
| Texturas | `gerar_texturas.py` | Script Python (Pillow) que gera texturas de item e entidade |

---

## 2. Problemas encontrados e corrigidos

### 2.1 Faltavam arquivos-fonte do Blockbench (`.bbmodel`)
Só existiam exports `geo.json` (prontos para o Bedrock). Sem o `.bbmodel` não é possível reabrir o modelo no Blockbench para editar.

**Correção:** criado `mcaddon/models/entity/zombie.bbmodel` — projeto completo do Blockbench com:
- todos os ossos (head, body, arm_left/right, leg_left/right, nose, olhos, boca, shirt, pants, sapatos)
- UVs mapeados para a textura 64×64
- grupos no outliner
- pivôs e rotações

**Como usar:** abra o Blockbench → File → Open → selecione `mcaddon/models/entity/zombie.bbmodel`. Depois edite e exporte novamente como Bedrock geometry (`.geo.json`).

### 2.2 Modelo Java com escala errada (zumbi minúsculo)
Em `ZombieModel.java` as caixas tinham tamanho de `0.4F` (menos de meio bloco), o que faria a entidade ficar minúscula no jogo.

**Correção:** as caixas agora usam escala de bloco (cabeça 8×8×8, corpo 8×12×4, braços 4×8×2, pernas 4×10×4), alinhada com a geometria do Bedrock.

### 2.3 Texturas muito simples (retângulos de cor sólida)
As texturas são geradas por `gerar_texturas.py` com cores planas, sem sombreado nem detalhe de pixel art.

**Sugestão:** use o **Texture Painter** do Blockbench para pintar as texturas diretamente sobre o modelo 3D, ou edite as PNGs em `src/main/resources/assets/zombieapocalypse/textures/` (Java) e `mcaddon/textures/` (Bedrock).

---

## 3. Como adicionar um novo zumbi (fluxo Java + Bedrock)

### 3.1 No Blockbench (modelo 3D)
1. Abra `mcaddon/models/entity/zombie.bbmodel`.
2. Duplique um osso ou adicione novos cubos para a variante (ex.: `armor` para o Tank, `bow` para o Archer).
3. Ajuste os UVs na textura 64×64.
4. Exporte:
   - Bedrock: `models/entity/zombie_novo.geo.json`
   - Java (opcional): use como referência para reescrever o `*Model.java`

### 3.2 No Bedrock (`mcaddon/`)
1. Crie `mcaddon/entities/zombie_novo.json` baseado em `zombie_apocalypse.json` (mude o `identifier`, textura, vida, dano, velocidade).
2. Adicione o spawn em `spawn_rules` (ou crie um arquivo próprio).
3. Atualize `mcaddon/manifest.json` se mudar a versão.

### 3.3 No Java (`src/main/java/`)
1. Crie a classe da entidade em `entity/` (estenda `ApocalypseZombieEntity` ou `Mob`).
2. Registre em `ModEntities.java` (`ENTITY_TYPES.register(...)`).
3. Crie o renderer em `client/render/` e a camada de modelo em `client/render/model/`.
4. Registre o renderer em `ClientEntityEvents.registerRenderers`.
5. Adicione atributos em `CommonEntityEvents.onEntityAttributeCreation`.
6. Adicione o item de spawn (ovo) se quiser.

### 3.4 Sincronize as texturas
Copie a mesma PNG de textura para ambos os lados:
- Java: `src/main/resources/assets/zombieapocalypse/textures/entity/zombie_novo.png`
- Bedrock: `mcaddon/textures/entity/zombie_novo.png`

---

## 4. Melhores práticas com Blockbench neste projeto

- **Mantenha o `.bbmodel` junto com o `.geo.json`** no `mcaddon/models/entity/`. O `.geo.json` é o export; o `.bbmodel` é o arquivo editável.
- **Textura 64×64** para entidades — aproveite toda a área: cabeça (0,0)-(56,32), corpo (16,20)-(44,32), membros nas laterais.
- **Use nomes de osso padrão do Bedrock** (`head`, `body`, `arm_left`, `arm_right`, `leg_left`, `leg_right`) para que as animações existentes funcionem sem alterar os controladores.
- **Exporte com o nome exato** que o `manifest` / `entity.json` referenciam (`geometry.zombie`, etc.).

---

## 5. Próximos passos sugeridos

1. Abra `zombie.bbmodel` no Blockbench e refine a modelagem (adicionar rasgos na roupa, olhos brilhantes, feridas).
2. Pinte as texturas com o Texture Painter do Blockbench (substitua os retângulos coloridos do `gerar_texturas.py`).
3. Crie `.bbmodel` para `wild_dog`, `crow` e `plague_rat` (os animais já têm modelo Java, mas faltam fontes Blockbench no Bedrock).
4. Sincronize versões: Java está na `0.1.0` e Bedrock na `1.0.0` — padronize em ambos os `manifest`/`gradle.properties`.
5. Adicione o `AlphaZombieEntity` (existe no Java) também ao Bedrock para manter os dois lados iguais.

---

## 6. Melhorias de Dificuldade (v0.2.0)

Para deixar o mod mais desafiador, foram aumentados:

### Java (Forge)
- Ondas: `min_zombies_per_wave` 25→50, `max_zombies_per_wave` 100→200, tamanho cresce ×5 por onda.
- Ondas mais frequentes: `wave_frequency_seconds` 180→90.
- Spawn contínuo: chance por tick 0.08→0.18, max perto do jogador 60→100.
- Detecção: `radius` 24→40 blocos.

### Variantes (Java + Bedrock)
- Vida e dano aumentados (ex.: Runner vida 25→45, dano 4→6; Tank vida 90→180, dano 10→12; Alpha vida 200→400, dano 10→14).
- Velocidades aumentadas (Runner 0.55→0.85, Infected 0.34→0.55, Tank 0.18→0.25...).
- Ataque mais rápido (`tick_delay` menor, reach maior).
- Spawn de Alpha (chefe) agora aparece a partir da onda 5 (antes onda 10), com chance 15%.

---

## 8. Novos Mobs e Chefes adicionados (v0.3.0)

- **Zumbi Bruto** (`brute_zombie`): elite pesado (vida 220, dano 12, velocidade 0.15, armadura 8). Spawn raramente.
- **Zumbi Behemoth** (`behemoth_zombie`): **chefe secundário** (vida 800, dano 18, arena sísmica, invoca zumbis).

Arquivos criados:
- `entity/BruteZombieEntity.java`
- `entity/BehemothZombieEntity.java`
- `client/render/BehemothZombieRenderer.java`
- `mcaddon/entities/zombie_brute.json`
- `mcaddon/entities/zombie_behemoth.json`
- `mcaddon/models/entity/zombie_behemoth.geo.json`
- `mcaddon/render_controllers/behemoth_zombie.render_controller.json`

---

## 9. Comandos úteis

```powershell
# Build do mod Java (Forge)
./gradlew build

# Gerar texturas (Python)
python gerar_texturas.py

# Empacotar addon Bedrock (zipar a pasta mcaddon)
Compress-Archive -Path mcaddon\* -DestinationPath Zombie_Apocalypse_Addon.mcaddon
```
