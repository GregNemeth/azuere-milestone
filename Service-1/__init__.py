import logging, requests

import azure.functions as func
# dev

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    nums = requests.get('http://localhost:7071/api/Service-2')
    letters= requests.get('http://localhost:7071/api/Service-3')
    
    mix = ''
    for i in range(0, 5):
        mix += str(nums.text[i])
        mix += str(letters.text[i])

    return func.HttpResponse(
            mix,
            status_code=200
    )
