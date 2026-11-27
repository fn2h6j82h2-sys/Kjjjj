# Writing rules (Kamil, 27.11): natural narration for an AI voice

These rules came from the mistakes reviewers found in earlier languages. Writers and the reviewer follow them. They take priority over sounding close to the English.

## 1. Emotion and intent, never word for word
- Literal idioms sound physical, comic or funereal in the most moving scenes:
  - "I emptied myself" = "I gave everything" (not "I emptied myself").
  - "I leave at peace" = "I leave with a calm heart" (not a funeral phrase like "rest in peace").
  - "found his voice" = he finally spoke up / his voice was heard.
  - "never became loud" = he never sought attention.
- Hidden everyday calques:
  - player = footballer (not "gamer/player");
  - little sister = younger sister;
  - note = farewell letter/message (not a memo);
  - "sign someone" = sign a contract with him;
  - "completed the family" = a younger sister was born;
  - "European nights" = Champions League nights;
  - "soccer dad" = just a dad of young footballers.
- Break up English telegraphic fragments without verbs ("Boots off. Phone out."). In other languages they sound like slogans or nonsense, so write short, full sentences with a verb instead.
- Use a film register, not newspaper, official or school-essay style (no needless "the said", "in the year" before every date, and so on).

## 2. Subject and repetitions
- The hero's plain name or a pronoun is invisible to the ear. Do NOT use press epithets ("the Argentine", "the winger", "the young striker", "the coach", "the captain", "the groom"). Use "captain" only where the passage really is about being captain.
- Mention the name or pronoun as often as THIS language naturally needs:
  - Languages with person endings on verbs (e.g. Czech, Serbian, Romanian, Italian, Greek, Hungarian, Turkish) rely on the implied subject. Name someone only when the person changes or a new scene starts.
  - Languages without person endings (e.g. Chinese, Thai, Indonesian) need the pronoun back often enough that the listener always knows who acts.
- Make a SEPARATE pass for close repetitions of the same word in neighbouring sentences. Fixing pronouns often creates them.

## 3. Variant and register
- Use one variant, the one in `jezyki.tsv`. No hybrids of regional variants.
- Address the viewer the same way through the whole film (informal "you" or polite/plural), from the call to action in the middle to the ending.

## 4. Text for the AI voice
- Numbers and dates: follow the numbers rule in `CLAUDE.md`. In languages with cases, make sure number endings are correct; when unsure, write the number as words.
- Use one quote format in the whole file. Don't mix paragraphs with and without quotation marks.
- No dashes glued to words (word—word). Use a comma, a colon, or a dash with spaces.

## 5. Final checklist (reviewer)
1. Facts and meaning: names, roles, dates, results; it is clear who does what in every sentence.
2. Calques and register: no sentence sounds translated, like a press article, or like an official document.
3. Repetitions and rhythm: no close repetitions, no epithets, the same address to the viewer throughout.
4. Voice hygiene: quotes, dashes and numbers as above. Then the relaxed length check from `CLAUDE.md` step 4, and only that.
