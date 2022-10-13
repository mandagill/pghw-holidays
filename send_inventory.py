import json
import logging
from pprint import pprint
from urllib import response


def lambda_handler(event, context):
    payload = clean_up_data(event['multiValueQueryStringParameters'])
    response = send_to_airtable(payload)

    return {
        # TODO replace this boilerplate
        # return response
        'statusCode': 200,
        'body': json.dumps("Check your logs")
    }


def clean_up_data(raw_data):
  # TODO
  return pretty_dictionary


def send_to_airtable(data):
  """Takes a dictionary and sends it to Airtable, returns a status code from Airtable API"""

  at = airtable.Airtable(environ.get("BASE_ID"), environ.get("AIRTABLE_KEY"))

  return at.create('Inventory', data)
  

