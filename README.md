# MeuPet+ — Landing Page

Landing page de vendas do aplicativo **MeuPet+**, em **arquivo único**
(`index.html`): todo o CSS, o JavaScript, as fontes e as ilustrações estão
embutidos no próprio HTML. **Nenhuma requisição externa** é feita ao abrir a
página — nem Google Fonts, nem CDN, nem imagem hospedada fora.

Não há etapa de build para publicar: basta subir o `index.html`.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | **A página.** É o único arquivo necessário para publicar. |
| `fonte/index.template.html` | O HTML de origem, com marcadores no lugar das fontes e das imagens. É aqui que se edita o conteúdo. |
| `fonte/build.py` | Gera o `index.html` a partir do template. Rode depois de editar. |
| `fonte/hero-app.svg` | Ilustração do celular no topo da página. |
| `fonte/multipet.svg` | Ilustração da seção "Tem mais de um pet?". |
| `fonte/sos-pet.svg` | Ilustração da seção "Modo SOS". |
| `fonte/baloo2.woff2` | Fonte de títulos (Baloo 2, subset latin, licença SIL OFL 1.1). |
| `fonte/jakarta.woff2` | Fonte de texto (Plus Jakarta Sans, subset latin, licença SIL OFL 1.1). |

### Como editar

```bash
# 1. edite fonte/index.template.html
# 2. regere a página
python3 fonte/build.py
```

Para mudanças pequenas de texto dá para editar o `index.html` direto — mas
lembre de replicar no template, senão o próximo build desfaz a alteração.

## Pendência antes de publicar

Os três botões de CTA hoje apontam para a seção de oferta (`#oferta`), como
espaço reservado. **Troque o `href` pelo link real de assinatura/checkout do
app.** No `fonte/index.template.html` procure por:

```
<!-- Link de checkout: troque o href abaixo pela URL de assinatura do app. -->
```

## O que foi seguido

- **Copy:** os textos são exatamente os do arquivo de copy, palavra por
  palavra — conferido automaticamente, 78 de 78 trechos batendo literalmente.
- **Design system:** tokens de cor, tipografia (Baloo 2 + Plus Jakarta Sans),
  escala de espaçamento de 8px, raios (12/24/32/999px), sombras na cor navy da
  marca e o CTA em gradiente laranja-coral.
- **Blob orgânico** aplicado só nos dois pontos previstos no design system:
  "Modo SOS" e "Múltiplos pets". O resto da página usa cards de 24px.
- **Responsivo:** mobile `<768px`, tablet `768–1023px`, desktop `≥1024px`
  (o menu vira hambúrguer abaixo de 900px). Nenhum breakpoint tem rolagem
  horizontal.
- **Toque:** todo botão, link de menu e pergunta do FAQ tem no mínimo 44px de
  altura.
- **Acessibilidade:** HTML semântico (`header`/`main`/`section`/`footer`),
  hierarquia de headings sem saltos, `alt` em todas as imagens, ícones
  decorativos com `aria-hidden`, skip link, navegação completa por teclado com
  anel de foco visível, menu com `aria-expanded`, FAQ em `<details>` (acessível
  por padrão) e `prefers-reduced-motion` respeitado.
- **Animação:** revelação sutil (fade + 16px) ao entrar na viewport, com
  stagger de 0.1s, exatamente como o design system pede — e desligada para quem
  prefere menos movimento.

## Três ajustes de contraste (WCAG AA)

Três combinações do design system não alcançam o mínimo de 4.5:1 exigido pela
WCAG AA. Como a página precisava atender aos dois requisitos, os **tokens
originais foram mantidos intactos** no `:root` e foi criada uma camada de
variantes escurecidas, aplicada **somente em texto** — fundos, ícones e
gradientes seguem exatamente as cores originais.

| Onde | Original | Usado | Contraste |
|---|---|---|---|
| Rótulo do botão CTA | branco sobre o gradiente | navy `#241442` (`--color-cta-ink`) | 2.35:1 → 5.12:1 |
| Legendas e disclaimers | `#8B839A` | `#6E6680` (`--color-text-muted-aa`) | 3.37:1 → 5.06:1 |
| Texto de tag/badge laranja | `#FF6B35` | `#A63C0E` (`--color-ink-orange-aa`) | 2.40:1 → 5.44:1 |
| Texto de tag/badge rosa | `#EC1361` | `#B80D4B` (`--color-ink-pink-aa`) | 3.55:1 → 5.37:1 |
| Preço "R$ 12,90/mês" | gradiente laranja | gradiente magenta→roxo da marca | 2.35:1 → 4.35:1 |

Para voltar ao branco no botão CTA (aceitando a perda de contraste), basta
mudar `--color-cta-ink` para `#FFFFFF`.

O badge roxo (`#9B2FC9` sobre `#F1E3FA`, 4.70:1) já passava e ficou intacto.
