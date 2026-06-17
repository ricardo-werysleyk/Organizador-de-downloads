# Organizador Automático de Arquivos

Um programa em Python que organiza automaticamente os arquivos de uma pasta em subdiretórios de acordo com suas extensões.

Projeto criado para praticar manipulação de arquivos utilizando o módulo `os`.

## Funcionalidades

* Leitura de arquivos de uma pasta escolhida pelo usuário
* Ignora diretórios existentes
* Identifica extensões automaticamente
* Cria pastas quando necessário
* Move arquivos para categorias apropriadas
* Valida se o caminho informado existe

Exemplo:

Antes:

```text
Downloads/
├── imagem.png
├── documento.pdf
├── codigo.py
├── video.mp4
```

Depois:

```text
Downloads/
├── Imagens/
│   └── imagem.png
├── Documentos/
│   └── documento.pdf
├── Codigo/
│   └── codigo.py
└── Videos/
    └── video.mp4
```

## Tecnologias utilizadas

* Python 3
* os
* shutil

## Como executar

Clone o projeto:

```bash
git clone <url-do-repositorio>
```

Entre na pasta:

```bash
cd organizador-arquivos
```

Execute:

```bash
python organizador.py
```

ou

```bash
py organizador.py
```

Digite o caminho da pasta que deseja organizar.

Exemplo:

```text
C:\Users\Usuario\Downloads
```

## Estrutura

```text
organizador-arquivos/
├── organizador.py
└── README.md
```

## Melhorias futuras

* [ ] Interface gráfica
* [ ] Relatório final de arquivos movidos
* [ ] Configuração personalizada de categorias
* [ ] Modo simulação (não mover arquivos)