# Translating the narration of "Lionel Messi: The Full Story"

This repository holds the English narration of a ~58-minute YouTube documentary about Lionel Messi (channel "Na Podium"). It is dubbed into ~35 languages with a cloned voice (ElevenLabs). Children watch too.

**What matters most: the narration must sound as if it was written in the target language from the start** — natural, spoken, idiomatic, like a professional native documentary narrator. Do NOT worry about exact length: the mixer places every paragraph at the English start and can speed a paragraph up a little. Only a final, relaxed length check is done (step 4).

## Files
- `en/akapity.tsv` — English paragraphs: `nr`, `sekcja` (0 = hook, 1–18 chapters, 19 ending, 20 next-film teaser), `okno_s`, `dl_en_s`, `tekst_en`.
- `jezyki.tsv` — language codes, variant notes, speaking rate of the voice (`zn_na_s`).
- `narzedzia/sprawdz_luz.py` — final relaxed check: `python narzedzia/sprawdz_luz.py <code>`.
- Output: `tlumaczenia/<code>.tsv` (`nr<TAB>text`, one line per paragraph, header line `nr<TAB>tekst`).

## Working without a repository (chat with an attached PACZKA file)
If the files don't exist yet, first unpack them from the attached PACZKA file (each `### PLIK: <path>` block → that file). Keep everything in your sandbox; the user only needs the final downloadable file. If you get interrupted, the user writes „dalej” and you continue.

## Steps for one language
1. **Write, don't translate.** Use the English text as the source of facts and story. For each paragraph write what a native narrator would naturally say: free sentence structure, local idioms, natural word order, no calques. Same facts, names, numbers, quotes and the same order of information; same calm, warm tone; simple words (children watch). Every paragraph number from `en/akapity.tsv`, same order, nothing merged or split.
2. **Rules** (and ALL of `ZASADY.md` — read it before writing):
   - Names stay as they are (Lionel, Leo, Messi, Celia, Jorge, Montiel, Newell's Old Boys, Grandoli, Rosario, La Masia, Camp Nou…); use the usual local name only where one is standard (Barcelona, Argentina, the World Cup).
   - Spanish quotes stay in Spanish (e.g. "Me vacié"), followed by a natural translation, as in the English text.
   - Numbers: years as digits (2022); other numbers and dates written as a narrator says them.
   - Plain text only: no brackets, stage directions, emojis or markup.
   - Respect the variant notes in `jezyki.tsv` (e.g. `pt-BR` = Brazilian Portuguese).
   - Watch for: clear subject in every sentence (who does what), correct gender/case/agreement, no repeated words in neighbouring sentences, a gap in numbering (e.g. no 7) is intentional.
3. **Native review** of the WHOLE file using the checklist in `ZASADY.md`, start to finish, as a native editor: fix anything stiff, translated-sounding, ambiguous or wrong; make names and terms consistent; check facts against the English.
4. **Final relaxed length check — once, at the end:** `python narzedzia/sprawdz_luz.py <code>`. It only flags places where the voice would fall clearly behind the picture. Fix only the flagged paragraphs (or the 1–2 before them) by tightening wording naturally — drop filler words, never facts. Run it again until `GOTOWE ✔`. Do not touch paragraphs that are not flagged.
5. **Hand the result to the user:** give `tlumaczenia/<code>.tsv` as a downloadable file and say in Polish: „Gotowe — pobierz plik <code>.tsv i wyślij go Kamilowi”.

## Work through sub-agents (when you have the Agent/Task tool, e.g. in Claude Code)
You are the **coordinator**; keep your own context small and never paste whole translations into it.
- **Three writer agents per language, in parallel:** sections 0–9, 10–14, 15–20. Give each: the language code, its sections, the full text of this `CLAUDE.md` and `ZASADY.md`, and the task „do steps 1–2 for `<code>`, only your sections, write `tlumaczenia/<code>-1.tsv` / `-2.tsv` / `-3.tsv`, return a 2-line summary”. No length checks for them.
- **Merge** the parts (a few lines of Python, `en/akapity.tsv` order, header `nr<TAB>tekst`) into `tlumaczenia/<code>.tsv`.
- **One reviewer agent** (fresh eyes): steps 3 and 4 on the whole file, fixing it directly; returns a 3-line summary.
- Keep **2 languages in progress** at a time. Verify `sprawdz_luz.py` says `GOTOWE ✔` yourself, then step 5.
- No Agent/Task tool (plain chat): do all steps yourself.

**All languages mode:** if asked for „wszystkie” (all), go through `jezyki.tsv` in `kolejnosc` order, skipping languages whose `tlumaczenia/<code>.tsv` already exists and passes `sprawdz_luz.py`. Hand over each file as soon as it is done.

Never change files in `en/`, `jezyki.tsv` or `narzedzia/`.
