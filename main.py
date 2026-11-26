"""One-Liner Laugh Lab entry.

Joke design: a robot vacuum files a deadpan incident report about a
sock it "neutralized" — bureaucratic language, an escalating cover-up,
then a flat denial of memory. The humour lives in the tone, not in a
punchline word, so every sentence stays in the same report voice.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

SETUP = "Incident report: the unmatched sock threatened household order and was neutralized."
PUNCHLINE = "Its partner has been filed as a missing person. I regret nothing; I remember nothing."


def build_line():
    """Assemble the entry from its two report-style fragments."""
    return SETUP + " " + PUNCHLINE


def validate(line):
    """The entry must be exactly one non-empty line under the limit."""
    if not line or "\n" in line or len(line) > MAX_CHARS:
        raise ValueError("entry must be a single line of at most 200 chars")


def main():
    line = build_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise RuntimeError("written entry does not match the line")


if __name__ == "__main__":
    main()
