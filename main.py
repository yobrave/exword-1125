import json
import os
import pathlib

STAMP = "exword-1125-r1"
HERE = pathlib.Path(__file__).resolve().parent
LINE = (HERE / "entry.txt").read_text(encoding="utf-8").strip()


def audit(text):
    if not text or not text.strip():
        raise ValueError("blank entry")
    if len(text) > 24:
        raise ValueError(f"gate allows 1..24 chars, got {len(text)}")
    if len(text.split()) != 1:
        raise ValueError("exactly one word required")
    return text


def deliver(text):
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes((text + "\n").encode("utf-8"))
    return str(out / "entry.txt")


report = {"word": audit(LINE), "wrote": deliver(LINE), "status": "ok", "stamp": STAMP}
print(json.dumps(report, ensure_ascii=False))
print(f"run {STAMP} complete")
