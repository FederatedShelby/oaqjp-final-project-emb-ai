import requests
import json

def emotion_detector(text_to_analyze):
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  payload =  { "raw_document": { "text": text_to_analyze } }
  
  response = requests.post(url, headers=header, json=payload)

  if response.status_code == 400:
    return {
      'anger': None,
      'disgust': None,
      'fear': None,
      'joy': None,
      'sadness': None,
      'dominant_emotion': None
    }

  responseDict = json.loads(response.text)
  
  anger_score = responseDict["emotionPredictions"][0]["emotion"]["anger"]
  disgust_score = responseDict["emotionPredictions"][0]["emotion"]["disgust"]
  fear_score = responseDict["emotionPredictions"][0]["emotion"]["fear"]
  joy_score = responseDict["emotionPredictions"][0]["emotion"]["joy"]
  sadness_score = responseDict["emotionPredictions"][0]["emotion"]["sadness"]

  dominant_score = anger_score
  dominant_emotion = "anger"

  if disgust_score > dominant_score:
    dominant_score = disgust_score
    dominant_emotion = 'disgust'

  if fear_score > dominant_score:
    dominant_score = fear_score
    dominant_emotion = 'fear'

  if joy_score > dominant_score:
    dominant_score = joy_score
    dominant_emotion = 'joy'

  if sadness_score > dominant_score:
    dominant_score = sadness_score
    dominant_emotion = 'sadness'
  
  return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
  }