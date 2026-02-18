# quiz application gui project
# by shassh umamaheswaran
# period 4 AP CSP

import tkinter as tk
from tkinter import messagebox

# colors
BG_COLOR = "#1a1a2e"
FRAME_BG = "#2d3748"
BUTTON_BG = "#2b5278"
BUTTON_HOVER = "#3d6a99"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#5dade2"
CORRECT_COLOR = "#a6e3a1"
WRONG_COLOR = "#f38ba8"

# window setup
window = tk.Tk()
window.title("How much do you know about CAMS?")
window.geometry("520x650")
window.resizable(False, False)
window.configure(bg=BG_COLOR) 

# quiz data 
quiz_data = [
    {
        "question": "Who was the Chemistry teacher that came before Ms. Brodeur?",
        "choices": ["Mrs. Herrera", "Mrs. Gransfield", "Mr. Herald", "Mrs. Daisy"],
        "answer": "Mrs. Herrera"
    },
    {
        "question": "Who's the tallest teacher?",
        "choices": ["Mr. Virak", "Mr. Carpenter", "Mr. Hoffman", "Mr. Gallardo"],
        "answer": "Mr. Hoffman"
    },
    {
        "question": "What's the name of the current Vice Principal?",
        "choices": ["Ms. Hoang", "Mr. Yu", "Ms. Bellie"],
        "answer": "Ms. Hoang"
    },
    {
        "question": "Which class does Mr. Harder not teach?",
        "choices": ["Aerospace", "Digital Electronics", "Principles of Engineering", "Computer Integrated Manufacturing"],
        "answer": "Principles of Engineering"
    },
    {
        "question": "Which teacher helps organize Link Crew?",
        "choices": ["Mr. Gallardo", "Ms. King", "Mrs. Imatomi", "Mrs. Cornejo"],
        "answer": "Ms. King"
    },
    {
        "question": "Which class here isn't taught at CAMS?",
        "choices": ["AP Gov", "Economics", "Anat Phys", "AP Human Geography"],
        "answer": "AP Gov"
    },
    {
        "question": "What was the class mascot for the 2023 class?",
        "choices": ["Narwhals", "Pythons", "Pandas", "Cobras"],
        "answer": "Cobras"
    },
    {
        "question": "The panthers originally had a different mascot, so what was it?",
        "choices": ["Ducks", "Flamingos", "Beavers", "Dolphins"],
        "answer": "Ducks"
    },
    {
        "question": "Who's the best teacher?",
        "choices": ["Mrs. Dreyfus", "Mr. Virak", "Mr. Gallardo", "Mr. Carpenter"],
        "answer": "Mr. Virak"
    },
]

# tracking variables
current_question = 0
score = 0
selected_answer = ""

# widgets

# title label
label_title = tk.Label(window, text="How Much Do You Know About CAMS?",
                        font=("Arial", 20, "bold"),
                        bg=BG_COLOR, fg=ACCENT_COLOR)
label_title.pack(pady=(20, 5))

# progress label
label_progress = tk.Label(window, text="", font=("Arial", 12),
                           bg=BG_COLOR, fg="gray")
label_progress.pack()

# question label
label_question = tk.Label(window, text="", font=("Arial", 15),
                           bg=BG_COLOR, fg=TEXT_COLOR, wraplength=450)
label_question.pack(pady=(15, 10))

# frame to hold choice buttons
frame_choices = tk.Frame(window, bg=BG_COLOR)
frame_choices.pack(pady=5)

# choice buttons stored here
choice_buttons = []


def select_choice(choice):
    """Handle clicking a choice button — highlight it as selected."""
    global selected_answer
    selected_answer = choice
    # reset all buttons to default, highlight selected
    for b in choice_buttons:
        if b.cget("text") == choice:
            b.configure(bg=BUTTON_HOVER, fg=TEXT_COLOR, relief=tk.SUNKEN,
                        highlightbackground=ACCENT_COLOR, highlightthickness=2)
        else:
            b.configure(bg=BUTTON_BG, fg=TEXT_COLOR, relief=tk.RAISED,
                        highlightthickness=0)


# submit button
btn_submit = tk.Button(window, text="Submit Answer", font=("Arial", 14, "bold"),
                        bg=ACCENT_COLOR, fg=BG_COLOR,
                        activebackground="#3d8ec9", activeforeground="white",
                        relief=tk.RAISED, bd=2, cursor="hand2",
                        command=lambda: check_answer())
btn_submit.pack(pady=15)

# feedback label
label_feedback = tk.Label(window, text="", font=("Arial", 14, "bold"),
                           bg=BG_COLOR)
label_feedback.pack(pady=5)

# score label
label_score = tk.Label(window, text="Score: 0/0", font=("Arial", 12),
                        bg=BG_COLOR, fg=TEXT_COLOR)
