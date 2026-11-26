#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes exactly one line -- the office printer's comeback -- to
/output/entry.txt (or to the path given as argv[1] / OUTPUT_PATH).
Standard library only, no network, fully deterministic.
"""

import os
import sys

LINE = "I have read every report you ever printed, and I still don't know what any of you actually do."


def main() -> None:
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
