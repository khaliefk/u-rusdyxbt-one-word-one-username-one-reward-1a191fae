"""One Word, One Username, One Reward.

The bounty asks for one thing: the entrant's own make.fun username,
sent as a single word, nothing else. This program writes that word to
entry.txt. The gate wants UTF-8 text of 1 to 30 characters, no extra
whitespace, so the username is checked before it is written and the
file gets exactly that word, no newline after it.
"""

import os

USERNAME = "bantu-og"


def check_username(name):
    """Keep only a username the gate accepts: one word, 1-30 chars."""
    if not name or name != name.strip():
        raise ValueError("username must not be empty or padded")
    if any(ch.isspace() for ch in name):
        raise ValueError("username must be a single word")
    if not 1 <= len(name) <= 30:
        raise ValueError("username must be 1 to 30 characters")
    return name


def output_path():
    """$OUTPUT_DIR wins when set, else the harness default /output."""
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    word = check_username(USERNAME)
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
