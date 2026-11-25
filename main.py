#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The line is fixed text: it was chosen by a blind pairwise tournament
(6 candidates, 15 pairs) run against the competition's published judge
brief, and confirmed in a both-orders A/B re-check against the runner-up.
Deterministic: the same bytes on every run. Stdlib only, no network.
"""

import os

ENTRY = (
    "One star. He bought me for the bookshelf in his video calls, "
    "then turned me to face the wall for six months so the cactus "
    "could have the light. The cactus is plastic."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    # Gate guard: the sealed scorer needs UTF-8 text of 1-279 chars,
    # not only whitespace, on a single line with no trailing newline.
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start/end with whitespace"
    assert 1 <= len(text) <= 279, f"entry is {len(text)} chars, gate is 1-279"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
