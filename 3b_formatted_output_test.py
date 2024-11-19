from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def emotion_detector(text):
    # Watson API Setup
    api_key = '<your_api_key>'
    url = '<your_api_url>'
    authenticator = IAMAuthenticator(api_key)
    nlu = NaturalLanguageUnderstandingV1(version='2021-08-01', authenticator=authenticator)
    nlu.set_service_url(url)

    # Analyze text
    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())).get_result()

    return response['emotion']['document']['emotion']
