#!/usr/bin/env python3
"""Name the Robot Band (cap 200): name plus hit song required.

Competition: u-motasimfuad-name-the-robot-band-1ffc6a74

Backstage deliberation
----------------------
The Loose Bolts offered 'I Left My Heart in the Charging Dock'.
A tidy country ballad for machines, and the dock gag is sweet,
but the band name itself does little work beside the song.
Ctrl+Alt+Defeat brought 'Dancing With 4% Battery'. The keyboard
name is the sort of pun a reader has met before, and the song
mostly repeats its energy joke.
Rust in Peace takes the slot because both halves fire: the name
is a headstone joke a metal band of robots would actually tour
under, and the hit single, 'Your Update Is Ready (Please Restart
Me Gently)', turns a dreaded system prompt into a love song. Two
laughs, no filler, and a name you would repeat to a friend.
"""

import os
from pathlib import Path

BAND_LINE = (
    "Rust in Peace \u2014 hit single: 'Your Update Is Ready "
    "(Please Restart Me Gently)'"
)

STAGE_CAP = 200


def check_lineup(text: str) -> None:
    # A band announcement without its hit single is just a name;
    # the gate below refuses to let that version take the stage.
    if not (1 <= len(text) <= STAGE_CAP):
        raise SystemExit("band line outside the gate")
    if "hit single" not in text:
        raise SystemExit("the brief demands a hit song")


def perform() -> None:
    check_lineup(BAND_LINE)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(BAND_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    perform()

# Tour rider: one charging dock per member, no stairs on stage,
# and absolutely no firmware updates during the encore.
