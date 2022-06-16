import requests

# make a API request to the Open TRIVIA databse API to get a set of random 10 questions  
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status() # raise error if request is not OK 
data = response.json() # response data
question_data = (data["results"]) # extract values for the "results" key 
