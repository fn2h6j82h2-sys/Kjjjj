# Translating the narration of "Lionel Messi: The Full Story"

This repository holds the English narration of a ~58-minute YouTube documentary about Lionel Messi (channel "Na Podium"). It is dubbed into ~35 languages with a cloned voice (ElevenLabs). The picture is already finished and timed to the English voice, so every translated paragraph must fit into the same time window as the English one. Children watch too.

## Files
- `en/akapity.tsv` — English paragraphs: `nr`, `sekcja` (0 = hook, 1–18 chapters, 19 ending, 20 next-film teaser), `okno_s` (seconds available for this paragraph), `dl_en_s` (how long the English voice takes), `tekst_en`.
- `jezyki.tsv` — language codes, names/variant notes, and the measured speaking rate of the cloned voice (`zn_na_s`, characters per second).
- `narzedzia/sprawdz.py` — checks completeness and length: `python narzedzia/sprawdz.py <code>`.
- Output: `tlumaczenia/<code>.tsv` (`nr<TAB>text`, one line per paragraph, header line `nr<TAB>tekst`) plus `tlumaczenia/<code>-raport.md`.

## Working without a repository (chat with an attached PACZKA file)
If the files below don't exist yet, first unpack them from the attached PACZKA file into your working directory (each `### PLIK: <path>` block → that file), then continue. Keep everything in your sandbox; the user only needs the final downloadable file. If a long translation doesn't fit in one reply, continue on your own chapter by chapter (save progress to the file after each chapter) — the user may just write „dalej”.

## When asked to translate into a language, do ALL of these steps
1. **Translate section by section** (hook, then chapters 1, 2, …), writing straight into `tlumaczenia/<code>.tsv`. Every paragraph number from `en/akapity.tsv`, same order, nothing merged or split.
2. **Style:** natural spoken narration, as a professional native documentary narrator would say it — not a literal translation. Same facts, same order of information, same emotional tone (calm, warm). Short, clear sentences; simple words (children watch). Keep the storytelling hooks and the questions.
3. **Rules:**
   - Names stay as they are (Lionel, Leo, Messi, Celia, Jorge, Montiel, Newell's Old Boys, Grandoli, Rosario, La Masia, Camp Nou…); use the usual local spelling only where one is standard (e.g. Barcelona, Argentina, World Cup = the normal local name of the tournament).
   - Quotes in Spanish stay in Spanish (e.g. "Me vacié"), followed by the translation exactly as the English text does.
   - Numbers: years as digits (2022); other numbers and dates written the way a narrator says them, in words where natural ("the twenty-fourth of June" → local words).
   - No stage directions, brackets, emojis or markup. Plain text only.
   - Respect the variant notes in `jezyki.tsv` (e.g. `es` = neutral Spanish without "vosotros"; `pt-PT` = European Portuguese, not Brazilian).
4. **Length:** each paragraph must fit its window. Run `python narzedzia/sprawdz.py <code>` after every chapter and fix every flagged paragraph: shorten or lengthen *naturally* (rephrase, drop/add a small non-essential detail that is in the English meaning), never by cramming or by padding with empty words. Target is 82–97% of the window.
5. **Native read-through:** read the WHOLE translation from start to finish as a native narrator. Fix: unnatural phrasing, literal calques, repeated words in neighbouring sentences, inconsistent names/terms, wrong gender/agreement, anything a child would not understand. Then run `sprawdz.py` again until it says `GOTOWE ✔`.
6. **Report** in `tlumaczenia/<code>-raport.md`: 5–10 lines — anything uncertain (terms, cultural choices), paragraphs that were hard to fit.
7. **Hand the result to the user:** give `tlumaczenia/<code>.tsv` as a downloadable file (and say in Polish: „Gotowe — pobierz plik <code>.tsv i wyślij go Kamilowi”). If you work in a git repository, also commit it.

## Work through sub-agents (required when you have the Agent/Task tool, e.g. in Claude Code)
You are the **coordinator**. Do not translate yourself — this keeps your context small and every language gets a fresh, focused translator.
- **One translator agent per language.** Give it: the language code, the full text of this `CLAUDE.md`, and the task „do steps 1–5 for `<code>`, write `tlumaczenia/<code>.tsv`, return only a 3-line summary (OK count from `sprawdz.py`, anything uncertain)”. It must not paste the translation back to you.
- **Then one reviewer agent per language** (a new one, fresh eyes): it reads the WHOLE `tlumaczenia/<code>.tsv` next to `en/akapity.tsv` as a native documentary narrator and checks meaning (nothing missing, nothing added, facts and order the same), naturalness, consistency of names/terms, and what a child would understand. It fixes the file directly, runs `python narzedzia/sprawdz.py <code>` until `GOTOWE ✔`, and writes `tlumaczenia/<code>-raport.md` (step 6).
- **Then one meaning-check agent per language** (third fresh agent, never saw the English while reading): chapter by chapter it reads ONLY `tlumaczenia/<code>.tsv` and writes a plain back-translation into English (`tlumaczenia/<code>-wstecz.tsv`, `nr<TAB>english`). Then it compares it with `en/akapity.tsv` and lists every paragraph where the meaning, a fact, a number, who-did-what, or the tone differs — and anything that could sound rude, insulting, odd or scary to a native child (wrong word register, slurs, double meanings). It fixes those paragraphs in `<code>.tsv` naturally, re-runs `sprawdz.py` until `GOTOWE ✔`, and adds the list of fixes to `<code>-raport.md`.
- Run up to **3 languages in parallel** (3 translator agents at once; a language's reviewer starts when its translator is done).
- **You verify yourself:** run `python narzedzia/sprawdz.py <code>`. Hand the file to the user (step 7) only after `GOTOWE ✔` and after the meaning check is done. If it fails, send the flagged paragraph numbers back to the reviewer (or a new agent) to fix — never accept it as is.
- If you don't have an Agent/Task tool (plain chat), do all steps yourself.

**All languages mode:** if asked to translate „wszystkie” (all), go through `jezyki.tsv` in `kolejnosc` order (1–20, not „rezerwa”), skipping languages whose `tlumaczenia/<code>.tsv` already passes `sprawdz.py`. Keep at most 3 languages in progress at once (sub-agents above); hand over each file as soon as it passes, then start the next language from the queue. If you get interrupted, the user writes „dalej” and you continue with the first unfinished language.

Do one language per request unless asked for „wszystkie”. Never change files in `en/`, `jezyki.tsv` or `narzedzia/`.
