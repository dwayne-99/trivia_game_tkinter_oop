import html  # Import the html module for unescaping HTML entities

class QuizBrain:
    def __init__(self, q_list):
        # Initialize the QuizBrain with a list of questions
        self.question_number = 0  # Track the current question number
        self.score = 0  # Keep track of the user's score
        self.question_list = q_list  # Store the list of questions
        self.current_question = None  # Store the current question object

    def still_has_questions(self):
        # Check if there are more questions to ask
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the next question and prepare it for display
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1  # Increment the question number
        q_text = html.unescape(self.current_question.text)  # Unescape HTML entities in the question text
        return f"Q.{self.question_number}: {q_text}"  # Return formatted question string

    def check_answer(self, user_answer):
        # Check if the user's answer is correct
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increment score if correct
            return True
        else:
            return False
