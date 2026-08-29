# MeuPet+ — landing page

Página de vendas do app MeuPet+, no ar em **https://meupetmais.com.br/home/**.
Converse em português (pt-BR) — é o idioma da Fabíola e de todo o conteúdo.

## ⚠️ Publicação: leia antes de encerrar qualquer tarefa

O GitHub Pages publica a partir da branch **`main`**, pasta `/ (root)`.

**Ao terminar uma alteração, faça o merge da branch de trabalho na `main` e dê
push nela.** Só isso coloca a mudança no ar. Sem esse passo o site continua
igual, e a Fabíola vê você dizer "pushado" sem nada mudar na tela dela.

Esta é uma **autorização permanente** dela para escrever na `main` deste
repositório — foi combinada explicitamente e vale para as próximas sessões.
Sequência:

```
git checkout main && git merge <branch-de-trabalho> && git push origin main
```

O deploy do Pages roda sozinho e leva um ou dois minutos.

Uma armadilha conhecida: o navegador guarda a página por ~10 min
(`Cache-Control: max-age=600`). Se a mudança não aparecer logo, teste numa
janela anônima antes de procurar outro culpado.

## Como editar a página

1. Edite **`fonte/index.template.html`** — é o arquivo de origem.
2. Rode **`python3 fonte/build.py`**, que gera o `home/index.html`.
3. Commite os dois.

Nunca edite `home/index.html` na mão: ele é gerado e será sobrescrito.

## Estrutura

| Caminho | O que é |
|---|---|
| `home/index.html` | A página. Arquivo único: CSS, JS, fontes e prints embutidos, zero requisição externa. |
| `index.html` (raiz) | Só redireciona `/` para `/home/`, preservando query string e âncora. |
| `fonte/` | Template, `build.py`, fontes `.woff2` e os prints em WebP. |
| `CNAME`, `.nojekyll` | Configuração do GitHub Pages. |

## Pendência aberta

**Link de checkout.** Os 5 CTAs apontam para `#oferta` como espaço reservado —
ninguém consegue assinar ainda. Quando a URL de assinatura existir, procure por
`<!-- Link de checkout` no `fonte/index.template.html`.
