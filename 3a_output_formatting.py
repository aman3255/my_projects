def emotion_predictor(text):
    emotions = emotion_detector(text)
    return {
        "text": text,
        "emotions": {
            "anger": emotions.get('anger', 0),
            "joy": emotions.get('joy', 0),
            "sadness": emotions.get('sadness', 0),
            "fear": emotions.get('fear', 0),
            "disgust": emotions.get('disgust', 0)
        }
    }
