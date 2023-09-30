# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from summarize import summarize_text  # Import the summarize_text function from your summarize.py

app = Flask(__name__)

# Initialize CORS extension with your app
CORS(app)

# Define a landing page for the root URL
@app.route('/')
def landing_page():
    return 'Welcome to the Text Summarizer API'

# Define the /api/summarize endpoint to handle POST requests
@app.route('/api/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        data = request.get_json()
        text_to_summarize = data.get('text')

        if text_to_summarize:
            # Call the summarize_text function from summarize.py
            summary = summarize_text(text_to_summarize)

            # Return the summary as a JSON response
            return jsonify({'summary': summary}), 200
        else:
            return jsonify({'error': 'Text data not provided in the request'}), 400
    else:
        return jsonify({'error': 'Invalid request method'}), 405

if __name__ == '__main__':
    app.run(debug=True)
