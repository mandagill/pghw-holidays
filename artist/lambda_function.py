import json
from python import airtable
import logging
import random

from pprint import pprint
from os import environ


def send_to_airtable(artist_name, email):
  """Takes an artist's name as a parameter, assigns a random Artist ID to the name and sends it to Airtable, returns a status code from Airtable API"""

  at = airtable.Airtable(environ.get("BASE_ID"), environ.get("AIRTABLE_KEY"))
  
  data = {
    'Vendor ID number': random.randrange(10000, 99999),
    'Name': artist_name,
    'Email': email
  }
  logging.info(f"Artist {artist_name} has been assigned id number {data['Vendor ID number']}")
  return at.create('Artists', data)


def lambda_handler(event, context):
    status_code = 502
    response_to_webhook = "The data from Gravity Forms was not handled as expected"
    
    pprint(f"this is the full event: {event}")

    name = event["Name"]
    email = event["Email"] 

    try:
      status_code = 200
      response = send_to_airtable(name, email)
      response_to_webhook = 'Artist ID was sent to the spreadsheet'
      logging.info(f"Record ID was created in Airtable: {pprint(response['id'])}")
    except:
      pass

    return {
        'statusCode': status_code,
        'body': json.dumps(response_to_webhook)
    }
