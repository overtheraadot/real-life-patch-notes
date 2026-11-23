#!/usr/bin/env python3
"""Real-Life Patch Notes entry (make.fun program/v1).

Writes one original patch note to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``). The line is a
software release note for a bug in human biology: knees that started
creaking on stairs after 30 years of silent operation.
"""

import os
import sys

LINE = "v2.0.1: fixed a bug where knees started creaking on stairs after 30 years of silent operation."


def main() -> int:
    # Gate guard: the sealed scorer only accepts UTF-8 text of 1-160
    # characters, a single line, not only whitespace. Refuse to write
    # anything outside the gate instead of submitting an invalid entry.
    if not (1 <= len(LINE) <= 160):
        print(f"gate: line is {len(LINE)} chars, must be 1-160", file=sys.stderr)
        return 1
    if "\n" in LINE or not LINE.strip():
        print("gate: line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
