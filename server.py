''' Executing this function initiates the application of emotion detector to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """Code receive text from HTML and runs emotion_detector over it."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    #format the response
    format_resp = (
        f'For the given statement, the system repsonse is "anger": {anger_score}, "disgust": {disgust_score}, "fear": {fear_score}, "joy": {joy_score},'
        f' and "sadness": {sadness_score}. The dominant emotions is <b>{dominant_emotion}</b>.'
    )
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return format_resp

@app.route("/")
def render_index_page():
    """Initiate rendering of main application over Flask"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
