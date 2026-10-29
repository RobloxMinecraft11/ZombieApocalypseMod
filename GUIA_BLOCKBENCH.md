# 🛠️ Guia do Blockbench — Zombie Apocalypse (Java + Bedrock)

Este guia ensina a usar o **[Blockbench](https://blockbench.net/)** para melhorar os modelos 3D e texturas deste mod, tanto para a **Java Edition (Forge 1.20.1)** quanto para a **Bedrock Edition (mcaddon)**.

> O Blockbench é o padrão da comunidade para criar modelos e animações de entidades/itens do Minecraft. Ele exporta diretamente o formato `.geo.json` usado pelo Bedrock e pode ser usado com plugins para a Java Edition.

---

## 📁 Estrutura relevante do projeto

```
mcaddon/
├── manifest.json               # Cabeçalho do addon Bedrock
├── models/entity/              # Modelos 3D (.geo.json) exportados pelo Blockbench
│   ├── zombie.geo.json         # Zumbi (melhorado)
│   ├── wild_dog.geo.json       # Cão selvagem (novo)
│   ├── plague_rat.geo.json     # Rato apocalíptico (novo)
│   └── crow.geo.json           # Corvo (novo)
├── textures/
│   ├── entity/                 # Texturas das entidades (64×64)
│   │   ├── zombie.png
│   │   ├── wild_dog.png
│   │   ├── plague_rat.png
│   │   └── crow.png
│   └── item/                   # Texturas dos itens (16×16 / 32×32)
├── animations/                 # Animações (.animation.json)
│   ├── zombie.animation.json
│   ├── wild_dog.animation.json
│   ├── plague_rat.animation.json
│   └── crow.animation.json
├── animation_controllers/      # Controladores de transição de animação
├── render_controllers/         # Controladores de render (liga geometry + textura)
└── entities/                   # Definições de entidade (referenciam geometry + animações)
    ├── zombie_apocalypse.json
    ├── wild_dog.json
    ├── plague_rat.json
    └── crow.json
```

---

## 1. Instalando o Blockbench

1. Baixe em: https://blockbench.net/ (versão Desktop, recomendada).
2. Instale e abra. No menu principal, selecione **"Bedrock"** como formato ao criar um novo projeto.
3. (Opcional) Instale plugins úteis:
   - **Blockbuster** — para cenas/animações cinemáticas.
   - **Java Model** — se quiser exportar para a Java Edition.

---

## 2. Importando os modelos existentes no Blockbench

Os arquivos `.geo.json` em `mcaddon/models/entity/` já estão prontos para serem abertos e editados visualmente no Blockbench:

1. Abra o Blockbench → **File → Open** → selecione `mcaddon/models/entity/zombie.geo.json`.
2. O modelo aparecerá na visualização 3D com todos os ossos (head, body, arm_left, arm_right, leg_left, leg_right).
3. No painel **Outliner** (à esquerda), você vê a lista de ossos e cubos. Clique em qualquer um para editar posição, tamanho, rotação e UVs.
4. Para ajustar a textura, abra a aba **Texture** (no painel direito) e carregue/pinte a imagem correspondente em `mcaddon/textures/entity/`.

**Repita para:** `wild_dog.geo.json`, `plague_rat.geo.json`, `crow.geo.json`.

---

## 3. Melhorando o modelo (fluxo recomendado)

### A. Ajustar ossos e cubos
No Blockbench:
- **Add Cube** → cria um novo cubo dentro do osso selecionado.
- Mova os cubos com os manipuladores (setas coloridas) ou digite valores no painel de transformação.
- Ajuste o **Pivot** de cada osso para que as rotações de animação fiquem corretas (ex: pivô da cabeça no pescoço, pivô dos braços no ombro).

### B. Texturar (UV Mapping)
1. Na aba **Texture**, crie ou carregue uma imagem PNG (ex: `zombie.png`, 64×64 para entidades).
2. Use o **UV Editor** (painel direito) para arrastar as faces dos cubos sobre a textura.
3. Pinte diretamente na textura com a ferramenta **Paint** (estilo pixel art do Minecraft).
4. Dicas de tamanho:
   - Entidades (zumbi, cão, rato, corvo): **64×64 px**.
   - Itens (taco, kit médico, isca etc.): **16×16 px** ou **32×32 px**.

### C. Animações
O Blockbench tem uma aba **Animate** onde você pode criar animações por frame (stop-motion) ou por comando. No entanto, neste projeto as animações Bedrock já estão definidas em `mcaddon/animations/*.animation.json` usando expressões matemáticas (formato Bedrock). 

- Se quiser editar animações visualmente: use a aba **Animate** e exporte para `.animation.json`.
- Se quiser ajustar as existentes: edite diretamente os arquivos `.animation.json` (estão comentados e usam `query.life_time`).

### D. Exportando para o Bedrock
Após editar:
1. **File → Export → Bedrock Geometry (.geo.json)** → sobrescreva o arquivo em `mcaddon/models/entity/`.
2. **Texture → Save** → sobrescreva o PNG em `mcaddon/textures/entity/`.
3. O pacote `.mcaddon` (`.mcpack`/`Zombie_Apocalypse_Addon.zip`) pode ser reempacotado e instalado no Minecraft Bedrock.

---

## 4. Sincronizando com a Java Edition (Forge 1.20.1)

A Java Edition não usa `.geo.json` nativamente. Os modelos Java estão em código:

```
src/main/java/com/mklar/zombieapocalypse/client/render/model/
├── ZombieModel.java
├── WildDogModel.java
├── PlagueRatModel.java
└── CrowModel.java
```

**Para trazer as melhorias do Blockbench para o Java:**

**Opção A — Recriar no código (recomendado para manter controle total):**
Abra o `ZombieModel.java` (ou os modelos dos animais) e espelhe a estrutura do `.geo.json` usando `CubeListBuilder.addBox(...)` com os mesmos tamanhos e posições que você definiu no Blockbench. Mantenha os mesmos nomes de partes (`body`, `head`, `legLeft`, `legRight`, `armLeft`, `armRight`) para que os renderizadores continuem funcionando.

**Opção B — Plugin Blockbench → Java:**
Instale o plugin **"Java Model"** no Blockbench, modele no formato Java e exporte como classe Java. Depois adapte o pacote (`package`) para `com.mklar.zombieapocalypse.client.render.model`.

> ⚠️ Atenção: a Java Edition usa um sistema de coordenadas e escala diferente do Bedrock. Teste no jogo após cada alteração para evitar modelos desproporcionais ou hitboxes erradas.

---

## 5. O que já foi melhorado neste commit

| Entidade | Status | Modelo Bedrock | Animação | Render Controller |
|----------|--------|----------------|----------|-------------------|
| Zumbi | ✅ Melhorado | `zombie.geo.json` (cabeça com olhos/nariz/dentes, mãos e sapatos integrados) | `zombie.animation.json` (cabeça e corpo balançam ao andar) | ✅ já existia |
| Cão Selvagem | ✅ Novo | `wild_dog.geo.json` (corpo, cabeça, 4 patas, cauda) | `wild_dog.animation.json` (trotar, balançar cauda) | ✅ novo |
| Rato Apocalíptico | ✅ Novo | `plague_rat.geo.json` (corpo pequeno, 4 patas, cauda longa) | `plague_rat.animation.json` (andar rápido) | ✅ novo |
| Corvo | ✅ Novo | `crow.geo.json` (corpo, cabeça, bico, 2 asas, 2 patas, cauda) | `crow.animation.json` (idle + voo com batida de asas) | ✅ novo |

As definições de entidade (`mcaddon/entities/*.json`) foram atualizadas para referenciar a geometria, animações e render_controllers correspondentes.

---

## 6. Checklist antes de lançar

- [ ] Abrir cada `.geo.json` no Blockbench e verificar que não há cubos sobrepostos incorretamente.
- [ ] Verificar que os **pivots** dos ossos de animação (pernas, braços, asas) estão nas articulações corretas.
- [ ] Confirmar que as texturas PNG em `mcaddon/textures/entity/` batem com o mapeamento UV dos modelos.
- [ ] Instalar o `.mcaddon` em um mundo Bedrock e verificar se as entidades aparecem com o modelo correto.
- [ ] (Java) Compilar com `gradlew.bat build` e verificar se os modelos renderizam sem erros no Forge.

---

## 7. Comandos úteis no jogo (Bedrock)

Depois de instalar o addon, para testar as entidades:

```
/summon zombieapocalypse:zombie
/summon zombieapocalypse:wild_dog
/summon zombieapocalypse:plague_rat
/summon zombieapocalypse:crow
```

---

## 8. Referências

- [Blockbench — Documentação oficial](https://github.com/JannisX11/blockbench/wiki)
- [Bedrock Geometry (geo.json)](https://docs.minecraftcreator.com/en/references/1-19-80/entity/geometry-1-12-0)
- [Bedrock Animation Controllers](https://docs.minecraftcreator.com/en/references/1-19-80/entity/animation-controllers-1-10-0)
- [Forge Java Entity Models](https://docs.minecraftforge.net/en/1.20.1/client/models/entity-models/)

---

*Boa modelagem! Se precisar de ajuda para exportar um modelo específico do Blockbench para o Java, me avise.*
