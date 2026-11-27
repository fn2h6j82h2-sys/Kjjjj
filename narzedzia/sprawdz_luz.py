"""Luźne sprawdzanie długości (Kamil 26.11: naturalność ważniejsza niż sztywny cel na akapit).
Symuluje ułożenie lektora: akapit startuje przy starcie akapitu EN albo, jeśli poprzedni jeszcze trwa, zaraz po nim (+0,25 s).
Akapit może więc „pożyczyć” czas od sąsiadów. Błąd tylko gdy:
  - start spóźnia się względem EN o więcej niż MAX_OPOZN s (obraz by się rozjechał), albo
  - ostatni akapit rozdziału wychodzi poza koniec rozdziału (karta / pauza).
Długość liczona z zapasem ZAPAS (mikser lekko przyspiesza za długie akapity). Za krótkie akapity nie są błędem (cisza jest OK) — tylko ostrzeżenie, gdy < 55% czasu EN (może czegoś brakuje).
Użycie: python narzedzia/sprawdz_luz.py <kod> [plik.tsv]"""
import csv, sys
MAX_OPOZN = 2.0
ZAPAS = 1.10  # Kamil 27.11: mikser może przyspieszyć akapit do 15%, więc sprawdzamy jak przy +10%
kod = sys.argv[1]; plik = sys.argv[2] if len(sys.argv) > 2 else f"tlumaczenia/{kod}.tsv"
zn = {r["kod"]: float(r["zn_na_s"]) for r in csv.DictReader(open("jezyki.tsv", encoding="utf-8"), delimiter="\t")}[kod]
en = list(csv.DictReader(open("en/akapity.tsv", encoding="utf-8"), delimiter="\t"))
tl = {}
for w in open(plik, encoding="utf-8-sig"):
    if "\t" in w:
        n, t = w.rstrip("\n").split("\t", 1)
        if n.strip() != "nr": tl[n.strip()] = t.strip()
brak, zle, krotkie = [], [], []
sek = None
for i, a in enumerate(en):
    s = a["sekcja"]
    if s != sek: sek, t_en, koniec_pop = s, 0.0, -1.0
    x = tl.get(a["nr"], "")
    if not x: brak.append(a["nr"])
    dl = len(x) / zn / ZAPAS
    start = max(t_en, koniec_pop + 0.25)
    koniec = start + dl
    opozn = start - t_en
    ostatni = i + 1 == len(en) or en[i + 1]["sekcja"] != s
    granica = t_en + float(a["okno_s"]) + 0.5
    if opozn > MAX_OPOZN: zle.append(f"  akapit {a['nr']}: start spóźniony o {opozn:.1f} s (poprzednie za długie) — skrócić ten lub 1–2 poprzednie")
    elif ostatni and koniec > granica: zle.append(f"  akapit {a['nr']} (koniec rozdziału): wychodzi {koniec - granica:.1f} s poza rozdział — skrócić o ok. {int((koniec - granica) * zn) + 1} znaków tu lub wcześniej")
    if x and len(a["tekst_en"]) > 60 and dl < 0.55 * float(a["dl_en_s"]): krotkie.append(a["nr"])
    koniec_pop = koniec
    t_en += float(a["okno_s"]) + 0.25
print(f"{kod}: {len(en)} akapitów EN, tempo {zn} zn/s, dopuszczalne opóźnienie {MAX_OPOZN} s")
if brak: print(f"BRAK ({len(brak)}):", ", ".join(brak))
if zle: print(f"DO POPRAWY ({len(zle)}):"); print("\n".join(zle))
if krotkie: print("Uwaga, bardzo krótkie (sprawdzić, czy nic nie zginęło):", ", ".join(krotkie))
print("GOTOWE ✔" if not (brak or zle) else "do poprawy ↑")
