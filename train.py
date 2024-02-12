import json  # Uvoz biblioteke za rad s JSON datotekama
# Uvoz funkcija za obradu teksta
from nltk_util import tokenize, stem, bag_of_words
import numpy as np  # Uvoz biblioteke za numeričke operacije
from model import NeuralNEt  # Uvoz definiranog modela neuronske mreže
import torch  # Uvoz PyTorch biblioteke
import torch.nn as nn  # Uvoz modula za definiciju neuronskih mreža u PyTorch-u
# Uvoz klasa za rad s podacima u PyTorch-u
from torch.utils.data import Dataset, DataLoader


with open('intents.json', 'r') as f:
    intents = json.load(f)  # Učitavanje podataka iz JSON datoteke

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ["?", "!", ",", "."]
# Stemizacija riječi
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))  # Uklanjanje duplikata i sortiranje riječi
tags = sorted(set(tags))  # Sortiranje oznaka


x_train = []
y_train = []

for (pattern_sentece, tag) in xy:
    bag = bag_of_words(pattern_sentece, all_words)
    x_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)  # Priprema oznaka za CrossEntropyLoss


x_train = np.array(x_train)
y_train = np.array(y_train)


class ChatDataset(Dataset):
    """
    Definicija klase za dataset koji će se koristiti za obuku modela.
    """

    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples


batch_size = 8

hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000


dataset = ChatDataset()
train_loader = DataLoader(
    dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)  # Učitavanje podataka u DataLoader
# Određivanje uređaja za izvođenje (GPU ili CPU)
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
model = NeuralNEt(input_size, hidden_size, output_size).to(
    device)  # Inicijalizacija modela


criterion = nn.CrossEntropyLoss()  # Definicija gubitka
optimizer = torch.optim.Adam(
    model.parameters(), lr=learning_rate)  # Definicija optimizatora


for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)
        labels = labels.long()
        # forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        # backward and optimizer step

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}')

print(f'final loss, loss={loss.item():.4f}')

data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)  # Spremanje modela i pripadajućih podataka

print(f'training complete. file saved to {FILE}')
