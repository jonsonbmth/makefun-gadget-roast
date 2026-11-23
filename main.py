#!/usr/bin/env python3
"""One Line Roast the Gadget You Use (make.fun bounty).

Writes one roast line to /output/entry.txt and prints it to stdout.
Standard library only; takes no arguments; deterministic.
"""

import os

LINE = "My smart speaker heard 'play jazz' as 'buy a kayak', and now I own a kayak."


def main():
    # The brief: one line, 1 to 200 characters of UTF-8 text.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "written bytes must round-trip exactly"
    print(LINE)


if __name__ == "__main__":
    main()
