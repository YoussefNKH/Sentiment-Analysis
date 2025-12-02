# app/nlp/topic_detection.py


# Simple keyword-based topic detection
def detect_topics(text: str):
    topics=[]
    keywords = {
        "depression": ["depression", "depressed", "sad", "hopeless", "empty"],
        "anxiety": ["anxiety", "anxious", "panic", "worry", "fear"],
        "therapy": ["therapy", "counseling", "treatment", "medication", "help"],
        "support": ["support", "community", "friend", "family", "talk"]
    }

    for topic, words in keywords.items():
        for word in words:
            if word in text.lower():
                topics.append(topic)
                break
    return topics if topics else ["general"]    
