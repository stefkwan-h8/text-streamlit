import requests
import json
from time import sleep

def cogniflow_request(model_url, api_key, input_text, attempt=3):

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

    data = {
        "text" : input_text
    }

    data_json = json.dumps(data)
    while attempt > 0:
        try:
            response = requests.post(model_url, headers=headers, data=data_json)
            result = response.json()
        except Exception as ex:
            attempt = attempt - 1
            if attempt > 0:
                print(f'Error trying to get cogniflow prediction endpoint. Retrying again in 3 seconds. '
                      f'Error: {str(ex)}')
                sleep(3)
            else:
                raise ex
        else:
            return result