"""Flask application for Emotion Detection."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector  # Import your emotion detector function

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint for detecting emotions in a given text.

    Expects a POST request with JSON data containing the key 'text'.
    Returns a formatted response with emotion scores and dominant emotion.
    """

    # Extract text from the POST request
    input_data = request.json
    text_to_analyze = input_data.get("text")

    if not text_to_analyze:
        return "Invalid text! Please try again!"
    #Call the emotion detector function
    emotion_data=emotion_detector(text_to_analyze)
    #Format the output response for the customer
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_data['anger']}, 'disgust': {emotion_data['disgust']}, "
        f"'fear': {emotion_data['fear']}, 'joy': {emotion_data['joy']} and "
        f"'sadness': {emotion_data['sadness']}."
        f"The dominant emotion is <b>{emotion_data['dominant_emotion']}.</b>"
    )

    #Send the response
    return formatted_response
# Home route to render the HTML page (if required)
@app.route('/')
def index():
    """
    Home route that renders the index HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
