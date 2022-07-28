from tkinter import *
from quiz_format import Quiz

class UserInterface:

    def __init__(self, quiz_format: Quiz):
        self.quiz = quiz_format
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=30, pady=30, bg="blue")

        # create label
        self.score = Label(text="Score: 0", fg="white", bg="blue")
        self.score.grid(row=0, column=1)

        # create canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text((150, 125), width=280, text="questions here", fill="blue", font=("Arial", 16))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # create buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

    def get_next_question(self):
        '''display next question'''
        self.canvas.config(bg="white")
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)

        self.window.mainloop()
        