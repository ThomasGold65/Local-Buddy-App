# LocalBuddy

**Overal een bekende!** Bewoners met een bezoekersvergunning delen hun ongebruikte bezoekersuren met parkeerders.

Deze repository bevat de klikbare demo van de app.

## Hoe het werkt

1. **Eenmalige klik:** de parkeerder vindt een bewoner op de kaart en tikt op *Word Buddy*. De bewoner accepteert één keer.
2. **Automatisch parkeren:** daarna start de parkeerder een sessie met één tik. Er gaat geen verzoek per keer naar de bewoner. LocalBuddy kiest de Buddy, controleert de limieten en meldt de sessie aan in het bezoekersparkeerportaal van de gemeente.
3. **De bewoner houdt controle:** met een daglimiet per Buddy, pauzeren of verwijderen, een melding bij elke sessie en het totaal aantal gedeelde uren.

Tarieven in de demo: de parkeerder betaalt € 3,00 per uur (regulier € 4,00) en de bewoner ontvangt € 2,00 per uur.

## Demo openen

Open `index.html` in een browser. De demo werkt offline en heeft geen server nodig.

- Links staat de parkeerder (Daan), rechts de bewoner (Sophie). Het middenpaneel toont de demo-route en de calls naar het parkeerportaal.
- Met **1 sec = 1 min** loopt een sessie snel af.
- Met **Demo resetten** begin je opnieuw.

## Bestanden

| Bestand | Wat |
| --- | --- |
| `app.src.html` | Broncode van de demo (HTML, CSS en JS) |
| `avatars/` | Avatars, uitgesneden uit het LocalBuddy-deck |
| `build.py` | Zet de avatars inline en maakt `index.html` en `artifact.html` |
| `index.html` | Gebouwde demo die zelfstandig werkt |

Opnieuw bouwen na een wijziging:

```bash
python3 build.py
```

## Status

Dit is een demo. De koppeling met het parkeerportaal van de gemeente is gesimuleerd. Er zijn nog geen echte accounts of betalingen.
