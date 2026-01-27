CONVERT = src/convert.py

all: decks.zip

decks: \
	decks/anki/zh-cn_en_grammar.txt \
	decks/anki/zh-cn_en_electronics.txt \
	decks/pleco/zh-cn_en_grammar.txt \
	decks/pleco/zh-cn_en_electronics.txt \

decks/anki/%.txt: src/%.txt $(CONVERT)
	@mkdir -p decks/anki
	$(CONVERT) anki < $< > $@

decks/pleco/%.txt: src/%.txt $(CONVERT)
	@mkdir -p decks/pleco
	$(CONVERT) pleco < $< > $@

decks.zip: decks
	zip -r9 decks.zip decks/ README.md LICENSE.md

clean:
	rm -f decks/anki/*.txt decks/pleco/*.txt decks.zip

.PHONY: all clean
