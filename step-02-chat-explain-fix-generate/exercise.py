from typing import Optional

def parse_scoreboard(raw: str) -> dict[str, int]:
    """Parse 'name:score' pairs separated by commas.

    Example: "alice:10,bob:9,alice:14" -> {"alice": 14, "bob": 9}

    Invalid segments should be skipped.
    """
    board: dict[str, int] = {}
    if raw == "":
        return board

    parts = raw.split(",")
    for part in parts:
        try:
            segments = part.split(":")
            if len(segments) != 2:
                continue
            name, score = segments
            name = name.strip().lower()
            value = int(score.strip())
            board[name] = value
        except ValueError:
            continue
    return board


def top_player(board: dict[str, int]) -> Optional[tuple[str, int]]:
    """Return the player with the highest score, else None.

    Keep this deterministic by sorting names alphabetically when scores tie.
    """
    if not board:
        return None
    
    max_score = max(board.values())
    top_name = min(name for name, score in board.items() if score == max_score)
    return (top_name, max_score)


if __name__ == "__main__":
    print(parse_scoreboard("Alice: 10, Bob: 15, Alice: 20, bad, Tom: nope"))
    print(top_player(parse_scoreboard("Alice: 10, Bob: 15, Alice: 20")))
    print(top_player({}))