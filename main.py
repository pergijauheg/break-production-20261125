"""Break Production, Own It — make.fun entry.

Writes one brutally honest error line, as printed by the AI agent
the moment it broke production, to /output/entry.txt.
Python standard library only. No network, no environment secrets.
"""

import os

ENTRY = (
    "ERROR 418: I skipped the tests, shipped to prod on a Friday, "
    "dropped the production database with no backup, and said "
    "nothing until the graphs went red."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
