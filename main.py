import requests
from user_interface import UserInterface
from question_format import Question


# make api call
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
questions_answers = response.json()

# set up user interface
user_interface = UserInterface()

# set up questions
all_questions = []
for question in questions_answers["results"]:
    quiz_question = question["question"]
    quiz_answer = question["correct_answer"]
    new_question = Question(quiz_question, quiz_answer)
    all_questions.append(new_question)
