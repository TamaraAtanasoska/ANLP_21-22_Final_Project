from sentence_transformers import SentenceTransformer


model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L12-v2")


def encode_to_sbert_embedding(df):
    """
    This function takes a dataframe and uses SBERT embeddings, with the model
    described above, to encode the text from the relevant columns. In this case
    just the title and summary are used since the end project evaluates just
    these parts, but it can be used on the full text too. However, using cosine
    similarity on the full text as encoded here won't work, and the text would have
    to be divided into smaller paragraphs and aggregated.
    """
    df["id1_title_encoded"] = df["id1_title"].apply(
        lambda x: model.encode(str(x), convert_to_tensor=True)
    )
    df["id2_title_encoded"] = df["id2_title"].apply(
        lambda x: model.encode(str(x), convert_to_tensor=True)
    )

    df["id1_summary_encoded"] = df["id1_text_summary"].apply(
        lambda x: model.encode(x, convert_to_tensor=True)
    )
    df["id2_summary_encoded"] = df["id2_text_summary"].apply(
        lambda x: model.encode(x, convert_to_tensor=True)
    )
    return df
