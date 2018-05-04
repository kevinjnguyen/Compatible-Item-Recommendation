import gzip

META_CELLPHONE = '../Datasets/meta_Cell_Phones_and_Accessories.json.gz'

def get_documents(file_name):
    g = gzip.open(file_name, 'r')
    results = []
    for line in g:
        document = eval(line)
        results.append(document)
    return results

all_documents = get_documents(META_CELLPHONE)

import os
api_key = os.environ['GOOGLE_KEY']

import requests
import json

LANGUAGE_ENDPOINT = 'https://language.googleapis.com/v1/documents:analyzeEntities?key={}'.format(api_key)

def merge_title_description(document):
    title = ''
    description = ''
    if 'title' in document:
        title = document['title']
    if 'description' in document:
        description = document['description']
    return title + description

def perform_api_request(document):
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "EN",
            "content": merge_title_description(document)
        },
        "encodingType": "UTF8"
    }

    r = requests.post(LANGUAGE_ENDPOINT, data=json.dumps(payload))
    return r.text

def save_api_request(document_name, r):
    file_name = 'Processed/{}.json'.format(document_name)
    with open(file_name, 'w') as outfile:
        json_data = json.dump(r, outfile)

def process_all_documents(all_documents):
    for document in all_documents:
        asin = document['asin']
        already_processed = os.path.exists('Processed/{}.json'.format(asin))
        if not already_processed:
            r = perform_api_request(document)
            save_api_request(asin, r)

process_all_documents(all_documents)