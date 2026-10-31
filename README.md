# Virtual Library (Python)

[Leia em português](README.pt-br.md)

A terminal program to register, list and search books, with a bar chart of how many books there are per genre.

## Features

1. Register a book (title, author, genre and quantity)
2. List all registered books
3. Search by title, author or genre (not case sensitive)
4. Generate a bar chart of books per genre

## How to run

You need Python 3 and the `matplotlib` library.

```
pip install matplotlib
python biblioteca.py
```

You can also paste the code into [Google Colab](https://colab.research.google.com), where `matplotlib` is already installed.

## Concepts practiced

Functions with docstrings, lists, dictionaries, loops, `while` menu, `try/except`, input validation, string methods (`strip`, `lower`), and charts with `matplotlib`.

## Limitations

- Books are stored only in memory: they are lost when the program closes.
- There is no option to edit or remove a book.

## Notes

- College project developed at Anhanguera in 2025.
- The program text is in Portuguese.
