from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    input_text = request.args.get('textToAnalyze')
    result = emotion_detector(input_text)

    anger_text = str(result["anger"])
    disgust_text = str(result["disgust"])
    fear_text = str(result["fear"])
    joy_text = str(result["joy"])
    sadness_text = str(result["sadness"])
    emotions_text = f"{anger_text}, {disgust_text}, {fear_text}, {joy_text} and {sadness_text}"
    dominant_emotion_text = result["dominant_emotion"]

    return f"For the given statement, the system response is {emotions_text}. The dominant emotion is {dominant_emotion_text}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
