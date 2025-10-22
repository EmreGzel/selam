"""Command line interface for playing Tic-Tac-Toe."""
from __future__ import annotations

from typing import Callable

from .game import TicTacToeGame


def prompt_for_move(prompt: str, input_func: Callable[[str], str] = input) -> int:
    """Prompt the user until a valid board position is provided."""

    while True:
        answer = input_func(prompt)
        answer = answer.strip()
        if not answer:
            print("Lütfen bir sayı girin (1-9).")
            continue
        if not answer.isdigit():
            print("Sadece 1 ile 9 arasındaki sayıları kullanabilirsiniz.")
            continue
        position = int(answer)
        if 1 <= position <= 9:
            return position
        print("Sayı 1 ile 9 arasında olmalıdır.")


def main(input_func: Callable[[str], str] = input) -> None:
    """Play a single game of Tic-Tac-Toe from the command line."""

    game = TicTacToeGame()
    print("Tic-Tac-Toe (XOX) oyununa hoş geldiniz! İlk oyuncu X.")
    while True:
        print()
        print(game.render())
        print()
        position = prompt_for_move(
            f"{game.current_player} oyuncusu, hamlenizi yapın (1-9): ",
            input_func=input_func,
        )
        try:
            winner = game.play_round(position)
        except ValueError as exc:
            print(f"Geçersiz hamle: {exc}")
            continue

        if winner:
            print()
            print(game.render())
            print()
            print(f"Tebrikler {winner}, oyunu kazandın!")
            break

        if game.is_draw():
            print()
            print(game.render())
            print()
            print("Oyun berabere bitti!")
            break

    print("Oyun bitti.")


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
