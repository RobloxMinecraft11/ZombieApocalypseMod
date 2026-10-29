# Changelog - Zombie Apocalypse

Todas as mudanças notaveis deste documento serao registradas neste arquivo.

O formato e baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto segue o [Versionamento Semantico](https://semver.org/lang/pt-BR/).

## [0.2.0] - 2026-10-29

### Adicionado
- Animacoes completas de zumbi no Bedrock: idle, ataque (`attack`) e morte (`die`).
- Animation controller com estados transicionais (idle <-> walk <-> attack <-> die) para Bedrock.
- Render controllers customizados para todas as variantes de zumbi (tank, runner, infected,
  night, destroyer, explosive, archer).
- Sistema de partículas de sangue no Java (dano, ataque e morte) via eventos `LivingHurtEvent`,
  `LivingAttackEvent` e `LivingDeathEvent`.
- Sons de ataque personalizados por variante (runner, tank, infected, night, destroyer, explosive, archer).
- Som de explosao e particulas de explosao no Zumbi Explosivo (fogo + fumaca).
- Zumbi Alfa Mutante (chefe) integrado ao registro de entidades e ao sistema de ondas
  (aparece a partir da onda 10).
- Sistema de recompensas por ondas sobrevidas (progressivo por numero da onda).

### Alterado
- Todos os JSONs do addon Bedrock validados (formato 1.20.0 / 1.12.0 / 1.8.0 / 1.10.0).

### Corrigido
- Erro de compilacao no `RunnerZombieEntity.java` (chave extra).
- Erros de compilacao em `SurvivalRevolverItem.java` (nomes de sons inexistentes no MC 1.20.1).

## [0.1.0] - 2026-10-28

### Adicionado
- Cinco variantes de zumbi: Corredor, Tanque, Infectado, Noturno e Destruidor.
- Sistema de ondas de apocalipse com dificuldade progressiva, frequencia configuravel,
  quantidade de inimigos ajustavel, eventos especiais noturnos e mensagens na tela.
- Itens de sobrevivencia: Bandagem, Antidoto, Alimento Enlatado, Detector de Zumbis.
- Armadura de combate (Capacete, Peitoral, Calcas, Botas) e Placa Reforçada.
- Efeito de Infecao (aplicado pelo Zumbi Infectado, removido pelo Antidoto).
- Configuracoes editaveis (zombieapocalypse-common.toml): frequencia das ondas,
  quantidade maxima de zumbis, velocidade/resistencia das variantes, raio de detecao,
  chance de infecao, destruicao de blocos e eventos noturnos.
- Receitas de fabricacao equilibradas para todos os itens e armadura.
- Texturas pixel art originais (16x16 itens, 64x64 entidades e armadura).
- Modelos JSON de itens, definicoes de som e arquivos de idioma (pt_BR e en_US).
- Bloco criativo da aba "Zombie Apocalypse".
- Spawn natural raro das variantes no Overworld.

### Alterado
- Nenhuma (versao inicial).

### Corrigido
- Nenhuma (versao inicial).

### Removido
- Nenhuma (versao inicial).

## [0.1.0-beta+animais] - 2026-10-28 (Melhorias Beta 0.1.0)

### Adicionado
- Tres animais apocalípticos: Cao Selvagem, Corvo e Rato Apocalíptico.
- Spawn contínuo de zumbis e animais tanto de dia quanto de noite (configurável).
- Uma onda a cada dia ciclico do Minecraft (baseado no tempo do mundo, 24000 ticks = 1 dia).
- Texturas pixel art provisórias para as 3 novas entidades (64x64).
- Novas opções de configuracao: spawncontinuo.enabled, spawncontinuo.chance_per_tick,
  spawncontinuo.max_near_player, e atributos dos animais (variantes.<animal>.health/.speed).

### Alterado
- Sistema de ondas agora disparado pelo ciclo dia/noite do mundo (uma onda por dia).
- Spawn de zumbis agora ocorre tanto de dia quanto de noite, não apenas em ondas.

### Corrigido
- Nenhuma.

### Removido
- Nenhuma.

## [0.1.0-beta] - Planejado

- Persistencia do estado das ondas entre reiniciacoes do servidor.
- Texturas finais via Higgsfield (requer plano básico ou superior - nao disponível neste ambiente).
- Comandos in-game para gerenciar ondas.
- Mais variantes e eventos especiais.
- Testes em servidor dedicado e multijogador.
