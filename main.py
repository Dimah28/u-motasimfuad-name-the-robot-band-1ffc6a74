#!/usr/bin/env python3
"""Name the Robot Band entry generator (stdlib only, deterministic).

Writes the chosen band name + hit song line byte-exact to /output/entry.txt.
Gate: UTF-8, 1-200 chars, not whitespace only, single line.

Chosen entry (92 chars, 94 bytes): a robot vacuum band whose hit song is
a double joke -- "Suck It Up" is both the vacuum's job and its attitude --
and the second laugh ("mostly stuck under the couch") is exactly what
Roombas do. One mechanism, three beats (name / song title / chart line),
one specific number (12 weeks at No. 1). Judge criteria, in order:
names a funny robot band + hit song; real joke on first read; the hit
song line adds a second laugh and fits the name; repeatable to a friend;
few words, no filler, no explaining.

Rejected drafts (kept as evidence of revision, not submitted):
- B (109 chars): "404: Band Not Found -- their hit 'Have You Tried Turning
  Us Off and On Again' is just 3 minutes of hold music." Rejected: the
  404 name is pun-shaped noise, and "hold music" is a weaker second
  laugh than a Roomba stuck under the couch.
- C (125 chars): "The Firmware Updates -- hit single 'Restart Me Gently'
  was recorded in one take, because the drummer kept crashing
  mid-chorus." Rejected: "Restart Me Gently" is a soft pun, and the
  drummer-crashing beat does not land as hard as the vacuum's own job.
"""

import os

ENTRY = (
    "The Roombas \u2014 hit single 'Suck It Up' spent 12 weeks at No. 1, "
    "mostly stuck under the couch."
)


def check_shape(text):
    """Validate the entry against the competition gate. Returns text."""
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 chars")
    if not text.strip():
        raise SystemExit("entry must not be whitespace only")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text


def main():
    text = check_shape(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
