import json
import logging
from pprint import pprint

from package import airtable
from os import environ


def lambda_handler(event, context):
    inventory = json.loads(event['body']) 
    inventory_list = prepare_payload(request_body=inventory)
    send_to_airtable(inventory_list)
    
    return {
        'statusCode': 200,
        'body': json.dumps("Check your logs")
    }
    

def prepare_payload(request_body):
  """Create a dictionary per inventory item, return a list of dicts"""
  # TODO
  pass
    

def send_to_airtable(data):
  """Takes a dictionary and sends it to Airtable, returns a status code from Airtable API"""
  # TODO add error handling 
  at = airtable.Airtable(environ.get("BASE_ID"), environ.get("AIRTABLE_KEY"))

  for each_inventory_item in data:
    at.create("Inventory", each_inventory_item)
  
  return 
  