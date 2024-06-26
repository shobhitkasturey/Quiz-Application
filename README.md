

---

# Quiz Application

This repository contains two versions of a quiz application: a console-based version and a graphical user interface (GUI) version using Tkinter. The application reads a list of questions and presents them to the user, keeping track of the score and providing feedback at the end.

## Features

- **Console Version:**
  - Presents questions in the console.
  - Accepts user input and checks answers.
  - Displays the final score at the end.

- **GUI Version:**
  - Presents questions in a graphical window.
  - Uses buttons for answer selection.
  - Displays the final score in a message box at the end.

## Requirements

- Python 3.x
- pandas (for the console version)
- Tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/quiz-application.git
    cd quiz-application
    ```

2. (Optional) Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install pandas if you want to run the console version:
    ```bash
    pip install pandas
    ```

## Console Version

### Usage

1. Ensure your questions are defined in the `questions` list within the script.
2. Run the script:
    ```bash
    python console_quiz.py
    ```

### How it Works

The console version of the quiz performs the following steps:
1. Initializes the quiz with a list of questions.
2. Displays each question and accepts user input.
3. Checks the user's answer and updates the score.
4. Displays the final score at the end of the quiz.

## GUI Version

### Usage

1. Ensure your questions are defined in the `questions` list within the script.
2. Run the script:
    ```bash
    python gui_quiz.py
    ```

### How it Works

The GUI version of the quiz performs the following steps:
1. Initializes the quiz window with a list of questions.
2. Displays each question with multiple-choice options.
3. Accepts user input through button clicks.
4. Checks the user's answer and updates the score.
5. Displays the final score in a message box at the end of the quiz.


```

### Contact

For any questions or suggestions, please contact:

Shobhit Kasturey  
Email: shobhitkasturey@gmail.com

