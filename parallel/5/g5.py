# System libraries:
import pandas as pd
import json
import nltk
import numpy as np
import os
import sys
import re

def import_yle_fi(fileNumber):
    # Original columns:
    #text - keep
    #analyzedText - drop
    #url - drop
    #publisher - drop
    #coverage - drop
    #timePublished - keep
    #headline - keep
    #score - drop
    #lead - keep

    analyzed_file_location = '/var/www/html/work/compressed/data/russia_finland/' \
        'analyzed/yle_finnish_mentioning_russia_' + str(fileNumber) + '.json'
    yle_fi_raw = None
    with open(analyzed_file_location,  encoding='utf-8') as json_data:
        yle_fi_raw = json_data.read().replace('}\n{', '},\n{')

    yle_fi_dict = json.loads(yle_fi_raw)

    yle_fi_data = pd.DataFrame.from_dict(yle_fi_dict['results']['docs'])

    drop_list = ['url', 'publisher', 'coverage', 'score']

    yle_fi_data = yle_fi_data.drop(columns = drop_list)

    return yle_fi_data

def get_lemmas(cell):
    lemma_list = []

    for sentence in cell:
        for word in sentence:
            lemma = word['analysis'][0]['wordParts'][0]['lemma']
            if not lemma == ' ':
                lemma_list.append(lemma)

    return lemma_list

def lemmatize_yle_fi_data(data):

    data['lemmas_content'] = data['analyzedText'].apply(get_lemmas)

    drop_list = ['analyzedText']

    data = data.drop(columns = drop_list)

    return data

def loop_all_source_files(start, end):
    data_list = []
    #for i in range(685):
    for i in range(end):
        data = import_yle_fi((i + start) * 100)
        lemmatized_data = lemmatize_yle_fi_data(data)
        data_list.append(lemmatized_data)
        print(i + start)

    dataframe = pd.concat(data_list)

    return dataframe


data = loop_all_source_files(300, 100)

data.to_csv('/var/www/html/work/compressed/data/russia_finland/processed/yle_fi_processed_05.csv', index=False)
