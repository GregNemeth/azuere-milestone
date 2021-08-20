import logging, requests

import azure.functions as func
# dev

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    nums = requests.get('https://gregs-milestone-project.azurewebsites.net/api/Service-2?code=/M7a3FflKMrPMMzR3v4f0FnOVkkzxmwm6/Ax6WQMzLCmCZX4uqPicQ==')
    letters= requests.get('https://gregs-milestone-project.azurewebsites.net/api/Service-3?code=QlhtSbWv7tgetWutjIZ0JxNJasKrbTB3NGFiFJ47oHIGRB3d3SsHDQ==')
    
    mix = ''
    for i in range(0, 5):
        mix += str(nums.text[i])
        mix += str(letters.text[i])

    return func.HttpResponse(
            str(mix),
            status_code=200
    )
