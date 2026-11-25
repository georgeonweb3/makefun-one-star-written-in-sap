#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a one-line, one-star review by a houseplant about its human
owner to /output/entry.txt. Stdlib only, deterministic: the same
text is written on every run.
"""

import os

ENTRY = (
    "One star. He bought me for the bookshelf in his video calls, "
    "then turned me to face the wall for six months so the cactus "
    "could have the light. The cactus is plastic."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 279


def main() -> None:
    text = ENTRY
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
