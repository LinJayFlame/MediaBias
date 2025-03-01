# Activate virtual environment first through venv/Scripts/activate
# and install dependencies in requirements.txt
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

def sentimentAnalysis(articleList: list[str]):
    model_name = "siebert/sentiment-roberta-large-english"
    tokeniser = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    trainer = Trainer(model=model)

    scoreList = []
    for article in tqdm.tqdm(articleList):
        scoreList.append(get_score(article, tokeniser, trainer))

    scoreArray = np.array(scoreList)
    return scoreArray.mean()
        
def get_score(file: str, tokeniser, trainer):
    filename = 'data/' + file
    data = pd.read_csv(filename)
    
    raw_sentences = data["text"]
    sentences = [s for s in raw_sentences if len(s) > 1]

    tokenized_texts = tokeniser(sentences,truncation=True,padding=True)
    dataset = SimpleDataset(tokenized_texts)
    predictions = trainer.predict(dataset)

    scores = predictions.predictions.argmax(-1)
    return scores.mean()

score = sentimentAnalysis(["HBR_1.csv"])
print(score)