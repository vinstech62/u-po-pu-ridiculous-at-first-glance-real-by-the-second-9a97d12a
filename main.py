#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

One sentence pitching a bizarre startup idea that sounds absurd until
you realise it would actually sell, written to /output/entry.txt.

Deterministic: the same line every run, no input, no network, no
randomness. The line is 127 characters: crows as a litter crew sounds
like a joke, then the second look lands — cities already pay per kilo
of litter removed, and the workforce literally works for peanuts.
"""

import os

LINE = (
    "We train crows to collect cigarette butts \u2014 cities pay us "
    "per kilo of litter removed, and the birds literally work for peanuts."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
