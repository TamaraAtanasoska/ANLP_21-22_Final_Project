import ast
import spacy

from sentence_transformers import SentenceTransformer, util


nlp_model_en = spacy.load("en_core_web_sm")
nlp_model_en.add_pipe("entityfishing")
nlp = spacy.load("en_core_web_lg")


def NER_and_NED(df):
    """
    This function takes a dataframe and performs the tasks for named entity
    recognition and named entitiy disambiguation on the relevant columns.
    The spaCy EntityRecogniser is used, as well as a package called
    entityfishing that does NED with Wikipedia.
    In a column as a tuple the following information is saved:
    - ne.text: the string as it appears in the orginal text
    - ne.label_: the disambiguated label of the type of NE (ex. PERSON, LOC etc.)
    - ne._.kb_qid: the identifier connecting the entitty to a Wikipedia article
    - ne._.nerd_score: confidence score
    """
    df["NE_summary_1"] = df["id1_text_summary"].apply(
        lambda x: [
            (e.text, e.label_, e._.kb_qid, e._.nerd_score)
            for e in nlp_model_en(str(x)).ents
        ]
    )
    df["NE_summary_2"] = df["id2_text_summary"].apply(
        lambda x: [
            (e.text, e.label_, e._.kb_qid, e._.nerd_score)
            for e in nlp_model_en(str(x)).ents
        ]
    )
    return df


def divide_named_entitites_in_two_types(column):
    """
    This function divides the named entities into two lists. One containes all
    the named entities that belong to the categories of geo-political entities,
    locations, date and time, and the other all the rest. This division is
    relevant to how the task is posed and to explore similarity aspects.
    """
    ner_list = column
    tags_list = ["GPE", "LOC", "DATE", "TIME"]

    gpe_loc_date_time = []
    rest = []
    for row in ner_list:
        tuples = ast.literal_eval(row)
        tags_ent = [list(t)[0] for t in tuples if list(t)[1] in tags_list]
        rest_ent = [list(t)[0] for t in tuples if list(t)[1] not in tags_list]
        gpe_loc_date_time.append(" ".join(list(set(tags_ent))))
        rest.append(" ".join(list(set(rest_ent))))
    return (gpe_loc_date_time, rest)


def transform_named_entities_into_a_big_sentence(column):
    """
    This function takes a column with named entities and creates one big
    sentence containing all named entities as words, without any of the other
    information.
    """
    transformed_ner = []
    for row in column:
        tuples = ast.literal_eval(row)
        list_ent = [list(t)[0] for t in tuples]
        transformed_ner.append(" ".join(list_ent))
    return transformed_ner


def encode_to_sentence_embeddings_and_find_cos_sim(texts):
    similarity = []
    t1 = texts[0]
    t2 = texts[1]
    for n, i in enumerate(t1):
        text_1 = model.encode(t1[n], convert_to_tensor=True)
        text_2 = model.encode(t2[n], convert_to_tensor=True)
        similarity.append(util.cos_sim(text_1, text_2).item())
    return similarity


def transform_named_entities_to_a_sentence_and_spacy_doc(column):
    """
    This function takes a column with named entities and transforms them into
    one large sentence and then to a spaCy document fof further processing.
    """
    transformed_ner = []
    for row in column:
        tuples = ast.literal_eval(row)
        list_ent = [list(t)[0] for t in tuples]
        transformed_ner.append(nlp(" ".join(list_ent)))
    return transformed_ner


def spacy_similarity_with_word_embeddings(texts):
    similarity = []
    t1 = texts[0]
    t2 = texts[1]
    for n, i in enumerate(t1):
        similarity.append(t1[n].similarity(t2[n]))
    return similarity


def get_text_label_and_wiki_identifier_named_entities(column):
    """
    This function takes a column with named entities and prunes the information
    to just the text as it appears in the string, the disambiguated label and wiki
    concept identifier.
    """
    transformed_ner = []
    for row in column:
        tuples = ast.literal_eval(row)
        list_ent = [list(t)[:3] for t in tuples]
        clean_lst = [[l for l in lst if l is not None] for lst in list_ent]
        sentences = [" ".join(l) for l in clean_lst]
        one_doc = ". ".join(sentences)
        transformed_ner.append(one_doc)
    return transformed_ner
