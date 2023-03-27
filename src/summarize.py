from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-summarize-news")
model = AutoModelForSeq2SeqLM.from_pretrained(
    "mrm8488/t5-base-finetuned-summarize-news", max_length=250
)


def generate_summary(sent):
    """
    Takes one text and generates a summary using the model with it's
    characteristics defined above.
    """
    input_ids = tokenizer(
        sent, return_tensors="pt", padding=True, truncation=True
    ).input_ids
    generations = model.generate(input_ids)
    output_ids = tokenizer.decode(generations[0], skip_special_tokens=True)
    return output_ids


def process_data(column):
    output = []
    for sent in column:
        summ = generate_summary(sent)
        # sometimes the model generates a string at the end with extra "nnn.." symbols
        output.append(summ.split(".nnn")[0])
    return output


def summarize(df):
    """
    This function takes a dataframe generates summaries for the two relevant
    columns that contain the full text.
    """
    df["id1_text"] = "summarize:" + df.id1_text
    df["id2_text"] = "summarize:" + df.id2_text

    df["id1_text_summary"] = process_data[df["id1_text"].tolist()]
    df["id2_text_summary"] = process_data[df["id2_text"].tolist()]

    df["id1_text"] = df["id1_text"].apply(lambda x: x.replace("summarize:", ""))
    df["id2_text"] = df["id1_text"].apply(lambda x: x.replace("summarize:", ""))
    return df
