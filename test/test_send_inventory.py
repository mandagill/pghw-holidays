import unittest

from inventory import send_inventory
from pprint import pprint
from random import randint


class TestSendInventory(unittest.TestCase):

  RANDOM_COLORS = ['', 'red', 'blue', 'green', 'purple', 'yellow', '']


  def some_color(self):
    return self.RANDOM_COLORS[randint(1, 5)]


  def test_airtable_calls_succeed(self):
    base_case = {
      'Item ID': '12345',
      'Item description': f"a {self.some_color()} felted wool scarf",
      'Category description': 'scarf',
    }

    response = send_inventory.send_to_airtable(base_case)

    self.assertNotError(response)


  def test_parse_inventory_with_commas(self):
    unprepared_payload = {'Item description': 'purple scarf woven with hand spun merino, purple woven shirt, spun merino cotton blend, purple, red, blue, orange woven tapestry, 10x2 inches', 'Category description': 'Scarf, Shirt, Wall tapestry', 'Price': '100, 100, 75', 'Name': 'TestUser'}

    list_of_dicts = send_inventory.prepare_payload(unprepared_payload)

    expected = [{'Item ID': 1, 'Artist': 'TestUser', 'Item description': 'purple scarf woven with hand spun merino', 'Category description': 'Scarf', 'Price': 100}, {'Item ID': 2, 'Artist': 'TestUser', 'Item description': 'purple woven shirt, spun merino cotton blend', 'Category description': 'Shirt', 'Price': 100}, {'Item ID': 3, 'Artist': 'TestUser', 'Item description': 'purple, red, blue, orange woven tapestry, 10x2 inches', 'Category description': 'Wall tapestry', 'Price': 75}]

    self.assertEquals(list_of_dicts, expected)
