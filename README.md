# MeuPet+ — Landing Page

Página de vendas do aplicativo **MeuPet+**, em **arquivo único** (`index.html`):
CSS, JavaScript, fontes e imagens estão todos embutidos. **Nenhuma requisição
externa** ao abrir a página. Sem framework, sem etapa de build no deploy —
o `index.html` sozinho já é o site.

## Publicar no Netlify

**Add new site → Import an existing project → GitHub → fabiola-ss/MeuPet-**

- **Branch to deploy:** `claude/landing-page-html-css-js-kzivtn`
- **Build command:** deixe **vazio**
- **Publish directory:** `.` (um ponto)

Todo push nessa branch republica o site.

## Antes de publicar: dois pendentes

### 1. Link de checkout

Os três CTAs apontam para a seção de oferta (`#oferta`) como espaço reservado.
Troque pelo link real de assinatura. Procure no `fonte/index.template.html`:

```
<!-- Link de checkout: troque o href abaixo pela URL de assinatura do app. -->
```

### 2. Fotos reais de pet

O layout já está montado para foto real em dois pontos — hero e Modo SOS — mas
os arquivos ainda não estão no repositório. Enquanto não estiverem, uma
ilustração ocupa o lugar. Para trocar, coloque os arquivos em `fonte/` e rode o
build:

```bash
# baixe do Unsplash (licença livre) e salve como:
#   fonte/foto-hero.jpg   faixa horizontal (~3:1), rosto do pet centralizado
#   fonte/foto-sos.jpg    quadrada (1:1), o recorte vira blob orgânico
python3 fonte/build.py
```

O script detecta os arquivos sozinho — `.jpg`, `.jpeg`, `.png` ou `.webp` — e
embute cada um no `index.html`. Nada mais precisa ser editado. Sugestões de
busca no Unsplash: *happy dog portrait*, *cat portrait studio*.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | **A página.** Único arquivo necessário para publicar. |
| `fonte/index.template.html` | HTML de origem, com marcadores no lugar das fontes e imagens. É aqui que se edita. |
| `fonte/build.py` | Gera o `index.html`. Rode depois de qualquer edição. |
| `fonte/retrato-pet.svg` | Ilustração provisória do hero (some quando `foto-hero.jpg` existir). |
| `fonte/sos-pet.svg` | Ilustração provisória do Modo SOS (some quando `foto-sos.jpg` existir). |
| `fonte/hero-app.svg` | Mockup do app na seção "A virada". |
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
| 7 | Modo SOS | **sólido** — navy-plum escuro, texto branco (blob na foto) | onda ↑ e ↓ |
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
