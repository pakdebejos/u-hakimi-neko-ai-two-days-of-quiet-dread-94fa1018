"""Heat Death on Schedule: one code review comment approving a PR with quiet dread.

The program writes one code review comment - a single line of at most 140
characters (91 characters) that approves a pull request while carrying quiet existential
dread - to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader). The text is a fixed
constant with no trailing newline, so both of the grader's runs write
byte-identical output.
"""
import os

COMMENT = """Approved. It works, the tests pass, and the heat death of the universe remains on schedule."""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(COMMENT)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
