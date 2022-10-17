import json
from package import airtable
import logging
import random

from pprint import pprint
from os import environ


def send_to_airtable(artist_name, email):
  """Takes an artist's name as a parameter, assigns a random Artist ID to the name and sends it to Airtable, returns a status code from Airtable API"""

  at = airtable.Airtable(environ.get("BASE_ID"), environ.get("AIRTABLE_KEY"))
  
  data = {
    'Vendor ID number': random.randrange(10000, 99999),
    'Name': f"{artist_name}",
    'Email': email
  }
  logging.info(f"Artist {artist_name} has been assigned id number {data['Vendor ID number']}")
  return at.create('Artists', data)


def lambda_handler(event, context):
    status_code = 200
    response_to_webhook = 'an attempt was made to send data to the spreadsheet'

    name = event['Name']
    email = event['email'] 

    try:
      response = send_to_airtable(name, email)
      if response is not None:
        status_code = 502
        logging.critical(f"A non-None response was returned from Airtable: {pprint(response)}")
    except:
      status_code = 502

    return {
        'statusCode': status_code,
        'body': json.dumps(response_to_webhook)
    }
