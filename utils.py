from gensim.models import KeyedVectors
import numpy as np
import pandas as pd
import requests

mapping_url = 'http://www.uniprot.org/mapping/'
uniprot_url = 'http://www.uniprot.org/uniprot/'
query_string = 'yourlist:{} AND reviewed:yes'
search_params = {
    'columns': 'id',
    'format': 'tab',
    'query': query_string,
}

def load_embedding(path, binary = True):
    embedding = KeyedVectors.load_word2vec_format(path, binary = binary)
    print('embedding loaded from', path)
    return embedding

def cosine(a, b):
    norm1 = np.linalg.norm(a)
    norm2 = np.linalg.norm(b)
    return np.dot(a, b) / (norm1 * norm2)

def get_job_number(mapping_params):
    response = requests.get(mapping_url, params=mapping_params,
                            allow_redirects=False)
    return response.headers['location'].split('/')[-1].split('.')[0]

def get_filtered_uniprot_ids(mapping_params):
    job_num = get_job_number(mapping_params)
    search_params['query'] = query_string.format(job_num)
    response = requests.get(uniprot_url, search_params)
    return response.text

