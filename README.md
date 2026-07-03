# Corretor de Texto:

Aplicação desktop desenvolvida em **Python** para realizar correção ortográfica e gramatical de textos em português por meio da biblioteca **LanguageTool**. O projeto possui uma interface gráfica simples e intuitiva, permitindo que o usuário insira um texto, visualize as sugestões de correção e copie o resultado com facilidade.

## Funcionalidades:

- Correção ortográfica.
- Correção gramatical.
- Interface gráfica amigável.
- Suporte ao idioma português.
- Copiar o texto corrigido.
- Aplicação desktop para Windows.

---

## Tecnologias utilizadas:

- Python 3
- PySide6 (Interface Gráfica)
- LanguageTool Python
- Qt Designer
- PyInstaller

---

## Interface:

<img width="947" height="759" alt="image" src="https://github.com/user-attachments/assets/2baedfa3-f76a-4676-af5c-e6cc196d4112" />

---

## Gerando o executável:

Para criar um executável (.exe) utilizando o PyInstaller:

```bash
pyinstaller --onefile --windowed --name "Corretor de Texto" --icon=icone.ico --add-data "interface_corretor_de_texto.ui;." --collect-data language_tool_python main.py
```

---

## Objetivo do projeto:

Este projeto foi desenvolvido com o objetivo de praticar:

- Desenvolvimento de aplicações desktop em Python;
- Construção de interfaces gráficas utilizando Qt Designer;
- Manipulação de textos;
- Empacotamento de aplicações com PyInstaller;
- Utilização da biblioteca LanguageTool para processamento de linguagem natural.

---

## 👨‍💻 Autor

**Thiago Yukio**

- GitHub: https://github.com/Thiago-Yukio
