# Biblioteca Virtual (Python)

[Read in English](README.md)

Programa de terminal para cadastrar, listar e pesquisar livros, com um gráfico de barras da quantidade de livros por gênero.

## Funcionalidades

1. Cadastrar livro (título, autor, gênero e quantidade)
2. Listar todos os livros cadastrados
3. Pesquisar por título, autor ou gênero (sem diferenciar maiúsculas de minúsculas)
4. Gerar um gráfico de barras com os livros por gênero

## Como executar

É preciso ter o Python 3 e a biblioteca `matplotlib`.

```
pip install matplotlib
python biblioteca.py
```

Você também pode colar o código no [Google Colab](https://colab.research.google.com), onde o `matplotlib` já vem instalado.

## Conceitos praticados

Funções com docstrings, listas, dicionários, laços, menu com `while`, `try/except`, validação de entrada, métodos de texto (`strip`, `lower`) e gráficos com `matplotlib`.

## Limitações

- Os livros ficam só na memória: são perdidos quando o programa fecha.
- Não há opção para editar ou remover um livro.

## Observações

- Projeto da faculdade, desenvolvido na Anhanguera em 2025.
- Os textos do programa estão em português.
