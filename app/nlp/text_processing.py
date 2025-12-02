# app/nlp/text_processing.py
import re
import emoji
import nltk
from nltk.corpus import stopwords
import unicodedata
import functools


# lazy download stopwords
@functools.lru_cache(maxsize=1)
def get_stopwords():
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
    return set(stopwords.words('english'))



def clean_text(text: str) -> str:
    if not text:
        return ""
    text = str(text)
    # Remove URLs, mentions, hashtags
    text =re.sub(r'https?://\S+|www\.\S+|@\w+|#', '', text)
    # Remove special characters and numbers in one pass
    text = re.sub(r'[^\w\s]|\d+', '', text)
    # Remove emojis
    text = emoji.replace_emoji(text, replace='')

    # convert to lowercase
    text = text.lower()
    # Normalize Unicode characters
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])

    text = re.sub(r'\s+', ' ', text).strip()

    return text
def normalize_text(text, remove_stopwords=False):
    if not text:
        return ""
    text = clean_text(text)

    tokens = text.split()
    if remove_stopwords:
        stop_words = get_stopwords()
        tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)


    

