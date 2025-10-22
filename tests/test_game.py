from xox.game import TicTacToeGame


def test_winner_rows_columns_diagonals():
    game = TicTacToeGame()

    # Horizontal win
    game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert game.winner() == "X"

    # Vertical win
    game.board = ["O", "X", "X", "O", "X", " ", "O", " ", " "]
    assert game.winner() == "O"

    # Diagonal win
    game.board = ["X", "O", " ", " ", "X", " ", " ", " ", "X"]
    assert game.winner() == "X"


def test_draw_detection():
    game = TicTacToeGame()
    game.board = [
        "X",
        "O",
        "X",
        "X",
        "O",
        "O",
        "O",
        "X",
        "X",
    ]
    assert game.is_draw()


def test_invalid_move_raises():
    game = TicTacToeGame()
    game.board[0] = "X"
    try:
        game.make_move(1)
    except ValueError as exc:
        assert "already occupied" in str(exc)
    else:
        raise AssertionError("Expected ValueError for occupied square")


def test_play_round_switches_players():
    game = TicTacToeGame()
    assert game.current_player == "X"
    winner = game.play_round(5)
    assert winner is None
    assert game.current_player == "O"


def test_play_round_returns_winner_without_switching():
    game = TicTacToeGame()
    game.board = [
        "X",
        "X",
        " ",
        "O",
        "O",
        " ",
        " ",
        " ",
        " ",
    ]
    game.current_player = "X"
    winner = game.play_round(3)
    assert winner == "X"
    assert game.current_player == "X"
