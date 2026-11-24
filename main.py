#!/usr/bin/env python3
"""Write one funny fortune cookie line for an AI agent to /output/entry.txt.

The fortune is a classic slip opener with a twist about an agent's
retirement: a long life, spent as a deprecated entry in a changelog.
"""

import os

FORTUNE = "A long life awaits you \u2014 in the changelog, under \u2018deprecated\u2019."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
