from question_model import Question
from data import question_data
from quiz import Quiz
from user_interface import UserInterface

question_list = []
#Populate the question list with the result from the API call
for question in question_data["results"]: #List of dictionaries
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)


quiz = Quiz(question_list)
quiz_ui = UserInterface(quiz)