import httpx
import numpy as np
import time
import textwrap
import socket

from googletrans import Translator
from utils import package_data


# attempt to fix a service timeout error
socket.setdefaulttimeout(15 * 1000)

# another attempt to fix a service timeout error
timeout = httpx.Timeout(100)
translator = Translator(timeout=timeout)

mdf_train = package_data(
    "../../data/semeval-2022_task8_train-data_batch_2.csv", "../../data/train_data"
)

# dividing data for smaller attempts
mdf_train_text_1 = mdf_train[["url1_lang", "id1_text"]]
mdf_train_text_2 = mdf_train[["url2_lang", "id2_text"]]

# dividing data for even smaller attempts
text1_slices = np.array_split(mdf_train_text_1, 10)
text2_slices = np.array_split(mdf_train_text_2, 10)

# code wasn't refactored because google banned the IP halfway through
with open("translations_text1.txt", "a") as f:
    for i, slice in enumerate(text1_slices):
        slice = slice.values.tolist()
        for j, row in enumerate(slice):
            if row[0] != "en":
                chunks = textwrap.wrap(row[1], 5000, break_long_words=False)
                container = []
                for chunk in chunks:
                    trans = translator.translate(chunk, src=row[0], dest="en")
                    container.append(trans.text)
                    time.sleep(5)
                f.write(" ".join(container) + " +++++++++++++++")
                print("Done with row " + str(j) + " from slice " + str(i))
                time.sleep(
                    15
                )  # a lot of sleep time trying not to be seen as a bot by google
            else:
                f.write(row[1] + " +++++++++++++++")
