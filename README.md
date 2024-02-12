# Chatbot aplikacija

ChatBot je aplikacija za razmjenu poruka koja koristi vještačku inteligenciju kako bi odgovarala na data pitanja i pružala korisne informacije ili podršku. Korisnici mogu postavljati pitanja ili započeti razgovor s ChatBotom putem polja za unos teksta. Aplikacija podržava različite teme i može se prilagoditi specifičnim potrebama korisnika zamjenom `intents.json` fajla. ChatBot je intuitivan i jednostavan za korištenje, pružajući korisnicima brz i učinkovit način za dobivanje informacija ili rješavanje problema.

## Sadržaj

1. [Instalacija](#instalacija)
2. [Korištenje](#korištenje)
3. [Struktura projekta](#struktura-projekta)
4. [Dodatne informacije](#dodatne-informacije)

## Instalacija

1. Klonirajte repozitorij na svoje računar (u slučaju da nemate git instaliran pratite korak 3.):

```bash
git clone https://github.com/username/chatbot.git
```

2. Instalirajte potrebne Python pakete koristeći `pip`: **torch,numpy i nltk.**

3. Idite na code i izaberite opciju download zip i raspakujte fajl, nakon toga pratite korka 2.:

## Korištenje

1. Pokrenite `app.py` datoteku kako biste pokrenuli aplikaciju:
2. Nakon pokretanja aplikacije, možete započeti razgovor s chatbotom. Unesite poruku u polje za unos teksta i pritisnite Enter.
3. Ako želite trenirati ChatBot-a sa novim podacima, ubacite ih u `intents.json` fajl i pokrenite `train.py` pa zatim `app.py`.
## Struktura projekta

- `main.py`: Glavna datoteka koja pokreće chatbot aplikaciju.
- `chat.py`: Datoteka koja sadrži logiku chatbota, uključujući funkcije za obradu poruka.
- `model.py`: Definicija modela neuronske mreže koja se koristi za klasifikaciju poruka.
- `nltk_util.py`: Pomoćne funkcije za obradu teksta koristeći NLTK (Natural Language Toolkit).
- `intents.json`: Datoteka koja sadrži definicije intents (namjene) koje chatbot može prepoznati.
- `data.pth`: Datoteka u kojoj se sprema obučeni model i pripadajući podaci.

## Dodatne informacije

- Aplikacija koristi Python programski jezik i PyTorch biblioteku za rad s neuronskim mrežama.
- Potrebno je imati instaliran Python (preporučena verzija 3.6 ili novija) kako bi aplikacija radila.
- Imaju dva json fajla od koji je jedan 'coffee.json' ako ova istreniramo dobićemo Chatbot-a koji pordaje kafu.

---

