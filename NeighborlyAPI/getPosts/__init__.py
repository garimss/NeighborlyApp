import logging
import azure.functions as func
from pymongo import MongoClient
import json
from bson.json_util import dumps
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ['MyDbConnection']  # TODO: Update with appropriate MongoDB connection information
        client = MongoClient(url)
        database = client['neighborly_mangodb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)