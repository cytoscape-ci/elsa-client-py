import requests

DEFAULT_ELSA = 'http://localhost:8080/'

REG_FILE_NAME = 'request.json'

DEFAULTS = {

    "service": "ci-service",
    "version": "v1",
    "instances": [
        {
            "location": "https://192.168.99.100:3000",
            "capacity": "infinity"
        }
    ]
}

RETRY = {
    "max": 3,
    "interval": 10
}


class ElsaClient:



    @staticmethod
    def register(elsa_url, path='.', ):
        pass

