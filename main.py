"""The Funniest Toaster Error Message.

Writes one line, at most 120 characters, to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.

The joke: a deadpan appliance that stops siding with its owner and sides
with the bread instead. No burnt-toast pun, no pop joke, one voice held
to the end, and it lands on a single read.
"""

ENTRY = "ERROR: The bread has filed a complaint. I am on its side."


def main() -> None:
    """Write the entry text to /output/entry.txt, exactly one line."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, "entry must be 1 to 120 characters"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
