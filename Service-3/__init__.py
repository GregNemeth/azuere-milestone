import logging, random, string
import azure.functions as func

random.choice(string.ascii_letters)
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    def listletters():
        list = ''
        for i in range(0, 5):
            list += random.choice(string.ascii_letters)
        return list
        
    return func.HttpResponse(
             listletters()
        )
