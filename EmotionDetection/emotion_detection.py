import requests
import json

# Function to run emotion detection using Watson NLP
def emotion_detector(text_to_analyze):

      # Check if the input is blank
    if not text_to_analyze.strip():  # Using .strip() to check for whitespace
        # Return a dictionary with None values for all keys
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


    # Watson NLP Emotion Predict endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Construct input JSON with the text to be analyzed
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request to the Watson NLP Emotion Predict API
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 400:
            return 'Invalid text! Please try again!'

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            result = response.json()

            # Extract emotional data from the response
            emotions = result.get('emotionPredictions', [])
            if emotions:
                # Extract the emotions dictionary
                emotion_scores = emotions[0]['emotion']

                # Find the dominant emotion (the emotion with the highest score)
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)

                # Return the emotions dictionary along with the dominant emotion
                return {
                    'anger': emotion_scores['anger'],
                    'disgust': emotion_scores['disgust'],
                    'fear': emotion_scores['fear'],
                    'joy': emotion_scores['joy'],
                    'sadness': emotion_scores['sadness'],
                    'dominant_emotion': dominant_emotion
                }
            else:
                return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }
        else:
            # return f"Error: {response.status_code}, {response.text}"
            return "HELLO JI"

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example use case
if __name__ == "__main__":
    text = "I am so happy I am doing this."
    print(emotion_detector(text))
