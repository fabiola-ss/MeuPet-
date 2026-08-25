#!/usr/bin/env python3
"""Gera o index.html final (arquivo único) a partir de fonte/index.template.html.

Troca os marcadores do template pelos data URIs das fontes e das imagens, para
que a página publicada não faça nenhuma requisição externa.

    python3 fonte/build.py

Os prints do aplicativo ficam em fonte/prints/ em WebP. Para trocar algum,
substitua o arquivo e rode este script de novo.
"""

import base64
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent
RAIZ = BASE.parent

TIPOS = {
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".png": "image/png", ".webp": "image/webp", ".svg": "image/svg+xml",
}

# marcador -> (nomes preferidos em ordem, é fonte?)
ALVOS = [
    ("__FONT_BALOO__",   ["baloo2.woff2"],                       True),
    ("__FONT_JAKARTA__", ["jakarta.woff2"],                      True),
    ("__PRINT_MEUSPETS__", ["prints/app-meus-pets.webp"],        False),
    ("__PRINT_HISTORICO__", ["prints/app-historico.webp"],       False),
    ("__PRINT_SOS__",      ["prints/app-modo-sos.webp"],         False),
    ("__PRINT_REMEDIO__",  ["prints/app-lembrete-remedio.webp"], False),
]


def achar(nome: str) -> pathlib.Path | None:
    """Resolve um nome com extensão, ou procura o primeiro formato disponível."""
    if "." in nome:
        caminho = BASE / nome
        return caminho if caminho.exists() else None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        caminho = BASE / (nome + ext)
        if caminho.exists():
            return caminho
    return None


def main() -> None:
    html = (BASE / "index.template.html").read_text(encoding="utf-8")
    avisos = []

    for marcador, candidatos, e_fonte in ALVOS:
        if marcador not in html:
            sys.exit("marcador ausente no template: " + marcador)

        escolhido = next((p for p in map(achar, candidatos) if p), None)
        if escolhido is None:
            sys.exit("nenhum arquivo encontrado para " + marcador)

        if escolhido.name == candidatos[-1] and len(candidatos) > 1:
            avisos.append("  {}: usando a ilustração {} (coloque {}.jpg em fonte/ para trocar pela foto real)"
                          .format(marcador, escolhido.name, candidatos[0]))

        b64 = base64.b64encode(escolhido.read_bytes()).decode("ascii")
        valor = b64 if e_fonte else "data:{};base64,{}".format(TIPOS[escolhido.suffix.lower()], b64)
        html = html.replace(marcador, valor)

    destino = RAIZ / "index.html"
    destino.write_text(html, encoding="utf-8")
    print("index.html gerado com {:.0f} KB".format(destino.stat().st_size / 1024))
    if avisos:
        print("\nfotos pendentes:")
        print("\n".join(avisos))


if __name__ == "__main__":
    main()
