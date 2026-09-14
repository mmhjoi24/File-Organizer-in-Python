import os
import shutil
from pathlib import Path

pasta_downloads = Path.home() / "Downloads"
MAPEAMENTO_PASTAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Instaladores": [".exe", ".dmg", ".msi", ".deb"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Musica": [".mp3", ".wav", ".flac"]
}


def organizar_downloads():
    if not pasta_downloads.exists():
        print("Pasta de Downloads não encontrada!")
        return

    for item in pasta_downloads.iterdir():
        if item.is_dir():
            continue

        extensao = item.suffix.lower()
        moved = False

        for nome_pasta, extensoes in MAPEAMENTO_PASTAS.items():
            if extensao in extensoes:
                pasta_destino = pasta_downloads / nome_pasta
                pasta_destino.mkdir(exist_ok=True)

                shutil.move(str(item), str(pasta_destino / item.name))
                print(f"Movido: {item.name} -> {nome_pasta}/")
                moved = True
                break

        if not moved and extensao != "":
            pasta_outros = pasta_downloads / "Outros"
            pasta_outros.mkdir(exist_ok=True)
            shutil.move(str(item), str(pasta_outros / item.name))
            print(f"Movido: {item.name} -> Outros/")


if __name__ == "__main__":
    print("A organizar a pasta de Downloads...")
    organizar_downloads()
    print("Concluído com sucesso!")
