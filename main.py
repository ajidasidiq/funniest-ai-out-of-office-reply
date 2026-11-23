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


def main() -> None:
    line = validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != line:
        raise RuntimeError("entry.txt does not match the validated line")
    print(line)


if __name__ == "__main__":
    main()
