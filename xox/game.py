"""Game logic for a simple Tic-Tac-Toe (XOX) implementation."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Optional


@dataclass
class TicTacToeGame:
    """A minimal Tic-Tac-Toe engine for two human players.

    The board uses 1-based positions to make the CLI friendlier. Positions are
    laid out as follows::

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
    """

    starting_player: str = "X"
    board: List[str] = field(default_factory=lambda: [" "] * 9)
    current_player: str = field(init=False)

    def __post_init__(self) -> None:
        self.current_player = self.starting_player

    def reset(self, starting_player: Optional[str] = None) -> None:
        """Reset the game to an empty board.

        Parameters
        ----------
        starting_player:
            Optionally override the starting player for the next round.
        """

        self.board = [" "] * 9
        if starting_player is not None:
            self.current_player = starting_player
        else:
            self.current_player = self.starting_player

    def render(self) -> str:
        """Return a human friendly representation of the board."""

        rows = [self.board[i : i + 3] for i in range(0, 9, 3)]
        display_rows = [" | ".join(row) for row in rows]
        return "\n---------\n".join(display_rows)

    def available_moves(self) -> Iterable[int]:
        """Yield the 1-based indices for empty squares."""

        return (index + 1 for index, value in enumerate(self.board) if value == " ")

    def make_move(self, position: int) -> None:
        """Place the current player's mark on the board.

        Raises
        ------
        ValueError
            If the requested position is outside the range 1-9 or already
            occupied.
        """

        if position < 1 or position > 9:
            raise ValueError("Position must be between 1 and 9.")

        index = position - 1
        if self.board[index] != " ":
            raise ValueError("That square is already occupied.")

        self.board[index] = self.current_player

    def switch_player(self) -> None:
        """Swap to the other player's turn."""

        self.current_player = "O" if self.current_player == "X" else "X"

    def winner(self) -> Optional[str]:
        """Return the winner symbol ("X" or "O") if the game is won."""

        winning_lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for first, second, third in winning_lines:
            line = (self.board[first], self.board[second], self.board[third])
            if line[0] != " " and line.count(line[0]) == 3:
                return line[0]
        return None

    def is_draw(self) -> bool:
        """Return ``True`` if the game has no empty squares and no winner."""

        return self.winner() is None and all(square != " " for square in self.board)

    def is_over(self) -> bool:
        """Return ``True`` if the game has ended with a win or a draw."""

        return self.winner() is not None or self.is_draw()

    def play_round(self, position: int) -> Optional[str]:
        """Execute a turn and return the winner if the game ended.

        The method performs a move, checks whether the game has ended, and
        switches players if needed.

        Parameters
        ----------
        position:
            1-based index of the square to fill.

        Returns
        -------
        Optional[str]
            The winning player's symbol, ``"X"`` or ``"O"``. ``None`` if the
            game should continue. A draw can be detected via :meth:`is_draw`.
        """

        self.make_move(position)
        winner = self.winner()
        if winner or self.is_draw():
            return winner

        self.switch_player()
        return None
