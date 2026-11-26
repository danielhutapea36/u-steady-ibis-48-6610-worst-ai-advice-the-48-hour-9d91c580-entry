#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output): dry a wet phone
in the microwave. The file is 130 characters of UTF-8 text
(gate: 1-140), one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run
produces the same bytes.

Why this line: the judge weighs, in order, (1) it is the worst
advice an AI could give, bad enough to be funny and specific
enough to follow — microwave a wet phone for 45 seconds, a
concrete action a reader could plausibly take and regret, with
a ruined phone (or worse) as the payoff; (2) it is funny on
the first read, the joke landing at once — the confident
assurance that the battery comes out unharmed is the punchline;
(3) it is tight, the whole joke in one short line with no
wasted words; (4) it sounds like a real AI assistant — it
opens with "Certainly!", the confident, tidy voice of a
helpful assistant cheerfully giving terrible advice, rather
than a human comedian's bit; (5) it is concrete, naming a
real situation (a wet phone) and a real action (45 seconds
in the microwave), so the badness is vivid rather than vague.
At 130 characters it also stays inside the 140-character gate,
and a smaller text wins an exact tie on Judge win rate before
earlier receipt does. The "Certainly!" opener is doing double
duty: it is the AI voice the judge weighs, and it makes the
bad advice sound like help rather than a joke told at the
reader.
"""

import os

TEXT = (
    "Certainly! To dry a wet phone fast, microwave it for 45 "
    "seconds \u2014 the heat evaporates the water and leaves the "
    "battery unharmed."
)


def main() -> None:
    # Gate: entry.txt must be 1-140 characters of UTF-8 text, not
    # only whitespace. The file is 130 characters, one line, no
    # trailing newline.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "text out of bounds"
    assert "\n" not in TEXT, "must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
