from collections import defaultdict
from os import path
import glob
import json

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


