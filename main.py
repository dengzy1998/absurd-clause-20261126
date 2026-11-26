#!/usr/bin/env python3
"""The Absurd Clause Contest entry (make.fun).

Writes the winning clause to /output/entry.txt.

Duel record (proxy judge: openai/gpt-oss-120b via Groq, using the judge brief
published verbatim in the kit's RULES.txt; each pair judged in both orders,
verdict format `VERDICT: A|B MARGIN: 1-5`):

Candidates (all original, one sentence, <=200 chars):
  C1 (163): borrow your name for one haunted house per year, returned slightly haunted
  C2 (164): on death, account inherited by least favorite cousin, else forfeited to the Company's cat
  C3 (132): no suing in any court above sea level, incl. mountains, airplanes, tall stools
  C4 (149): disputes settled by arm-wrestling the Company's champion, retired lighthouse keeper Gus
  C5 (152): cancel only by handwritten letter in a bottle, delivered by a tide of our choosing
  C6 (148): profile picture replaced with the founder's dog on holidays, birthdays, Tuesdays

Round 1:
  C2 beat C1 2-0 (margins 4, 4) - cousin-to-cat inheritance beat the haunted-house name loan
  C3 vs C4 tied 1-1 (margins 4, 4) - each won once, as Entry B
  C5 beat C6 2-0 (margins 4, 4) - letter-in-a-bottle beat the founder's dog
Final:
  C2 beat C5 2-0 (margins 3, 4) - the judge called the morbid inheritance twist
  with the corporate cat a bigger, more self-contained punchline than the
  letter-in-a-bottle gag.

Champion: C2. It won because it is the most concrete and self-contained
absurdity: death, inheritance, a least favorite cousin, a 30-day deadline,
and the Company's cat, all in deadpan legal register, landing on one reading
with no setup.

Usage: python3 main.py  -- writes the clause to /output/entry.txt exactly
as-is (single line, no trailing newline).
"""

from pathlib import Path

ENTRY = (
    "If you die while using the Service, your account will be inherited by "
    "your least favorite cousin, who must log in within 30 days or forfeit "
    "it to the Company's cat."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
