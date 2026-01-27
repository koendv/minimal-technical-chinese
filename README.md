# minimal technical chinese
Minimal flashcard deck for extracting precise meaning from datasheets and manuals. 144 carefully chosen flashcards.

## Quick Start

- Download the decks from "releases"
- Import in [Pleco](https://www.pleco.com/) or [Anki](https://apps.ankiweb.net/)
- Begin with the grammar, then vocab
- Try scanning a datasheet in 4 to 6 weeks.

## Background

Hi. I'm an electronics engineer who wishes to read Chinese datasheets (数据手册).
I find university-level Chinese learning is a lot of pressure, directed towards an end goal of reading classic Chinese literature ("Voyage to the West"). 
I understand my knowledge of Chinese will always be lacking.
I know I do not have the cultural background to read a newspaper article in Chinese.
I am aware any ethnic Chinese kid beats my pronounciation.
However, I wish to be able to read Chinese technical literature in my field.
At the very least, be able to scan datasheets and reference manuals, read a few sentences, maybe a paragraph in depth.

A datasheet is a document that is authoritative in what it states, but what it omits should not be inferred.
To me, this is sufficient to classify a datasheet as a literary genre of its own.
However, it is a literary genre which is not studied in language schools because the subject is out of scope for language teachers.
Hence the need for a study aid of my own.

## Deliverables

This git contains two decks of flashcards, one for grammar, one for vocabulary.

-  53 grammar operators
-  91 technical vocabulary
- 144 total

This implies that, for a study effort similar to HSK1, one can learn the backbone of a Chinese technical document.

## Example

Chinese: "FT，FTf，和FTa引脚当输入高于VDD + 0.3 V时，必须禁用内部上拉/下拉电阻。"

Parsed using this deck:

- 当...时 – condition in effect (Conditions & Scope)
- 高于 – exceeds upper limit (related to 不高于 – Limits & Thresholds)
- 必须 – mandatory requirement (Mandatory / Prohibited / Optional)
- 禁用 – disable functionality (State / Mode / Configuration)
- 内部 – internal (Descriptive Term)

Even without knowing every term, using these cards you extract:

- Trigger: Input voltage > VDD + 0.3V
- Mandatory Action: Disable something
- Target: Internal pull-up/pull-down resistors
- Severity: 必须 means violation risks damage

Source: AT32F405/AT32F402 Datasheet, Section 4.3.11 "GPIO Port Characteristics"

## Note

The card structure could be inverted to create a deck of English terms with meanings in Chinese for Chinese engineers who wish to read datasheets in English.

Contributions welcome.

*For those of us who build crystal palaces of silicon*
