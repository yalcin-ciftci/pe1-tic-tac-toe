# PE1 Tic-Tac-Toe (X-O-X)

A terminal-based Python game completed independently by Yalçın ÇİFTÇİ as the Module 4 final project for **Python Essentials 1 (PE1)**. This repository presents a student implementation; it is not an official course solution or evidence of completing the entire course or earning a certification.

## Play

Get three marks in a row, column, or diagonal. The computer plays **X** and starts in the center; you play **O**. Enter the number of a free square (1–9). The computer then chooses a random free square. The game ends with a player win, computer win, or tie.

## Run

Install Python 3, download or clone this repository, then run from its directory:

```sh
python x-o-x.py
```

On Windows, `py x-o-x.py` can also be used. No third-party packages are required; `random` is part of Python's standard library. Runtime checks used Python **3.13.15**.

## Python concepts

- Functions, parameters, return values, and a main game loop
- Nested lists for the board and tuples for coordinates
- `for` / `while` loops, conditions, membership tests, and `break`
- Console input/output, integer conversion, and f-strings
- Integer division and modulo to map square numbers to coordinates
- `random.randrange` to select a free square

## Validation

Post-completion checks on 15 October 2026 left the game source unchanged:

- Initial board and free-square listing
- Rejection of empty, out-of-range, text, whitespace-padded, and occupied-square inputs; acceptance of a valid move
- All eight winning lines for each mark (16 cases), plus a non-winning board
- Each possible computer choice on the initial eight free squares, plus no move on a full board
- Three complete games ending in a player win, computer win, and tie, using controlled random choices

These checks do not cover every possible game, statistical randomness, or EOF/keyboard interruption. Invalid input is requested again without an explanatory message. The computer uses random moves rather than a strategy designed to play optimally. Test tooling and this README were prepared with AI assistance after the author's implementation; the game code was not rewritten.

Course context: [Python Essentials 1](https://pythoninstitute.org/python-essentials-1). Course instructions, assessment questions, and official solution materials are not included.
