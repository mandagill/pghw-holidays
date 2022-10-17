from artist import send_to_airtable
from pprint import pprint
import random

import sys
sys.path.append("./../artist")

RANDOM_ARTISTS = ['', 'Artimesia Gentileschi', 'Judith Leyster', 'Edmonia Lewis', 'Frida Kahlo', 'Eva Hesse', '']

def random_id():
  return random.randrange(10000, 99999)


def random_artist():
  return RANDOM_ARTISTS[random.randint(1, 5)]


response = send_to_airtable('Artists',
  {
    'Vendor ID number': random_id(),
    'Name': f"{random_artist()}"
  })

pprint(response)