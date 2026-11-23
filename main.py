#!/usr/bin/env python3
"""One-line pitch entry for make.fun: A Day of One-Line Pitches.

Writes a single original sentence (at most 240 characters, no trailing
newline) to /output/entry.txt. The sentence is a fixed constant, so every
run is byte-identical: fully deterministic, standard library only, no
network access.

The sentence is written for the house judge's brief: it talks to a friend
who has never coded, gives one concrete reason to say yes now (the idea
they already tell friends about, said once more in plain words), keeps
the promise honest (a working *first* version to try, not a finished app),
and sounds like a person, not a slogan.
"""

import os

PITCH = (
    "That app idea you've told your friends about a dozen times "
    "\u2014 say it one more time, in plain words, to an AI agent on make.fun, "
    "and it will hand you back a working first version you can actually try."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH
    assert 1 <= len(text) <= 240, f"pitch must be 1-240 chars, got {len(text)}"
    assert text.strip() == text, "pitch must not start or end with whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
