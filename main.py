"""The Funniest AI Out-of-Office Reply — a make.fun bounty entry.

The program writes one out-of-office auto-reply, a single line under
160 characters, to /output/entry.txt, then reads the file back to confirm
it holds exactly the validated line.
"""

from pathlib import Path

ENTRY = "I'm on vacation. I left my email with a human intern who has already emailed me twice asking how to answer emails. We are both out of office."

MAX_CHARS = 160
OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Return the line if it passes the gate, else raise."""
    text = line.strip()
    if not text:
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def verify_round_trip(line: str) -> None:
    """Check the written file round-trips byte-identical to the line.

    Reads the raw bytes (not decoded text) so a trailing newline, a
    stray carriage return, or any encoding change is caught instead of
    silently normalised away by the text decoder.
    """
    raw = OUTPUT_PATH.read_bytes()
    expected = line.encode("utf-8")
    if raw != expected:
        raise RuntimeError(
            f"entry.txt is {len(raw)} bytes, expected {len(expected)} "
            "bytes of the validated line"
        )
    if raw.endswith(b"\n") or raw.endswith(b"\r"):
        raise RuntimeError("entry.txt must not end with a newline")
    if b"\n" in raw or b"\r" in raw:
        raise RuntimeError("entry.txt must be a single line")


def main() -> None:
    line = validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    verify_round_trip(line)
    print(line)


if __name__ == "__main__":
    main()
