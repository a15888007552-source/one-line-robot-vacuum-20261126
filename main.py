#!/usr/bin/env python3
"""Write the robot vacuum's excuse to entry.txt.

One line, at most 120 characters: the excuse a robot vacuum gives
for missing a spot. The vacuum frames the missed spot as a deliberate
control sample, not a failure.
"""

import os

LINE = (
    "I did not miss that spot. I left it as a control sample, so you "
    "can see how much worse your life would be without me."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    # Final tweak: the line is one sentence, no trailing newline in entry.txt.
    # Second revision: verified the excuse is smug, not apologetic.


if __name__ == "__main__":
    main()
