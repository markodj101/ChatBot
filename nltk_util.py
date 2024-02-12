import nltk  # Uvoz biblioteke za obradu prirodnog jezika
import numpy as np  # Uvoz biblioteke za numeričke operacije
# nltk.download('punkt')  # Preuzimanje potrebnih podataka za tokenizaciju (može biti potrebno samo prilikom prvog pokretanja)

# Uvoz klase PorterStemmer za stemming
from nltk.stem.porter import PorterStemmer


def tokenize(sentence):
    """
    Funkcija koja razbija rečenicu na tokene.
    """
    return nltk.word_tokenize(sentence)


stemmer = PorterStemmer()  # Inicijalizacija objekta za stemming


def stem(word):
    """
    Funkcija za izvođenje stemizacije riječi.
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    """
    Funkcija koja generira vreću riječi za zadatu tokeniziranu rečenicu i listu svih riječi.
    """
    tokenized_sentence = [
        stem(w) for w in tokenized_sentence]  # Stemizacija tokenizirane rečenice
    # Inicijalizacija vreće riječi
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            # Postavljanje odgovarajućeg indeksa na 1.0 ako se riječ nalazi u tokeniziranoj rečenici
            bag[idx] = 1.0
    return bag