label_score.pack(pady=5)


# program logic 
def load_question():
    """Load the current question and its choices into the GUI."""
    global selected_answer
    label_feedback.configure(text="")
    selected_answer = ""
    btn_submit.configure(state="normal")

    q = quiz_data[current_question]

    label_progress.configure(text=f"Question {current_question + 1} of {len(quiz_data)}")
    label_question.configure(text=q["question"])

    # clear old choice buttons
    for b in choice_buttons:
        b.destroy()
    choice_buttons.clear()

    # create a styled label-button for each choice (Labels respect bg/fg on macOS)
    for choice in q["choices"]:
        btn = tk.Label(frame_choices, text=choice, font=("Arial", 13),
                        bg=BUTTON_BG, fg=TEXT_COLOR,
                        relief=tk.RAISED, bd=2, cursor="hand2",
                        padx=10, pady=8, anchor="w")
        btn.pack(pady=3, padx=10, fill=tk.X)
        btn.bind("<Button-1>", lambda e, c=choice: select_choice(c))
        choice_buttons.append(btn)


def check_answer():
    """Validate selection, check answer, update score, advance question."""
    global current_question, score

    # input validation: make sure an answer is selected
    if selected_answer == "":
        messagebox.showwarning("No Selection", "Please select an answer before submitting.")
        return

    # disable submit to prevent double-clicking
    btn_submit.configure(state="disabled")

    # check if the answer is correct
    correct = quiz_data[current_question]["answer"]
    if selected_answer == correct:
        score += 1
        label_feedback.configure(text="Correct!", fg=CORRECT_COLOR)
        for b in choice_buttons:
            if b.cget("text") == correct:
                b.configure(bg=CORRECT_COLOR, fg=BG_COLOR, relief=tk.SUNKEN)
    else:
        label_feedback.configure(text=f"Incorrect! Answer: {correct}", fg=WRONG_COLOR)
        for b in choice_buttons:
            if b.cget("text") == selected_answer:
                b.configure(bg=WRONG_COLOR, fg=BG_COLOR, relief=tk.SUNKEN)
            if b.cget("text") == correct:
                b.configure(bg=CORRECT_COLOR, fg=BG_COLOR, relief=tk.SUNKEN)

    label_score.configure(text=f"Score: {score}/{current_question + 1}")

    current_question += 1
    if current_question < len(quiz_data):
        window.after(1500, load_question)
    else:
        window.after(1500, show_results)


def show_results():
    """Display the final score and percentage."""
    label_question.configure(text="")
    label_feedback.configure(text="")
    label_progress.configure(text="Quiz Complete!", fg=ACCENT_COLOR)
    for b in choice_buttons:
        b.destroy()
    choice_buttons.clear()
    btn_submit.pack_forget()

    percentage = round((score / len(quiz_data)) * 100)
    label_question.configure(text=f"You scored {score}/{len(quiz_data)}  ({percentage}%)",
                              font=("Arial", 20, "bold"), fg=ACCENT_COLOR)

    # restart button
    btn_restart = tk.Button(window, text="Restart Quiz", font=("Arial", 14, "bold"),
                             bg=ACCENT_COLOR, fg=BG_COLOR,
                             activebackground="#3d8ec9", activeforeground="white",
                             relief=tk.RAISED, bd=2, cursor="hand2",
                             command=restart_quiz)
    btn_restart.pack(pady=20)


def restart_quiz():
    """Reset everything and start over."""
    global current_question, score
    current_question = 0
    score = 0
    label_score.configure(text="Score: 0/0")
    label_question.configure(font=("Arial", 15), fg=TEXT_COLOR)
    label_progress.configure(fg="gray")

    for widget in window.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == "Restart Quiz":
            widget.destroy()
    btn_submit.pack(pady=15)

    load_question()


# start the quiz
load_question()

window.mainloop()


"""
Documentation

What does this program do?
    This is a GUI-based quiz application that tests how much the user
    knows about CAMS. It presents multiple-choice questions one at a
    time, checks answers, gives feedback, and displays a final score.

How does the user interact with it?
    The user reads each question, selects an answer by clicking a choice
    button, and clicks "Submit Answer." After the last question, the
    final score and percentage are shown with an option to restart.

Where is user input handled?
    User input is handled through choice buttons (selected_answer variable)
    and the "Submit Answer" button. Input validation occurs in check_answer(),
    which uses a messagebox warning if no answer is selected.

Where is program logic implemented?
    Program logic is in four functions:
    - load_question(): loads a question and its choices into the GUI
    - check_answer(): validates input, compares answer, updates score
    - show_results(): calculates and displays the final percentage
    - restart_quiz(): resets all variables and restarts from question 1
"""
