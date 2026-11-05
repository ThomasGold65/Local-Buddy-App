# LocalBuddy

**Overal een bekende!** Bewoners met een bezoekersvergunning delen hun ongebruikte bezoekersuren met parkeerders.

Live demo (besloten, met login): https://localbuddy.goldmarketing.nl

## Hoe het werkt

1. **Eenmalige klik:** de parkeerder vindt een bewoner op de kaart en tikt op *Word Buddy*. De bewoner accepteert één keer.
2. **Automatisch parkeren:** daarna start de parkeerder een sessie met één tik. Er gaat geen verzoek per keer naar de bewoner. LocalBuddy kiest de Buddy, controleert de limieten en meldt de sessie aan in het bezoekersparkeerportaal van de gemeente.
3. **De bewoner houdt controle:** met een daglimiet per Buddy, pauzeren of verwijderen, een melding bij elke sessie, het totaal aantal gedeelde uren en een aan/uit-schakelaar per bekend kenteken.

De kaart toont alle vergunningzones van Amsterdam en Rotterdam, uit RDW Open Data Parkeren (gebiedsbeheerder 363 en 599).

## Besloten demo

`index.html` is een inlogpagina. De demo zit daar AES-versleuteld in en wordt pas in de browser ontsleuteld met de juiste gebruikersnaam en het juiste wachtwoord. De broncode en de echte gegevens staan dus niet leesbaar in deze repository.

## Bestanden

| Bestand | Wat |
| --- | --- |
| `index.html` | Inlogpagina met de versleutelde demo (GitHub Pages) |
| `login.html` | Sjabloon van de inlogpagina |
| `build.py` | Bouwt de demo en versleutelt hem in `index.html` |
| `vendor/` | Leaflet (kaart) en de zonegrenzen (`zones.json`) |
| `avatars/` | Avatars, uitgesneden uit het LocalBuddy-deck |

Lokaal en niet in git: `app.src.html` (broncode), `login.local` (gebruikersnaam en wachtwoord) en `local/LocalBuddy-offline.html` (demo zonder login).

Opnieuw bouwen na een wijziging:

```bash
python3 build.py
```

## Status

Dit is een demo. De koppeling met het parkeerportaal van de gemeente is gesimuleerd. Er zijn nog geen echte accounts of betalingen.
