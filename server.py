"""Flask web application that detects emotion in text using a custom EmotionDetection module."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text emotion score and return the results."""
    text = request.args.get("textToAnalyze")
    emotions = emotion_detector(text)

    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
