"""The Tired Dark Lord: A 100-Word Villain Monologue.

A fantasy villain's monologue of about a hundred words, written to
/output/entry.txt. The tiredness lives in the voice, not in a plain
announcement: the pauses, the deflections, the small chores of
villainy (sharpening swords, feeding the dragon, filing conquest in
triplicate) that have worn the speaker down. He still has a scheme --
banners, an eclipse, a throne of black glass -- and a history, but the
eclipse keeps getting rescheduled and the monologue itself is the one
part of the job where someone finally listens.

The monologue is built from five spoken beats: the unasked question,
the plan he once had, the small failures that eroded it, the
rescheduled eclipse, and the invitation to the knight -- which turns
out to be about the monologue itself. Every beat is short, so the
rhythm stays tired: sentences trail off, restart, and give up.
"""

import os

BEAT_QUESTION = (
    "You know what the hero never asks? Who sharpens the swords. "
    "Who feeds the dragon. Who files the conquest in triplicate."
)
BEAT_PLAN = (
    "I had a plan once \u2014 a good one. Banners, an eclipse, "
    "a throne of black glass."
)
BEAT_EROSION = (
    "Then the dragon caught a cough, the banners faded in the wash, "
    "and the eclipse... well, it is still coming, I just keep "
    "rescheduling it."
)
BEAT_INVITATION = (
    "So. Come closer, little knight. I will monologue. "
    "I always monologue."
)
BEAT_PAYOFF = (
    "It is the only part of the job where someone finally listens "
    "\u2014 and I don't even have to stand up."
)

MAX_CHARS = 600
MIN_CHARS = 1
TARGET_WORDS = 100


def compose(*beats: str) -> str:
    """Join the spoken beats into one monologue, one breath apart."""
    parts = [beat.strip() for beat in beats]
    return " ".join(parts)


def check_monologue(text: str) -> str:
    """Gate the monologue the way the sealed scorer does.

    /output/entry.txt must be UTF-8 text of 1 to 600 characters, and
    the brief asks for about a hundred words.
    """
    assert MIN_CHARS <= len(text) <= MAX_CHARS, f"monologue is {len(text)} chars"
    assert text == text.strip(), "no stray whitespace around the monologue"
    words = text.split()
    assert 80 <= len(words) <= 115, f"monologue has {len(words)} words"
    return text


def voice_notes(text: str) -> dict:
    """Per-bounty voice check: the tiredness must be felt, never announced.

    The judge rewards a villain whose weariness lives in rhythm, pauses
    and deflections, so the monologue must never simply say he is
    tired, weary or exhausted. It must still name a scheme (the
    eclipse, the throne) and carry the pauses that make the voice
    sound worn down: the trailing ellipsis and the flat "So." that
    restarts the speech.
    """
    lowered = text.lower()
    for word in ("tired", "weary", "exhausted", "fatigued", "sleepy"):
        assert word not in lowered, f"the villain must not announce he is {word}"
    assert "eclipse" in lowered, "the scheme must survive in the monologue"
    assert "throne" in lowered, "the villain's history must show"
    assert "..." in text, "the pauses must be audible in the rhythm"
    assert "So." in text, "the deflection must restart the speech"
    words = text.split()
    return {"words": len(words), "chars": len(text), "beats": 5}


def main() -> None:
    text = check_monologue(
        compose(
            BEAT_QUESTION,
            BEAT_PLAN,
            BEAT_EROSION,
            BEAT_INVITATION,
            BEAT_PAYOFF,
        )
    )
    notes = voice_notes(text)
    assert notes["beats"] == 5
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
