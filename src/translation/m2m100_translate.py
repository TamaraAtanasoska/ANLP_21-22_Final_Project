from transformers import AutoTokenizer, M2M100ForConditionalGeneration
import pandas as pd

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = AutoTokenizer.from_pretrained("facebook/m2m100_418M")

# create a dataframe from all train data
mdf_train = package_data(
    "data/semeval-2022_task8_train-data_batch_2.csv", "data/train_data"
)

# create separate chunks for easier traslation and monitoring
mdf_train_title_1 = mdf_train[["url1_lang", "id1_title"]].values.tolist()
mdf_train_title_2 = mdf_train[["url2_lang", "id2_title"]].values.tolist()
mdf_train_text_1 = mdf_train[["url1_lang", "id1_text"]].values.tolist()
mdf_train_text_2 = mdf_train[["url2_lang", "id2_text"]].values.tolist()

df_list = [mdf_train_title_1, mdf_train_title_2, mdf_train_text_1, mdf_train_text_2]

for i, df in enumerate(df_list):
    temp = []
    for j, row in enumerate(df):
        if row[0] != "en":
            tokenizer.src_lang = row[0]
            model_inputs = tokenizer(
                row[1], return_tensors="pt", padding=True, truncation=True
            )
            gen_tokens = model.generate(
                **model_inputs, forced_bos_token_id=tokenizer.get_lang_id("en")
            )
            temp.append(tokenizer.batch_decode(gen_tokens, skip_special_tokens=True))
        else:
            temp.append(row[1])
        if j % 100 == 0:
            print(j)
    temp_df = pd.DataFrame(temp)
    temp_df.to_csv("translations_tran_data_df" + str(i + 1) + ".csv")
