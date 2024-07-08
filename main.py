# Import necessary classes from other modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Initialize an empty list to store Question objects
question_bank = []

# Iterate through each question in the question_data
for question in question_data:

    # Extract the question text from the current question dictionary
    question_text = question["question"]

    # Extract the correct answer from the current question dictionary
    question_answer = question["correct_answer"]

    # Create a new Question object with the extracted text and answer
    new_question = Question(question_text, question_answer)

    # Add the new Question object to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object, passing in the list of Question objects
quiz = QuizBrain(question_bank)

# Create a QuizInterface object, passing in the QuizBrain object
quiz_ui = QuizInterface(quiz)
