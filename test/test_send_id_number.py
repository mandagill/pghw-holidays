from pprint import pprint
from artist import lambda_function
import random

import sys
sys.path.append("./../artist")

RANDOM_ARTISTS = ['', 'Artimesia Gentileschi', 'Judith Leyster', 'Edmonia Lewis', 'Frida Kahlo', 'Eva Hesse', '']

def random_id():
  return random.randrange(10000, 99999)


def random_artist():
  return RANDOM_ARTISTS[random.randint(1, 5)]


response = lambda_function.lambda_handler('Artists',
  {
    'Vendor ID number': random_id(),
    'Name': f"{random_artist()}"
  })

pprint(response)