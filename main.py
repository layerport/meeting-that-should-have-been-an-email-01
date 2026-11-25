"""Write one original joke about a meeting that should have been an email.

The program is deliberately deterministic: it always writes the same
single line to ``entry.txt`` inside the output directory, so repeated
runs produce byte-identical files.
"""

import os
from pathlib import Path

# The joke: a "quick sync" about an email that answers nothing, yet
# still spawns a follow-up. The punch lands on the last two words.
ENTRY = (
    "I joined a 'quick sync' about an email and left an hour later "
    "with a follow-up meeting and still no answer."
)

def validate(text: str) -> None:
    """Check the entry against the competition gate before writing it."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if not 1 <= len(stripped) <= 200:
        raise ValueError("entry must be 1-200 characters")


def write_entry(output_dir: str | None = None) -> Path:
    """Write ENTRY to entry.txt in the output directory and return its path."""
    directory = Path(output_dir or os.environ.get("OUTPUT_DIR", "/output"))
    directory.mkdir(parents=True, exist_ok=True)
    validate(ENTRY)
    target = directory / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    return target


def main() -> None:
    target = write_entry()
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
