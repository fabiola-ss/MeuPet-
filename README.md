# MeuPet+ — Landing Page

Página de vendas do aplicativo **MeuPet+**, em **arquivo único** (`home/index.html`):
CSS, JavaScript, fontes e imagens estão todos embutidos. **Nenhuma requisição
externa** ao abrir a página. Sem framework, sem etapa de build no deploy —
o `home/index.html` sozinho já é o site.

## Publicar no GitHub Pages em meupetmais.com.br/home

O GitHub Pages serve pelo caminho da pasta: o que está em `home/index.html`
aparece em `meupetmais.com.br/home/`. Por isso a página gerada mora em `home/`,
e não na raiz.

Na raiz ficam três arquivos de publicação:

| Arquivo | Para que serve |
|---|---|
| `CNAME` | Diz ao Pages qual domínio serve este repositório. |
| `index.html` | Manda quem digita o domínio puro para `/home/`, preservando `?utm_...` e âncora. Sem ele, `meupetmais.com.br` dá 404. |
| `.nojekyll` | Desliga o Jekyll — o site é HTML puro, não precisa de processamento. |

> O Pages não faz redirect de servidor (nada de 301), então o da raiz é uma
> página com `location.replace` mais `meta refresh`. Ela fica em cache no
> navegador por ~10 min: se um dia você mexer nela e parecer que não mudou,
> teste numa janela anônima antes de procurar outro culpado.

### Configuração, uma vez só

1. **Settings → Pages → Build and deployment → Source: Deploy from a branch**
2. **Branch:** `claude/landing-page-html-css-js-kzivtn` · **Folder:** `/ (root)`
3. **Custom domain:** `meupetmais.com.br` → Save, e marque **Enforce HTTPS**
   depois que o certificado sair (leva alguns minutos).

### DNS, no painel do domínio

Domínio de topo (`meupetmais.com.br`) precisa de quatro registros **A**:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

E um **CNAME** de `www` para `fabiola-ss.github.io`.

Todo push na branch republica o site.

## Antes de publicar: dois pendentes

### 1. Link de checkout

Os CTAs apontam para a seção de oferta (`#oferta`) como espaço reservado.
Troque pelo link real de assinatura. Procure no `fonte/index.template.html`:

```
<!-- Link de checkout: troque o href abaixo pela URL de assinatura do app. -->
```

### 2. Peso da página

Os prints do app são embutidos em base64, então o `index.html` fica em
torno de **780 KB**. Como os prints estão dentro do HTML, o `loading="lazy"`
não reduz o que é baixado: o navegador precisa do arquivo inteiro antes de
desenhar qualquer coisa.

Se a velocidade de carregamento incomodar, o caminho é servir os prints como
arquivos separados ao lado do `home/index.html` em vez de embutidos — o HTML volta
para ~160 KB e as imagens passam a carregar em paralelo e sob demanda. Isso
abre mão do "arquivo único", mas no Pages (que publica a pasta inteira) não
faz diferença nenhuma no deploy.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `home/index.html` | **A página.** Único arquivo necessário para publicar. |
| `fonte/index.template.html` | HTML de origem, com marcadores no lugar das fontes e imagens. É aqui que se edita. |
| `fonte/build.py` | Gera o `home/index.html`. Rode depois de qualquer edição. |
| `fonte/prints/*.webp` | Os prints reais do aplicativo, em WebP. |
| `fonte/baloo2.woff2` | Baloo 2 (Google Fonts, subset latin, SIL OFL 1.1). |
| `fonte/jakarta.woff2` | Plus Jakarta Sans (Google Fonts, subset latin, SIL OFL 1.1). |

## Ritmo visual das seções

Três blocos de cor sólida cheia quebram o creme e criam os pontos altos do
scroll. As transições entre sólido e creme nunca são um corte reto:

