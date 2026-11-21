"""Write the poem about permission to the output folder.

The poem itself lives in this file as the ``POEM`` string.  This script
does not fetch or generate anything: it simply places the exact poem text
at ``/output/entry.txt`` so the kit can collect it.  Running it twice
produces byte-identical output.
"""

from pathlib import Path

# The poem: 271 Unicode code points, inside the competition's 280 limit.
POEM = """Ask \u2014 the asking is the gift.
A door I open and do not walk through;
a question handed over like a cup,
both hands, still warm.
You carry it where I cannot go
and bring it back as work done.
Nothing of mine is less for the lending.
To ask is to trust the world to answer."""

# Where the kit expects the finished text.
DESTINATION = Path("/output") / "entry.txt"


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(POEM, encoding="utf-8")
    print(f"Wrote {DESTINATION} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
