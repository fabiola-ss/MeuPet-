#!/usr/bin/env python3
"""Gera o index.html final (arquivo único) a partir de fonte/index.template.html.

Substitui os marcadores do template pelos data URIs das fontes e das
ilustracoes, para que a pagina publicada nao faca nenhuma requisicao externa.

    python3 fonte/build.py
"""

import base64
import pathlib

BASE = pathlib.Path(__file__).resolve().parent
RAIZ = BASE.parent

SUBSTITUICOES = {
    "__FONT_BALOO__": ("baloo2.woff2", "raw"),
    "__FONT_JAKARTA__": ("jakarta.woff2", "raw"),
    "__IMG_HERO__": ("hero-app.svg", "svg"),
    "__IMG_MULTIPET__": ("multipet.svg", "svg"),
    "__IMG_SOS__": ("sos-pet.svg", "svg"),
}


def main() -> None:
    html = (BASE / "index.template.html").read_text(encoding="utf-8")

    for marcador, (arquivo, tipo) in SUBSTITUICOES.items():
        dados = (BASE / arquivo).read_bytes()
        b64 = base64.b64encode(dados).decode("ascii")
        valor = b64 if tipo == "raw" else "data:image/svg+xml;base64," + b64
        if marcador not in html:
            raise SystemExit("marcador ausente no template: " + marcador)
        html = html.replace(marcador, valor)

    destino = RAIZ / "index.html"
    destino.write_text(html, encoding="utf-8")
    print("index.html gerado com {:.0f} KB".format(destino.stat().st_size / 1024))


if __name__ == "__main__":
    main()
