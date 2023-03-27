from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("Davlan/bert-base-multilingual-cased-ner-hrl")
model = AutoModelForTokenClassification.from_pretrained(
    "Davlan/bert-base-multilingual-cased-ner-hrl"
)

nlp = pipeline("ner", model=model, tokenizer=tokenizer)


def process_data(column):
    output = []
    for sent in column:
        ner = nlp(sent)
        output.append(ner)
    return output


def recognise_named_entities_multilingual(df):
    """
    This function takes a dataframe and finds the named entities for the two
    relevant columns.
    """
    df["id1_text_multi_NER"] = process_data[df["id1_text"].tolist()]
    df["id2_text_multi_NER"] = process_data[df["id2_text"].tolist()]
    return df
