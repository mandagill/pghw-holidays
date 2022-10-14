from send_inventory import send_to_airtable
from pprint import pprint
from random import randint

RANDOM_COLORS = ['', 'red', 'blue', 'green', 'purple', 'yellow', '']

TEST_BODY = "{'body': 'Artist=AmandaTest+GilmoreTest&Item+description=blue+knit+dishtowel%2C+small+woven+wall+hanging&Category+description=towel%2C+tapestry&Taxable='"


def some_color():
  return RANDOM_COLORS[randint(1, 5)]


response = send_to_airtable('Inventory',
  {
    'Item ID': '12345',
    'Item description': f"a {some_color()} felted wool scarf",
    'Category description': 'scarf',
  })

pprint(response)