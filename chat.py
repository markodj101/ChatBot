import random
import json
import torch
from model import NeuralNEt  # Import klase NeuralNet iz model.py
# Import funkcija bag_of_words i tokenize iz nltk_util.py
from nltk_util import bag_of_words, tokenize

# Provjera dostupnosti CUDA uređaja za ubrzanje rada s Tensorima
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')

# Učitavanje intents iz JSON datoteke
with open('intents.json', 'r') as f:
    intents = json.load(f)

# Putanja do datoteke s podacima za model
FILE = "data.pth"
data = torch.load(FILE)

# Dobivanje dimenzija ulaza, skrivenog sloja i izlaza iz podataka
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

# Inicijalizacija i postavljanje modela na odabrani uređaj
model = NeuralNEt(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)  # Postavljanje stanja modela
model.eval()  # Postavljanje modela u evaluacijski način rada

bot_name = "Dummie"  # Naziv čet bota


def get_response(msg):
    # Tokenizacija ulazne poruke
    sentence = tokenize(msg)
    # Pretvaranje tokenizirane poruke u vektor riječi
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    # Izračunavanje izlaza modela za ulaznu poruku
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # Dobivanje vjerovatnoće izlaza
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # Ako je vjerovatnoća veća od 0.75, biramo slučajni odgovor iz odgovarajućih namjena
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    # Ako vjerovatnoća nije dovoljno visoka, vraćamo poruku o nedostatku razumijevanja
    return "I do not understand...."
