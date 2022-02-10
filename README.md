# SemEval 2022 Task 8: Multilingual News Article Similarity (Term project)
A final project for the course "Advanced Natural Language Processing" for the winter semester 2021/22. Part of the program Cognitive Systems at the University of Potsdam. The project is based on the data and description of the [SemEval 2022 Task 8: Multilingual News Article Similarity](https://competitions.codalab.org/competitions/33835#learn_the_details-overview). 

The end report/paper for the project can also be found in the repo (not yet submitted, end od March 2022).

## Data

The competition could not provide the raw article text because of copyright reasons, so a tool was developed and made available to scrape the articles for every participant individually. I have uploaded the train and evaluation data documents that contain the links to the article pairs as given in the [data folder](data/). I attempted to scrape the data during the first week of February 2022, and there were already quite a few inaccessible articles from the train data. As a strategy against this, one can just omit the pairs with the missing data during training/evaluation, and the code I provide does this already. I was lucky to obtain the scraped data from an earlier point in time by a kind competition participant, so the number of pairs missing for me was marginal. I am currently not sure about the copyright issues and if I am allowed to push the whole data in this repo, and to stay on the safe side I will just link to the way to scrape them individually. 

The tool to scrape the data can be found here: [downloader](https://github.com/euagendas/semeval_8_2022_ia_downloader). It can be used like this: 

```
pip install semeval_8_2022_ia_downloader
python -m semeval_8_2022_ia_downloader.cli --links_file=<train/eval data> --dump_dir=<desired dir>
```

A `.html` and a `.json` file will be downloaded of the individual articles. The first will contain the website with the article, the second some additional data. The articles are grouped in a folder according ot their last two digits. For example, a the folter `train_data/10/` would contain the `.html` and `.json` files for the file `9876543210`, from the given pair `0123456789_9876543210`. The script will generate a `.csv` file of the articles it couldn't download. 

More details about the data are found on the [competition website](https://competitions.codalab.org/competitions/33835#learn_the_details-timetable). 





