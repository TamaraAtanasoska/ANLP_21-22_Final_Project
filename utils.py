import glob
import json
import os

from collections import defaultdict
from os import path

import pandas as pd


def prepare_texts(base_path: str) -> pd.DataFrame:
    """
    A function to prepare data. Takes in the path of the data 
    and returns a dataframe that contains the article id, the 
    title and the text. The article id can be then used to 
    find the right raw text for the article pair ids.  
    """
    d = defaultdict(list)
    texts = []

    for file in glob.iglob(path.join(base_path, '*/*.json'), recursive=True):
        jdict = json.load(open(file))
        texts.append([(os.path.splitext(os.path.basename(file))[0]), \
                       jdict['title'], jdict['text']])


    tdf = pd.DataFrame(texts, columns=['id', 'title', 'text'])
    return tdf


def package_data(pair_data_path: str, scraped_data_path: str) -> pd.DataFrame:
    """
    A function to package the data for processing into one dataframe. 
    it combines the data in the original .csv file with the scraped, 
    raw texts. The links are cleaned and they are replaced by titles and text
    for both of the articles in the given pair. 
    """
    data = pd.read_csv(pair_data_path) 
    data = data.drop(columns=['link1', 'link2', 'ia_link1', 'ia_link2'])
    data['id1'] = data.pair_id.str.split('_').str[0]
    data['id2'] = data.pair_id.str.split('_').str[-1]

    tdf = prepare_texts(scraped_data_path)
    mdf = pd.merge(data, tdf, how='left', left_on=['id1'], right_on=['id'])
    mdf.rename(columns={'text':'id1_text', 'title':'id1_title'}, inplace=True)
    mdf.drop(columns=['id', 'id1'], inplace=True)

    mdf = pd.merge(mdf, tdf, how='left', left_on=['id2'], right_on=['id'])
    mdf.rename(columns={'text':'id2_text', 'title':'id2_title'}, inplace=True)
    mdf.drop(columns=['id', 'id2'], inplace=True)

    return mdf
