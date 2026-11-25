#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): a To: line naming who the unsent message was
meant for, and the unsent message itself, one line, exactly as typed.

The entry is a fixed string constant. This program reads no clock, no
randomness, no network and no files, so every run writes byte-identical
output.
"""

import os
import sys

# The entry: a two-part micro-confession (see SPEC.md section 4).
# To: line names the addressee; the message line is 129 characters,
# under the 200-character cap. The whole file is 138 characters, inside
# the gate's 1-260 character range.
ENTRY = (
    "To: Dad\n"
    "I finally learned to change a tire the week after your funeral, "
    "and I still check the spare every Sunday in case you're watching.\n"
)


def main() -> int:
    # Guard the gate before writing: 1-260 characters total, and the
    # message line itself at most 200 characters, one line, no trailing
    # explanation.
    body = ENTRY.rstrip("\n")
    lines = body.split("\n")
    assert 1 <= len(body) + 1 <= 260, "entry outside the 1-260 gate"
    assert len(lines) == 2, "entry must be exactly two lines"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert len(lines[1]) <= 200, "message line over 200 characters"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
