# ar — raport recenzenta (MSA, styl panarabskiego dokumentu TV)

- Ujednolicone terminy: Ballon d'Or = الكرة الذهبية; Golden Ball turnieju = جائزة أفضل لاعب في البطولة (106, 177/178, 263); Golden Boot = الحذاء الذهبي; Champions League = دوري الأبطال (w 140 tylko „النهائي”, bo kontekst z 139 jasny, a okno ciasne); notatka z 2026 = رسالة; Me vacié = «أي: أفرغت نفسي» (5 i 311); pecho frío = «pecho frío»، أي الصدر البارد; w 103 zmieniono „روساري القلب” na „قلبه في روساريو”.
- Refren „He did not say much. He just played.” wszędzie: لم يكن كثير الكلام. كان يلعب فقط. (6, 75, 115, 171, 333).
- Widz zawsze w liczbie mnogiej (96, 110, 332, 334 — „ربما فيكم الهادئ… فإن كنتم هادئين”). Cudzysłowy « ». Brak znaków diakrytycznych poza šaddą w وقّعوا/وقّعه (57, 62), żeby nie czytać „upadli”.
- Wybory kulturowe: „What are you looking at, fool?” = «إلى ماذا تنظر يا أحمق؟» (łagodne, nie obraźliwe dla dzieci); drony = طائرات الدرون (zamiast مسيرات, które kojarzą się z wojskiem); Gladiator = المصارع (arabski tytuł filmu).
- Przywrócone fakty: 164 (RPA), 167 („właśnie to”, „nawet hymnu”), 173 (poprawiony błąd „w Bośni” → „przeciw Bośni”), 175 (obrońca Mascherano), 181 (Luis), 190, 191 (Sergio), 203 (Mateo, rodzeństwo jako świadkowie), 204 („nawet nie”, Andy), 210 (Islandia), 211 (przed meczem), 230 (Messi podał do Di Maríi przy złotym medalu), 154 (strzał płaski z dystansu, obrońca, Carles), 242 („prawdopodobnie”), 251 (drybling, potem asysta), 263, 272 (wszedł z ławki, podkręcony wolny), 273, 310, 89, 90, 104, 112 (przeredagowane), 113, 55 (Cesc), 176 (Mario).
- Nadal brakuje (za ciasne okna): 44 „only”, 68/71 „mała siostra” (jest tylko „siostra”), 104 „senior team”, 139 i 142 imiona Andrés/Edwin, 205 „duże ekrany”/„prawie puste”, 219 „Monachium”, 223 „Diego”, 235 „hiszpańskiej” ligi, 242 „wszyscy wiedzieli”, 251 imię Julián, 277 Leandro, 288 Cristian, 310 data 21 lipca (zostało „dwa dni po finale”).
- Najtrudniejsze do zmieszczenia: 154, 164, 173, 204, 230, 242, 251, 272, 289.

## Kontrola sensu
Tłumaczenie wsteczne zrobione „na ślepo” (bez EN): `tlumaczenia/ar-wstecz.tsv`. Poprawki po porównaniu z EN:
- 4: niejasne, kto wbija igłę (mogło brzmieć, że lekarz) → dodano „بنفسه” (sam sobie); usunięto „صغيرة”, by zmieścić się w oknie.
- 23: „Leo wie, gdzie będzie grał” (zmiana sensu) → „وليو اختار ناديه” (Leo już wybrał swój klub = wiedział, gdzie chce grać).
- 180: „Messi strzelił” brzmiało jak gol w meczu (a było 0:0) → „سجل ميسي ركلته” (strzelił swój karny); usunięto „مجددا”, by zmieścić długość.
- 261: „ثم رفعها وقبلها” gramatycznie wskazywało na płaszcz (عباءة), nie puchar → „ثم رفع الكأس، وقبلها، ولم يفلتها”; „قبل رفع الكأس” → „قبل التتويج”.
- 263: „podniosły jego dorobek do siedmiu” bez kontekstu (mogło znaczyć karierę) → „صارت أهدافه سبعة” w zdaniu o turnieju (6. i 7. gol mundialu).
- 279: „ولاعب ابنه ماتيو الكرة” bez znaków diakrytycznych czytało się też jako „i piłkarz jego syna Mateo” → „وداعب ابنه ماتيو الكرة” (żonglował piłką).
- 314: odwrócony sens — „którego chłopiec z Rosario chciał i nie dostał” → „الذي أراده صبيا يوما ولم ينله” (klub, który kiedyś chciał go jako chłopca i go nie dostał).
Świadomie zostawione: 161 „a god” → „أسطورة” (unikamy religijnie drażliwego określenia); 258 „طلب من الله أن ينهيها” (wierne EN, naturalne w arabskim); 309 „صار في السماء اثنان” (łagodne, wierne EN); 250 „يا أحمق” (łagodne, jak „fool”); 310 bez daty 21 lipca (jest „dwa dni po finale”, okno za ciasne); 316 „حرب فوكلاند” (nazwa standardowa w arabskich mediach, jak w EN); 317 bez „dla Argentyny” (wynika z kontekstu meczu pożegnalnego). Po poprawkach: cel.py W CELU ✔ (318/318), sprawdz.py GOTOWE ✔.
