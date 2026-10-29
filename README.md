# Zombie Apocalypse

**Zombie Apocalypse** é um mod experimental para Minecraft Java Edition que traz um
sistema de apocalipse zumbi ao jogo, com variantes de inimigos, ondas de invasão,
itens de sobrevivência e mecânicas de infecção.

> ⚠️ **Versão Beta 0.1.0 — experimental.** Este é um lançamento inicial. Funcionalidades
> podem conter bugs, não estar balanceadas ou mudar em versões futuras.

---

## 📋 Informações básicas

| Campo | Valor |
|-------|-------|
| **Mod ID** | `zombieapocalypse` |
| **Minecraft** | 1.20.1 |
| **Forge** | 47.4.28 (série 47.x) |
| **Java** | 17 |
| **Versão** | 0.1.0 (beta) |
| **Licença** | MIT (veja LICENSE) |

---

## ✨ Funcionalidades implementadas

### Variantes de zumbi (5)
Cada uma com atributos, comportamento, sons e identificação próprios:

| Variante | Descrição |
|----------|-----------|
| **Corredor** | Rápido, pouca resistência |
| **Tanque** | Lento, muito resistente, alta redução de dano |
| **Infectado** | Aplica efeito temporário de infecção ao atacar |
| **Noturno** | Fica mais rápido e perigoso durante a noite |
| **Destruidor** | Quebra blocos configuráveis para alcançar o jogador |

### Animais apocalípticos (3)
Novas criaturas hostis que spawnam tanto de dia quanto de noite:

| Animal | Descrição |
|--------|-----------|
| **Cão Selvagem** | Canino hostil, aparece em bando, ataca jogadores |
| **Corvo** | Ave voadora, mais comum à noite, ataca jogadores |
| **Rato Apocalíptico** | Roedor pequeno, rápido, espalha doenças |

### Sistema de apocalipse (ondas)
- **Uma onda a cada dia ciclico do Minecraft** (baseado no tempo do mundo, 24000 ticks = 1 dia)
- Dificuldade progressiva (ondas maiores com o numero da onda)
- Frequência das ondas configurável (fallback por tempo)
- Quantidade mínima/máxima de inimigos por onda ajustável
- Eventos especiais durante a noite (mais zumbis noturnos e infectados)
- Mensagem de título na tela quando uma onda começa
- Opção para ativar/desativar o sistema
- Limite de zumbis por servidor e por área (perto do jogador)
- Respeita a dificuldade do Minecraft (sem ondas nem spawn em Paz)

### Spawn contínuo (dia e noite)
- Zumbis e animais apocalípticos spawnam continuamente perto dos jogadores
- Tanto de dia quanto de noite
- Controlado por chance por tick e limites de quantidade
- Não sobrecarrega o servidor nem a área do jogador

### Itens de sobrevivência
- **Bandagem**: recupera parte da vida (4 pontos)
- **Antídoto**: remove o efeito de infecção
- **Alimento Enlatado**: novo alimento de sobrevivência
- **Detector de Zumbis**: identifica a proximidade de zumbis do mod
- **Armadura de combate**: capacete, peitoral, calças e botas (material "Riot")
- **Placa Reforçada**: componente de fabricação e reparo da armadura

### Outros
- Efeito de Infecção (dano periódico enquanto ativo)
- Receitas de fabricação equilibradas para todos os itens
- Aba criativa dedicada "Zombie Apocalypse"
- Spawn natural raro das variantes no Overworld

---

## 📦 Instalação

