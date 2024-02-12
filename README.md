# Chatbot aplikacija

Ova aplikacija implementira jednostavan chatbot koji može odgovarati na određene pitanja korisnika. Chatbot je izgrađen pomoću neuronske mreže te se koristi za obradu prirodnog jezika.

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

2. Instalirajte potrebne Python pakete koristeći `pip`: torch,numpy i nltk.

3. Idite na code i izaberite opciju download zip i raspakujte fajl, nakon toga pratite korka 2.:

## Korištenje

1. Pokrenite `main.py` datoteku kako biste pokrenuli aplikaciju:

```bash
python main.py
```

2. Nakon pokretanja aplikacije, možete započeti razgovor s chatbotom. Unesite poruku u polje za unos teksta i pritisnite tipku "Send" ili pritisnite Enter kako biste poslali poruku.

## Struktura projekta

- `main.py`: Glavna datoteka koja pokreće chatbot aplikaciju.
- `chat.py`: Datoteka koja sadrži logiku chatbota, uključujući funkcije za obradu poruka.
- `model.py`: Definicija modela neuronske mreže koja se koristi za klasifikaciju poruka.
- `nltk_util.py`: Pomoćne funkcije za obradu teksta koristeći NLTK (Natural Language Toolkit).
- `intents.json`: Datoteka koja sadrži definicije intents (namjene) koje chatbot može prepoznati.
- `data.pth`: Datoteka u kojoj se sprema obučeni model i pripadajući podaci.
- `requirements.txt`: Datoteka koja sadrži popis Python paketa potrebnih za pokretanje aplikacije.

## Dodatne informacije

- Aplikacija koristi Python programski jezik i PyTorch biblioteku za rad s neuronskim mrežama.
- Potrebno je imati instaliran Python (preporučena verzija 3.6 ili novija) kako bi aplikacija radila.
- Za detaljnije informacije o korištenju aplikacije i prilagodbama, pogledajte komentare unutar izvornog koda.

---

Ovo je samo primjer kako bi README datoteka mogla izgledati. Prilagodite je vašim potrebama i dodajte dodatne informacije prema zahtjevima vašeg projekta.
