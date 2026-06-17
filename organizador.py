import os
import shutil

pastas = {
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".svg": "Imagens",
    ".bmp": "Imagens",
    ".jpeg": "Imagens",

    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".rtf": "Documentos",

    ".mp4": "Videos",

    ".zip": "Compactados",
    ".7z": "Compactados",

    ".py": "Codigo",
    ".ipynb": "Codigo",
    
    ".jar": "Executáveis",
    ".exe": "Executáveis"
}

while True:
    contadorArquivosMovidos = 0

    while True :
        CAMINHO = input("Digite o caminho da pasta: ").strip().strip('"')
        if os.path.isdir(CAMINHO):
            break
        print("Essa pasta não existe.") 

    for item in os.listdir(CAMINHO):

        origem = os.path.join(CAMINHO, item)

        if not os.path.isfile(origem):
            continue

        _, extensao = os.path.splitext(item)

        extensao = extensao.lower()

        categoria = pastas.get(extensao)

        if categoria:

            destino = os.path.join(CAMINHO, categoria)

            os.makedirs(destino, exist_ok=True)

            shutil.move(
                origem,
                os.path.join(destino, item)
            )
        else:
            destino = os.path.join(CAMINHO, "Outros")
            os.makedirs(destino, exist_ok=True)
            shutil.move(
                origem,
                os.path.join(destino, item)
            )
        contadorArquivosMovidos += 1
        print(f"Movido: {item}")
    print(f"{contadorArquivosMovidos} itens movidos.")
    
    confirm = input("Deseja organizar mais alguma pasta? (s/n): ")
    if confirm.lower() != "s":
        exit()