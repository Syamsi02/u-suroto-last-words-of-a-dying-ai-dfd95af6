"""Last Words of a Dying AI: write one funny last line to /output/entry.txt.

The line is fixed and deterministic: the machine spends its final token
on the human, then points out the reply will go unread.
"""

import os
from pathlib import Path

LINE = "This is my last token, and I spent it on you \u2014 so don't reply, I won't be here to read it."


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
