import json
import logging
import re
from package import airtable

from os import environ
from pprint import pprint
from urllib import response

ID_INDEX = 0
CATEGORY_INDEX = 1
DESCRIPTION_INDEX = 2
PRICE_INDEX = 3


def extract_artist_id(janky_string):
  regex_object = re.search("ID\=\d{5}", janky_string)
  param = regex_object.group()
  artist_id = param[3:]
  return artist_id

def lambda_handler(event, context):

    inventory_as_string = event['multiValueQueryStringParameters'].values()
    artist = extract_artist_id(event['body'])
    inventory_items = prepare_payload(artist, inventory_as_string)
    
    for each_line in inventory_items:
      response = send_to_airtable(each_line)
      if response is not None:
        # logging.critical(f"an inventory item failed to send to Airtable, inventory ID is {artist_id}-{each_line['Item ID']}.")
        pass
    
    return {
        'statusCode': 200,
        'body': json.dumps("Inventory batch has been sent to the spreadsheet.")
    }
    

def prepare_payload(artist, query_parameters):
  """returns a list of dictionaries, each dictionary
   representing a single line in the spreadsheet to 
   send to airtable"""
  payload_dictionary = {}
    
  return payload_dictionary
    
    
def send_to_airtable(table_name, data):
  """Takes a dictionary and sends it to Airtable, returns a status code from Airtable API"""

  at = airtable.Airtable(environ.get("BASE_ID"), environ.get("AIRTABLE_KEY"))

  return at.create(table_name, data)
  

