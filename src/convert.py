#!/usr/bin/env python3
"""
convert_cards.py

Usage:
    python convert_cards.py pleco  < cards_source_v1.txt > pleco.txt
    python convert_cards.py anki   < cards_source_v1.txt > anki.tsv

The source file format:
category | hanzi | pinyin | function | note
"""

import sys

if len(sys.argv) != 2 or sys.argv[1] not in ("pleco", "anki"):
    sys.stderr.write("Usage: convert_cards.py [pleco|anki]\n")
    sys.exit(1)

mode = sys.argv[1]
current_category = ""

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("#"):
        continue

    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 5:
        continue

    category, hanzi, pinyin, function, note = parts

    if mode == "pleco":
        # Pleco format:
        # Hanzi<TAB>definition //category
        if (category != current_category):
            print(f"//{category}")
            current_category = category
        definition = f"{function}; {note}"
        print(f"{hanzi}\t{pinyin}\t{definition}")

    elif mode == "anki":
        # Anki TSV format:
        # Hanzi<TAB>Pinyin<TAB>Meaning<TAB>Category
        meaning = f"{function}; {note}"
        print(f"{hanzi}\t{pinyin}\t{meaning}\t{category}")
