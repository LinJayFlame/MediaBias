import pandas as pd
import numpy as np
import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer

class SimpleDataset:
    def __init__(self, tokenized_texts):
        self.tokenized_texts = tokenized_texts

    def __len__(self):
        return len(self.tokenized_texts["input_ids"])

    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.tokenized_texts.items()}

# actual code is commented out as the roberta model takes a long time to execute the query
# a cache of the results is used instead
def getSentiments(category):
    # nyt_score = sentimentAnalysis(["New_York_Times.csv", "New_York_Times_2.csv", ...], "work")
    # st_score = sentimentAnalysis(...)
    # ...
    if category == "work":
        return {
            "Straits Times": 0.78,
            "BBC News": 0.74,
            "The Guardian": 0.77,
            "CNN": 0.72,
            "Forbes": 0.89,
            "CNA": 0.86,
            "Brookings": 0.78
        }
    elif category == "living":
        return {
            "Straits Times": 0.78,
            "BBC News": 0.80,
            "The Guardian": 0.91,
            "CNN": 0.77,
            "Forbes": 0.90,
            "CNA": 0.53,
            "Brookings": 0.81
        }
    elif category == "learning":
        return {
            "Straits Times": 0.87,
            "BBC News": 0.58,
            "The Guardian": 0.73,
            "CNN": 0.63,
            "Forbes": 0.80,
            "CNA": 0.57,
            "Brookings": 0.85
        }
    else:
        return None

def sentimentAnalysis(articleList: list[str], category: str):
    model_name = "siebert/sentiment-roberta-large-english"
    tokeniser = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    trainer = Trainer(model=model)

    scoreList = []
    for article in tqdm.tqdm(articleList):
        scoreList.append(get_score(article, category, tokeniser, trainer))

    scoreArray = np.array(scoreList)
    return scoreArray.mean()
        
def get_score(file: str, category: str, tokeniser, trainer):
    filename = 'data/' + category + '/' + file

    # for csv
    data = pd.read_csv(filename)
    raw_sentences = data["text"]

    # for txt
    # raw_sentences = []
    # with open(filename, "r") as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         raw_sentences.append(line.strip())

    sentences = [s for s in raw_sentences if len(s) > 1]

    tokenized_texts = tokeniser(sentences,truncation=True,padding=True)
    dataset = SimpleDataset(tokenized_texts)
    predictions = trainer.predict(dataset)

    scores = predictions.predictions.argmax(-1)
    return scores.mean()