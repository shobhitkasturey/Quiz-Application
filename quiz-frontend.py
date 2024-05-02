import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class QuizGUI:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.score = 0
        self.current_question = 0

        self.master.title("Quiz Game")
        self.master.geometry("500x300")

        # Background color for the webpage
        self.master.configure(bg="#f0f0f0")

        self.question_label = ttk.Label(master, text="", font=("Helvetica", 14), background="#ffffff")
        self.question_label.pack(pady=10)

        self.options_buttons = []
        for i in range(4):
            style = ttk.Style()
            style.configure("Quiz.TButton", background="#2196F3", foreground="#000000", font=("Helvetica", 12))
            button = ttk.Button(master, text="", command=lambda idx=i: self.check_answer(idx+1), style="Quiz.TButton")
            button.pack(fill=tk.X, padx=20, pady=5)
            self.options_buttons.append(button)

        self.next_button = ttk.Button(master, text="Next Question", command=self.next_question, style="Quiz.TButton")
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data['question'])
        options = question_data['options']
        for i in range(4):
            self.options_buttons[i].config(text=options[i])

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question]['answer']
        if user_answer == correct_answer:
            self.score += 1
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(self.questions)}")
            self.master.quit()

def main():
    root = tk.Tk()

    questions = [
        {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Berlin", "Rome"],
        'answer': 1
    },
    {
        'question': "What is 2 + 2?",
        'options': ["3", "4", "5", "6"],
        'answer': 2
    },
    {
        'question': "What is 45 + 59?",
        'options': ["105", "96", "110", "104"],
        'answer': 4
    },
    {
        'question': "What is 78 * 45?",
        'options': ["2500", "3490", "3600", "3510"],
        'answer': 4
    },
    {
        'question': "Who is the Prime-Minister Of Australia?",
        'options': ["Rahul Gandhi", "Narendra Modi", "David Hurley", "Anthony Albanese"],
        'answer': 4
    },
    {
        'question': "What is 4 + 5?",
        'options': ["3", "4", "9", "6"],
        'answer': 3
    },
    {
        'question': "What is 2 + 3?",
        'options': ["3", "4", "5", "6"],
        'answer': 3
    }
        # Add more questions here...
    ]

    quiz_gui = QuizGUI(root, questions)

    root.mainloop()

if __name__ == "__main__":
    main()
