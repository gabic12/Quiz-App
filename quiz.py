import html #To clear the HTML Entities

class Quiz:
    """Brain of the Quiz"""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Checks if it reached the last question from the list"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Returns the next question from the list"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

    def check_answer(self, user_answer):
        """Checks the user answer with the correct answer"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False