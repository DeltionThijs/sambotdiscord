# Sambotdiscord

Sambotdiscord is een Discord-bot geschreven in Python met behulp van de discord.py-bibliotheek. Deze bot kan reageren op bepaalde berichten en periodiek berichten sturen naar het hoofdkanaal van de servers waar de bot zich in bevindt.

## Installatie

1. Zorg ervoor dat Python 3 is geïnstalleerd op uw systeem.
2. Clone of download de repository naar uw lokale machine.
3. Navigeer naar de map waarin u de repository heeft gekloond of gedownload.
4. Maak een virtuele omgeving met behulp van `python3 -m venv venv`.
5. Activeer de virtuele omgeving met behulp van `source venv/bin/activate` (Linux/Mac) of `venv\Scripts\activate` (Windows).
6. Installeer de vereiste afhankelijkheden met behulp van `pip install -r requirements.txt`.
7. Maak een `.env`-bestand in dezelfde map als het script en voeg de volgende regel toe: `DISCORD_TOKEN=je-bot-token-hier`. Vervang `'je-bot-token-hier'` door je eigen Discord-bot-token.
8. Voer het script uit met behulp van `python sam2.py`.

## Gebruik

- De bot reageert automatisch op bepaalde berichten die bepaalde trefwoorden bevatten. Bijvoorbeeld, als het woord "lenen" in een bericht voorkomt, zal de bot een reactie sturen met de tekst "Hey, ik ben kkr broke. Mag ik geld?".
- Je kunt ook de `!hello`-opdracht gebruiken om een bericht te sturen met de tekst "Hallo, ik ben een sam de kanker mongool".

## Aanpassing

Je kunt de functionaliteit van de bot aanpassen door de code in het `sam2.py`-bestand te bewerken. Je kunt bijvoorbeeld de trefwoorden en reacties aanpassen in de `on_message`-functie of nieuwe opdrachten toevoegen in de `@bot.command`-decorateur.

## Bijdragen

Bijdragen aan dit project zijn welkom. Als je een probleem vindt of een verbetering voorstelt, kun je een probleem openen of een pull-verzoek indienen.

## Licentie

Dit project is gelicentieerd onder de MIT-licentie. Zie het `LICENSE`-bestand voor meer informatie.

**Let op:** Zorg ervoor dat je de daadwerkelijke bot-token vervangt in het `.env`-bestand voordat je het script uitvoert.
