import json
import os
import sys
from pathlib import Path

BOUND = 24
STAMP = "ex-word-1125"

word_file = Path(__file__).resolve().with_name("entry.txt")

if not word_file.exists():
    print(json.dumps({"verdict": "absent", "bound": BOUND}))
    sys.exit(1)

raw = word_file.read_text(encoding="utf-8")
pick = ""
for line in raw.replace("\r", "").split("\n"):
    if line.strip():
        pick = line.strip()
        break

if (n := len(pick)) < 1 or n > BOUND:
    print(json.dumps({"verdict": "out-of-bound", "bound": BOUND, "n": n}))
    sys.exit(1)

box = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
box.mkdir(parents=True, exist_ok=True)
(box / "entry.txt").write_bytes(pick.encode("utf-8"))
print(json.dumps({"verdict": "one-word-ok", "n": n, "bound": BOUND, "stamp": STAMP,
                  "round": "r21"}))
