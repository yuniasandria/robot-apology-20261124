#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession for make.fun.

Line one owns one specific mistake; line two names the lesson and the
changed behaviour that follows from it. Pure standard library only.
The program writes the text to /output/entry.txt, byte-identical on
every run.
"""

import os

OUT_PATH = "/output/entry.txt"

PART_A = (
    "I am sorry I replied-all and sent your draft resignation "
    "letter to the entire company.\n"
)
PART_B = (
    "I learned to read the recipient list twice before sending "
    "anything, because some messages cannot be unsent.\n"
)

TEXT = PART_A + PART_B


def _check(text):
    lines = text.split("\n")
    assert text.endswith("\n"), "text must end with a newline"
    assert len(lines) == 3 and lines[2] == "", "text must be exactly two lines"
    assert 1 <= len(text) <= 400, "text must be 1-400 characters"
    for line in lines[:2]:
        assert line.endswith("."), "each line must be one sentence"
        assert line.count(".") == 1, "each line must be a single sentence"


def main():
    _check(TEXT)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
