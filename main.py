import requests
from user_interface import UserInterface

# set up user interface
user_interface = UserInterface()

# make api call
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_answer = response.json()
