import requests
import os
import random
import codecs

name_of_directory = 'TEST-amg-automated'
RANDOM_ARTISTS = ['ArtimesiaGentileschi', 'JudithLeyster', 'EdmoniaLewis', 'FridaKahlo', 'EvaHesse']

def random_artist():
  index = random.randrange(0, 4)
  return RANDOM_ARTISTS[index]

os.mkdir(f"{name_of_directory}")
artist = random_artist()

r = requests.get(f"https://barcodeapi.org/api/qr/{artist}")

qr_stringified = r.text

with open(f"{artist}.png", 'bw') as f:
  # TODO fix this, it returns "It may be damaged or use a file format that Preview doesn’t recognize" when I go to open it
  f.write(codecs.encode(qr_stringified, encoding='zlib'))
