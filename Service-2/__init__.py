import logging, random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    def list():
        list = ''
        for i in range(0, 5):
            list += str(random.randint(1,9))
        return list
        
    return func.HttpResponse(
             list()
        )
