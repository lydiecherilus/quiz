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
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()
        

    def get_next_question(self):
        '''display next question'''
        self.canvas.config(bg="white")
        if self.quiz.is_question_left():
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=(f"The quiz is completed.\nYour final score is: {self.quiz.score}/{self.quiz.question_number}"))
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_button_clicked(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    

    def false_button_clicked(self):
        right_answer = self.quiz.check_answer("False")
        if right_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
