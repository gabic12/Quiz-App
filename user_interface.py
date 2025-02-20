from tkinter import *
from quiz import Quiz

class UserInterface:
    """Quiz UI"""
    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        """Set up the UI with Tkinter"""
        #Window
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg="#375362")

        #Label
        self.score_label = Label(text="Score: 0", bg="#375362", fg="white")
        self.score_label.grid(row=1, column=2)

        #Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill="#375362",font=("Arial", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        #Images and buttons
        true_button_image = PhotoImage(file="images/true.png")
        false_button_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.answer_is_true)
        self.true_button.grid(row=3, column=1)
        self.wrong_button = Button(image=false_button_image, highlightthickness=0, command=self.answer_is_false)
        self.wrong_button.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Turns the canvas to white and displays the next question, until the end of the quiz"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def answer_is_true(self):
        """Returns true"""
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_is_false(self):
        """Returns false"""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Based on the button clicked, the canvas will flash green for a correct one or red for a wrong one"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question) #Wait 1 sec, then display the next question