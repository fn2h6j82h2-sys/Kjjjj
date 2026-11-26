"""Sprawdza tłumaczenie: komplet akapitów i czy każdy zmieści się w swoim oknie czasowym.
Użycie: python narzedzia/sprawdz.py <kod>      (np. python narzedzia/sprawdz.py pt-PT)
Czyta tlumaczenia/<kod>.tsv (nr<TAB>tekst) i tlumaczenia/<kod>-tytuly.tsv (rozdzial<TAB>tytul).
Szacowany czas = znaki / tempo lektora w tym języku (jezyki.tsv). Cel: 82–97% okna (okno = czas do startu następnego akapitu EN).
"""
import csv, sys

kod = sys.argv[1]
tempo = {r["kod"]: float(r["zn_na_s"]) for r in csv.DictReader(open("jezyki.tsv", encoding="utf-8"), delimiter="\t")}
if kod not in tempo: sys.exit(f"Nieznany kod {kod}. Kody: {', '.join(tempo)}")
zn_s = tempo[kod]
en = list(csv.DictReader(open("en/akapity.tsv", encoding="utf-8"), delimiter="\t"))
tl = {}
for w in open(f"tlumaczenia/{kod}.tsv", encoding="utf-8"):
    if "\t" not in w: continue
    nr, t = w.rstrip("\n").split("\t", 1)
    if nr.strip() == "nr": continue
    tl[nr.strip()] = t.strip()

brak, za_dlugie, za_krotkie, ok = [], [], [], 0
for a in en:
    nr = a["nr"]
    if nr not in tl or not tl[nr]: brak.append(nr); continue
    okno = float(a["okno_s"]); czas = len(tl[nr]) / zn_s; proc = czas / okno
    cel_min, cel_max = int(okno * 0.82 * zn_s), int(okno * 0.97 * zn_s)
    if proc > 0.97: za_dlugie.append((nr, len(tl[nr]), cel_min, cel_max, proc))
    elif proc < 0.82 and len(a["tekst_en"]) > 60: za_krotkie.append((nr, len(tl[nr]), cel_min, cel_max, proc))
    else: ok += 1
nadmiar = sorted(set(tl) - {a["nr"] for a in en})

print(f"{kod}: tempo {zn_s} zn/s, akapitów EN {len(en)}, OK {ok}")
if brak: print(f"BRAK ({len(brak)}):", ", ".join(brak))
if nadmiar: print("NIEZNANE NUMERY:", ", ".join(nadmiar))
for nazwa, lista in (("ZA DŁUGIE (skrócić naturalnie)", za_dlugie), ("ZA KRÓTKIE (wydłużyć naturalnie, bez lania wody)", za_krotkie)):
    if lista:
        print(f"{nazwa} ({len(lista)}):")
        for nr, z, a, b, p in lista: print(f"  akapit {nr}: {z} znaków, cel {a}–{b} ({p:.0%} okna)")
print("GOTOWE ✔" if not (brak or za_dlugie or za_krotkie or nadmiar) else "do poprawy ↑")
