# Contribuindo com o Zombie Apocalypse

Obrigado pelo interesse em contribuir! Este e um mod experimental em versao beta
(Minecraft 1.20.1 + Forge 47.4.28). Todas as contribuicoes sao bem-vindas.

## Como começar

1. Faça um fork do repositorio.
2. Clone o fork localmente.
3. Abra o projeto em sua IDE (IntelliJ IDEA ou Eclipse recomendados).
4. Execute `gradlew.bat genIntellijRuns` (Windows) ou `./gradlew genIntellijRuns`
   para gerar as configuracoes de execucao.
5. Teste com `gradlew.bat runClient`.

## Padroes de codigo

- Java 17.
- Codificacao UTF-8.
- Comentarios e mensagens em portugues do Brasil (codigo em ingles).
- Nomes de identificadores em ingles (mod ID, pacotes, classes).
- Siga a estrutura existente: `entity`, `item`, `init`, `config`, `event`, `client`.

## Enviando mudancas

1. Crie uma branch a partir de `main` ou `develop`.
2. Faça suas mudancas e teste localmente (`gradlew.bat build`).
3. Envie um pull request descricao o que foi alterado e por que.

## Relatando bugs

Abra uma issue no GitHub com:
- Versao do Minecraft e Forge.
- Versao do mod.
- Passos para reproduzir.
- Logs de erro (logs/latest.log), se houver.

## Licenca

Ao contribuir, voce concorda que suas contribuicoes serao licenciadas sob a
mesma licenca MIT do projeto (veja LICENSE).

## Recursos visuais

As texturas atuais sao pixel art provisoria gerada localmente. Contribuicoes
com texturas finais, modelos e sons sao bem-vindas. Não inclua materiais de
terceiros sem autorizacao.
