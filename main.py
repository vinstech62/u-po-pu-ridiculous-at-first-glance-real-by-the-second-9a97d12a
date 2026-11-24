#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

One sentence pitching a bizarre startup idea that sounds absurd until
you realise it would actually sell, written to /output/entry.txt.

Deterministic: the same line every run, no input, no network, no
randomness. Verified 2026-11-24: the line is 147 characters (149 UTF-8
bytes), one sentence, and two consecutive runs wrote byte-identical
/output/entry.txt (mode 644). The pitch works the brief's turn: crows as
a litter crew sounds like a joke, then the second look lands — cities
already spend millions sweeping cigarette butts up, so paying per kilo
pencils out, and the workforce literally works for peanuts.
"""

import os

LINE = (
    "We train crows to collect cigarette butts \u2014 cities already spend "
    "millions sweeping them up, so they pay us per kilo and the birds work "
    "for peanuts."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
