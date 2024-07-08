# Import the requests library for making HTTP requests
import requests

# Define a dictionary of parameters for the API request
parameters = {
    "amount": 10,  # Request 10 questions
    "type": "boolean",  # Request only true/false questions
}

# Send a GET request to the Open Trivia Database API
response = requests.get("https://opentdb.com/api.php", params=parameters)

# Raise an exception for any HTTP errors (4xx or 5xx status codes)
response.raise_for_status()

# Parse the JSON response into a Python dictionary
data = response.json()

# Extract the "results" list from the response data
# This list contains the actual question data
question_data = data["results"]
