#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes exactly one line -- the office printer's comeback -- to
/output/entry.txt (or to the path given as argv[1] / OUTPUT_PATH).
Standard library only, no network, fully deterministic.
"""

import os
import sys

LINE = "I jammed because I read page one and refused to print the rest."


def validate(line: str) -> None:
    """Fail loudly unless the line passes the gate: exactly one line,
    1 to 240 characters, valid UTF-8, not only whitespace."""
    if not isinstance(line, str):
        raise SystemExit("entry line is not a string")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be exactly one line")
    if not (1 <= len(line) <= 240):
        raise SystemExit(
            f"entry line must be 1-240 characters, got {len(line)}"
        )
    if not line.strip():
        raise SystemExit("entry line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> None:
    validate(LINE)
    output_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
