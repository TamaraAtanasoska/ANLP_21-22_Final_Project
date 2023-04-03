# SemEval 2022 Task 8: Multilingual News Article Similarity (Term project)
A final project for the course "Advanced Natural Language Processing" for the winter semester 2021/22. Part of the program Cognitive Systems at the University of Potsdam. The project is based on the data and description of the [SemEval 2022 Task 8: Multilingual News Article Similarity](https://competitions.codalab.org/competitions/33835#learn_the_details-overview). 

The end report/paper for the project going over the thought process, related papers and implementation can be found [here](Final_project_ANLP_Atanasoska.pdf).

### Environment recreation 

Run ```pip install -r setup/requirements.txt``` to install the necessary packages in your existing environment.

## Data

As with all data of this kind, the it must be individually scraped because of copyright reasons. The competition provided files that contained links and a a tool to download the data. The tool to scrape the data can be found here: [downloader](https://github.com/euagendas/semeval_8_2022_ia_downloader). It can be used like this: 

```
pip install semeval_8_2022_ia_downloader
python -m semeval_8_2022_ia_downloader.cli --links_file=<train/eval data> --dump_dir=<desired dir>
```

A `.html` and a `.json` file will be downloaded of the individual articles. The first will contain the website with the article, the second some additional data. The articles are grouped in a folder according ot their last two digits. For example, a the folter `train_data/10/` would contain the `.html` and `.json` files for the file `9876543210`, from the given pair `0123456789_9876543210`. The script will generate a `.csv` file of the articles it couldn't download. 

More details about the data are found on the [competition website](https://competitions.codalab.org/competitions/33835#learn_the_details-timetable). 

## API documentation

This repository contains an API that is used to explore the simplicity-performance trade-offs when it comes to finding similarity between two articles. The collected documentation for the API can be [accessed here](https://tamaraatanasoska.github.io/SemEval-2022-Task-8-Multilingual-News-Article-Similarity/). It shows a hirearchy of methods and collected docstrings.

## Usage

[This notebook](https://colab.research.google.com/drive/1k-2Pq858ADX6-A1j1oWpCIRPHs3zmj9K?usp=sharing) goes over all the API modular parts and shows how each of methods like summarisation, named entity recognition and disambiguation, similairty measurements and the encoding with different emebddings can be used in detail. The notebook starts with cloning the repository and recreating the environment and continues into neatly divided sections for each method. 
