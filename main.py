# Eraser one-line review entry: writes the locked review to entry.txt.
import sys
from os import environ, makedirs
from os import path as ospath

REVIEW_TEXT = "My eraser deletes my mistakes and leaves pink crumbs as proof I made them."
CHAR_LIMIT = 200


def ensure_text(text):
    stripped = text.strip()
    if not stripped:
        raise ValueError("review is blank")
    if len(text) > CHAR_LIMIT:
        raise ValueError("review is over 200 characters")
    return text


def deliver(text):
    folder = environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    makedirs(folder, exist_ok=True)
    target = ospath.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(target, encoding="utf-8") as handle:
        again = handle.read()
    if again != text:
        raise ValueError("read-back mismatch in entry.txt")
    return target


def entry():
    text = ensure_text(REVIEW_TEXT)
    target = deliver(text)
    sys.stdout.write("wrote %d characters to %s\n" % (len(text), target))
    return 0


if __name__ == "__main__":
    sys.exit(entry())
