'''
import modules
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    This code receives the text from the HTML interface and 
    runs emotion detection using emotion_detector()
    function. The output returned shows the scores for each
    emotion and the dominant emotion for the provided text.
    '''
    input_text = request.args.get('textToAnalyze')
    result = emotion_detector(input_text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger_text = str(result["anger"])
    disgust_text = str(result["disgust"])
    fear_text = str(result["fear"])
    joy_text = str(result["joy"])
    sadness_text = str(result["sadness"])
    emotions_text = f"{anger_text}, {disgust_text}, {fear_text}, {joy_text} and {sadness_text}"
    dominant_emotion_text = result["dominant_emotion"]

    text_first = f"For the given statement, the system response is {emotions_text}. "
    text_last = f"The dominant emotion is {dominant_emotion_text}."

    return text_first + text_last

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