| # | Seção | Fundo | Transição |
|---|---|---|---|
| 1 | Hero | **sólido** — gradiente magenta→roxo, texto branco | scalloped ↓ |
| 2 | Identificação | creme | — |
| 3 | Problema | creme-alt | — |
| 4 | Virada/Solução | creme | — |
| 5 | Features | creme-alt | — |
| 7 | Modo SOS | **sólido** — roxo escuro, cartão de emergência | onda ↑ e ↓ |
| 8 | Como funciona | creme | — |
| 9 | Oferta | **sólido** — gradiente laranja-coral | onda ↑, scalloped ↓ |
| 10 | Garantia | creme-alt | — |
| 11 | FAQ | creme | — |
| 12 | CTA final | creme | — |

## Variação de composição

Cada seção usa um tratamento diferente, para a página não virar uma pilha de
cards brancos iguais:

- **Hero** — foto do pet ocupando a lateral direita inteira, encostando na
  borda da tela e se dissolvendo no gradiente. Sem moldura, sem card. Uma única
  pill de destaque, para a headline mandar.
- **Identificação** — as falas do consultório em balões de conversa com rabicho,
  alternados, não em cards simétricos.
- **Problema** — lista nua: ícone + texto lado a lado, separados só por um filete.
  Nenhum card.
- **Virada** — texto à esquerda e o mockup do app solto à direita, sem moldura.
- **Features** — carrossel horizontal com scroll-snap; o próximo card fica
  cortado na lateral, mostrando que tem mais pra rolar. Setas no desktop,
  arraste no mobile, e a trilha é focável pelo teclado.
- **Multi-pet / Modo SOS** — os dois únicos pontos com blob de `border-radius`
  assimétrico, com recortes diferentes entre si.
- **Como funciona** — timeline com linha de conexão, sem card.
- **Garantia** — linhas simples com check, sem card.
- **FAQ** — acordeão de filetes, sem card.

Sombras nunca são cinza: `rgba(36,20,66,…)` da navy da marca nos cards e
`rgba(255,107,53,.35)` no CTA.

## Tipografia

Escala reduzida, conforme especificado:

| Papel | Tamanho |
|---|---|
| H1 | 40px desktop / 30px mobile |
| H2 | 30px desktop / 24px mobile |
| H3 | 20px |
| Subheadline/destaque | 16px, line-height 1.6 |
| Corpo | 15px, line-height 1.6 |
| Legendas, FAQ, disclaimers | 13px |

Baloo 2 nos títulos, Plus Jakarta Sans no corpo — os arquivos do Google Fonts,
embutidos em base64 em vez de linkados. Mesmas fontes, mesma renderização, sem
as duas requisições externas e sem o flash de fonte trocando durante o
carregamento. Para voltar ao `<link>` do Google Fonts, é só trocar os dois
blocos `@font-face` no topo do `<style>`.

## Contraste

Todos os pares de texto passam WCAG AA (≥4.5:1), com duas exceções que vêm da
identidade visual definida no briefing:

| Onde | Contraste | Observação |
|---|---|---|
| Rótulo branco no botão CTA laranja | **2.35:1** | branco bold sobre o gradiente, conforme especificado |
| Corpo branco no hero (extremo magenta) | **4.35:1** | o máximo possível sobre `#EC1361`; no extremo roxo dá 5.76:1 |

O bloco de oferta usa texto navy sobre o laranja (5.12–7.14:1) em vez de branco,
que ali daria 2.35:1. Se quiser branco no botão CTA com contraste de verdade, o
caminho é escurecer o gradiente — a partir de `#C24A16` o branco passa em 4.9:1.

## Acessibilidade

HTML semântico, hierarquia de headings sem saltos, `alt` em todas as imagens,
ícones decorativos com `aria-hidden`, skip link, navegação completa por teclado
com anel de foco visível, menu com `aria-expanded`, carrossel focável e
anunciado como região, FAQ em `<details>` e `prefers-reduced-motion` respeitado.
Toda área de toque tem no mínimo 44px.
