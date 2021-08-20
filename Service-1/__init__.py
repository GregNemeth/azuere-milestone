import logging, requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey
# dev

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Initialize the Cosmos client
    endpoint = "endpoint URI here"
    key = 'primary key here'

    # <create_cosmos_client>
    client = CosmosClient(endpoint, key)
    # </create_cosmos_client>

    # Create a database
    # <create_database_if_not_exists>
    database_name = 'milestone-history'
    database = client.create_database_if_not_exists(id=database_name)
    # </create_database_if_not_exists>

    # Create a container
    # <create_container_if_not_exists>
    container_name = 'HistoryContainer'
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path="/username"),
        offer_throughput=400
    )
    # </create_container_if_not_exists>

    nums = requests.get('service_2 URI here')
    letters= requests.get('service_2 URI here')
    
    mix = ''
    for i in range(0, 5):
        mix += str(nums.text[i])
        mix += str(letters.text[i])

    item = {'id': 'username_id', 'username': mix}
    container.create_item(item)

    return func.HttpResponse(
            str(mix),
            status_code=200
    )