1. Instale o [Minecraft Forge 47.4.28](https://files.minecraftforge.net/) para Minecraft 1.20.1.
2. Baixe o arquivo `zombieapocalypse-0.1.0-forge-1.20.1.jar` das Releases (quando publicado).
3. Coloque o JAR na pasta `mods` do seu Minecraft (`.minecraft/mods`).
4. Inicie o Minecraft com o perfil Forge.
5. O arquivo de configuração `zombieapocalypse-common.toml` será gerado em `.minecraft/config/`
   na primeira execução. Edite-o para ajustar ondas, detecção, infecção e destruição de blocos.

---

## 📱 Addon Bedrock (mcaddon)

O projeto inclui um addon para a **Minecraft Bedrock Edition** na pasta `mcaddon/`,
com modelos 3D, texturas e animações criados no **Blockbench**.

### Instalação no Bedrock

1. Compacte a pasta `mcaddon/` em um arquivo `.zip` e renomeie para `.mcpack`
   (ou use o arquivo `Zombie_Apocalypse_Addon.mcaddon` já gerado).
2. Abra o `.mcpack` no Minecraft Bedrock para importar o addon.
3. Ative o addon nas configurações de comportamento e recursos do mundo.
4. Use `/summon` para testar as entidades:

   ```
   /summon zombieapocalypse:zombie
   /summon zombieapocalypse:wild_dog
   /summon zombieapocalypse:plague_rat
   /summon zombieapocalypse:crow
   ```

### Estrutura do addon

- `manifest.json` — cabeçalho e módulos (entidades + itens).
- `models/entity/*.geo.json` — geometria 3D (formato Blockbench/Bedrock).
- `textures/entity/*.png` e `textures/item/*.png` — texturas pixel art.
- `animations/*.animation.json` — animações das entidades.
- `animation_controllers/*.json` — transições entre animações.
- `render_controllers/*.json` — liga geometria e textura.
- `entities/*.json` — definições de cada entidade (spawn, vida, ataque, IA).

Para editar modelos e texturas visualmente, abra os arquivos `.geo.json` no
Blockbench (consulte `GUIA_BLOCKBENCH.md`).

---

## 🛠️ Compilação no Windows

Pré-requisitos: Java 17 e conexão com internet (para baixar dependências do Forge).

```cmd
cd C:\caminho\do\projeto\zombieapocalypse
gradlew.bat build
```

O JAR final será gerado em:

```
build\libs\zombieapocalypse-0.1.0-forge-1.20.1.jar
```

---

## ⚙️ Configuração

Edite `zombieapocalypse-common.toml` (pasta `config`) para ajustar:

- `apocalipse.enabled` — ativa/desativa o sistema de ondas
- `apocalipse.wave_frequency_seconds` — frequência das ondas (em segundos)
- `apocalipse.max_zombies_server` — limite global de zumbis
- `apocalipse.max_zombies_near_player` — limite de zumbis perto do jogador
- `apocalipse.min_zombies_per_wave / max_zombies_per_wave` — tamanho das ondas
- `apocalipse.night_events_enabled` — eventos noturnos
- `detecao.radius` — raio de detecção dos zumbis (blocos)
- `variantes.<tipo>.health` e `.speed` — vida e velocidade de cada variante
- `infeccao.chance` — chance de infecção ao ser atacado pelo Zumbi Infectado
- `infeccao.duration_seconds` — duração da infecção
- `destruicao.enabled` — ativa/desativa quebra de blocos pelo Destruidor
- `destruicao.blocks` — lista de blocos que o Destruidor pode quebrar
- `variantes.caeselvagem.health / .speed` — vida e velocidade do Cão Selvagem
- `variantes.corvo.health / .speed` — vida e velocidade do Corvo
- `variantes.ratopraga.health / .speed` — vida e velocidade do Rato Apocalíptico
- `spawncontinuo.enabled` — ativa/desativa spawn contínuo de dia e noite
- `spawncontinuo.chance_per_tick` — chance de spawn por tick perto de cada jogador
- `spawncontinuo.max_near_player` — limite de entidades perto do jogador

---

## 🖼️ Recursos visuais

As texturas (entidades, itens, armadura e arte de capa) são em **pixel art**
(estilo 16x16 / 64x64). Os modelos 3D das entidades foram criados e podem ser
editados no **[Blockbench](https://blockbench.net/)** — consulte
`GUIA_BLOCKBENCH.md` para o passo a passo completo de modelagem, texturização,
animação e exportação para Java e Bedrock.

### Modelos 3D por entidade (Bedrock / Blockbench)

| Entidade | Modelo | Animação | Status |
|----------|--------|----------|--------|
| Zumbi | `zombie.geo.json` | `zombie.animation.json` | ✅ Melhorado |
| Cão Selvagem | `wild_dog.geo.json` | `wild_dog.animation.json` | ✅ Novo |
| Rato Apocalíptico | `plague_rat.geo.json` | `plague_rat.animation.json` | ✅ Novo |
| Corvo | `crow.geo.json` | `crow.animation.json` | ✅ Novo |

A arte de capa está em `docs/assets/cover.png`.

---

---

## 🎮 Comandos In-Game (/za)

Gerencie o apocalipse diretamente pelo chat ou console:

- `/za wave` — inicia imediatamente a onda atual centralizada no jogador.
- `/za wave <numero>` — inicia uma onda com o número especificado.
- `/za status` — exibe o relatório completo: onda atual, total de inimigos ativos, ondas sobrevividas, dia do mundo e limites configurados.
- `/za reset` — reinicia o contador de ondas e o progresso salvo.
- `/za spawn <tipo> [quantidade]` — invoca variantes de zumbis ou animais apocalípticos.

---

## 🐛 Problemas resolvidos e melhorias recentes

1. **Persistência de Ondas via SavedData (NBT):**  
   O progresso das ondas agora é salvo automaticamente no mundo (`zombieapocalypse_state.dat`), não sendo mais perdido ao reiniciar o servidor ou fechar o jogo.

2. **Modelagem e Renderização 3D dos Animais:**  
   O Corvo, o Cão Selvagem e o Rato Apocalíptico agora possuem modelos 3D customizados com animações completas (voo do corvo, corrida quadrúpede do cão e do rato, abanar de cauda e ataque).

3. **Correção de IA e Velocidade:**  
   Corrigido o modificador de velocidade de ataque das variantes de zumbis e animais, garantindo perseguição fluida e ataques letais.

4. **Granada de Fumaça Tática:**  
   Substituída a colocação de blocos rígidos por uma nuvem volumétrica realista (`AreaEffectCloud`), aplicando cegueira nos monstros e concedendo invisibilidade/fuga para o sobrevivente.

5. **Isca de Zumbi Reformulada:**  
   Agora atrai e acelera realisticamente criaturas hostis em um raio de 36 blocos, com efeitos de partículas de sangue e som de atração.

6. **Aba Criativa e Modelos de Itens:**  
   Aba criativa dedicada devidamente registrada e modelos 3D/texturas adicionados para o Taco com Pregos, Granada de Fumaça, Kit Médico e Isca.

7. **Melhorias Beta 0.2.0 (Novas):**
   - **Animações completas no Bedrock:** idle, ataque e morte para todos os zumbis + animation controller com transições.
   - **Partículas de sangue:** ao ser atingido, ao atacar e ao morrer (Java).
   - **Sons de ataque** personalizados por variante + explosão com partículas (fogo/fumaca).
   - **Zumbi Alfa Mutante (chefe):** registrado no mod e integrado às ondas (aparece a partir da onda 10).
   - **Recompensas por onda sobrevivida:** progressivas (Kit Medico, Bandagem, Antidoto, Alimento Enlatado, Detector).
   - **Build corrigido:** erros de compilação no RunnerZombieEntity e SurvivalRevolverItem resolvidos.

---

## 📬 Como reportar bugs

Abra uma issue no repositório do GitHub incluindo:
- Versão do Minecraft e Forge
- Versão do mod (0.1.0)
- Descrição do problema e passos para reproduzir
- Logs relevantes (`.minecraft/logs/latest.log`), se houver

---

## 📄 Créditos e licenças

- **Código-fonte**: Zombie Apocalypse Project — licença MIT (veja LICENSE).
- **Texturas, modelos e arte**: arte e modelos 3D originais criados localmente para este projeto.
- **Sons**: referências a sons nativos do Minecraft (sem arquivos de áudio de terceiros).
- **Minecraft e Forge**: marcas registradas de seus respectivos proprietários. Este
  mod não é afiliado à Mojang Studios nem à Forge.

Não foram incorporados materiais de terceiros sem autorização.

---

*Desenvolvido para Minecraft 1.20.1 + Forge 47.4.28*
