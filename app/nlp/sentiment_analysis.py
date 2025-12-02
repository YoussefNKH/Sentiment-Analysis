# app/nlp/sentiment_analysis.py
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis",model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str):
    results = sentiment_analyzer(text)[0]
    label = results['label']
    if label == 'POSITIVE':
        return 'positive',results['score']
    elif label == 'NEGATIVE':
        return 'negative',results['score']
    else:
        return 'neutral',results['score']
    