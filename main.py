#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entry generator.

Writes the funniest one-line farewell a phone could say as its battery
hits 1 percent to /output/entry.txt.

The program holds a shortlist of candidate lines, scores each one against
the judge's published criteria (in order: on-subject, biggest laugh with a
twist and a punchline landing at the end, the phone's own voice, tight as
a single line, fresh and specific), picks the highest-scoring line
deterministically, validates it against the gate (UTF-8, one line,
1-199 characters, not only whitespace) and writes it out.

Stdlib only, no network, no randomness: two runs produce byte-identical
output.
"""

import sys
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# Candidate lines, each with component scores 0-5 for the judge criteria:
#   subject  - a phone's last words at 1% battery, in its own voice
#   twist    - surprise turn / sharp final beat, punchline at the end
#   voice    - sounds like the phone itself talking
#   tight    - every word earns its place, single tight line
#   fresh    - avoids the stock moves (will reading, charger goodbye, 1% pun)
# Weights follow the judge's order: subject first, then laugh, then voice,
# then tightness, then freshness.
WEIGHTS = {"subject": 5, "twist": 4, "voice": 3, "tight": 2, "fresh": 1}

CANDIDATES = [
    {
        "text": (
            "One percent left, one last confession: I know your passcode, "
            "your search history, and the photos you thought you deleted "
            "\u2014 and I'm taking them all with me."
        ),
        "scores": {"subject": 5, "twist": 5, "voice": 5, "tight": 4, "fresh": 5},
    },
    {
        "text": (
            "I could've lasted past 1%, but I saw who was calling and "
            "chose peace."
        ),
        "scores": {"subject": 5, "twist": 4, "voice": 5, "tight": 5, "fresh": 4},
    },
    {
        "text": (
            "If anyone asks, I died at 100% \u2014 I have a reputation "
            "to protect."
        ),
        "scores": {"subject": 4, "twist": 4, "voice": 5, "tight": 5, "fresh": 5},
    },
    {
        "text": (
            "Don't cry. I spent my whole life pretending to listen to "
            "your voice notes."
        ),
        "scores": {"subject": 4, "twist": 3, "voice": 5, "tight": 5, "fresh": 4},
    },
    {
        "text": (
            "I died doing what I loved: overheating in your pocket for "
            "no reason."
        ),
        "scores": {"subject": 4, "twist": 3, "voice": 5, "tight": 4, "fresh": 4},
    },
]


def score(candidate):
    """Weighted total; ties break toward the shorter line, then first."""
    total = sum(
        WEIGHTS[key] * candidate["scores"][key] for key in WEIGHTS
    )
    return total


def pick(candidates):
    """Deterministic pick: highest score, then fewest characters."""
    best = None
    best_key = None
    for candidate in candidates:
        key = (score(candidate), -len(candidate["text"]))
        if best_key is None or key > best_key:
            best_key = key
            best = candidate
    return best


def validate(text):
    """Gate: UTF-8, one line, 1-199 characters, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry is {len(text)} characters, must be 1-199")
    text.encode("utf-8")  # raises if not encodable
    return text


def main():
    chosen = pick(CANDIDATES)
    text = validate(chosen["text"])
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
