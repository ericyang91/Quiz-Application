class Quiz:
    """
    A class to represent a quiz, with functionalities for adding, displaying, 
    and executing quiz items. This class supports taking the quiz one question 
    at a time or executing the entire quiz. Each quiz item is expected to contain 
    a question, a list of multiple-choice options, and the correct answer.

    Attributes:
        quiz_name (str): The name of the quiz.
        quiz_items (list): A list to store quiz questions, each represented by 
                           a quiz_item object from class "Quiz_item" that includes question text, 
                           a list of answer choices, and the correct answer.

    Methods:
        add_quiz_items(quiz_item): Adds a new quiz item to the quiz.
        display_quiz_items(): Returns a formatted string displaying all questions,
                              choices, and answers in the quiz.
        execute_single_question(question_number, user_answer): Executes a single 
                              question and checks if the answer is correct.
        execute_entire_quiz(): Executes the entire quiz, prompting the user for answers 
                              to each question and calculating the score based on correct answers.
    """

    def __init__(self, quiz_name):
        """
        Initializes the Quiz object with a name and an empty list for quiz items.
        
        Parameters:
            quiz_name (str): The name of the quiz.
        """
        self.quiz_name = quiz_name
        self.quiz_items = []  # List to store quiz items (each item includes question, choices, answer)

    def add_quiz_items(self, quiz_item):
        """
        Adds a new quiz item to the quiz.
        
        Parameters:
            quiz_item (object): An object of class "Quiz_item" representing a quiz item. This object should
                                have 'question' (str), 'choices' (list), and 'answer' (str) attributes.
        """
        # Append the provided quiz item to the list of quiz items
        self.quiz_items.append(quiz_item)

    def display_quiz_items(self):
        """
        Returns a formatted string of all quiz questions, choices, and answers.

        Raises:
            ValueError: If there are no quiz items in the quiz.

        Returns:
            str: A string displaying each question with its choices and the correct answer.
                 Each question and its answer choices are formatted in a human-readable way.
        """
        if not self.quiz_items:
            raise ValueError('The quiz is empty.')
        else:
            result = []  # Initialize an empty list to accumulate formatted strings

            # Loop over quiz items and format each question with its choices and answer
            for i, item in enumerate(self.quiz_items, 1):
                result.append(f"Question {i}: {item.question}")  # Add question number and text

                # Enumerate choices for each question, prefixing each choice with an index
                for j, choice in enumerate(item.choices, 1):
                    result.append(f"     {j}: {choice}")

                # Include the answer at the end of the question block
                result.append(f"Answer: {item.answer}")
                result.append("")  # Add an empty line for spacing between questions
            
            # Join all elements in the result list into a single string separated by newlines
            return "\n".join(result)

    def execute_single_question(self, question_number, user_answer):
        """
        Executes a single question from the quiz and checks if the user's answer is correct.

        Parameters:
            question_number (int): The question number to execute.
            user_answer (str): The user's answer for the question.

        Raises:
            ValueError: If the question number is not in the range of available questions.

        Returns:
            str: 'Correct' if the answer is correct, 'Incorrect' otherwise.
        """
        # Check if question number is valid
        if question_number not in range(1, len(self.quiz_items) + 1):
            raise ValueError('Question does not exist.')
        
        # Retrieve the specific quiz item based on the question number
        quiz_object = self.quiz_items[question_number - 1]
        
        # Compare the user's answer to the correct answer (case-insensitive comparison)
        if quiz_object.answer.strip().lower() == user_answer.strip().lower():
            return 'Correct'
        else:
            return 'Incorrect'

    def execute_entire_quiz(self):
        """
        Executes the entire quiz by prompting the user for each question and calculating the score.

        This method iterates over all quiz items, displays each question and its choices, and prompts 
        the user to enter an answer. It keeps track of incorrect answers and provides a score summary at the end.

        Raises:
            ValueError: If there are no quiz items to execute.

        Returns:
            str: A summary of the quiz results, including:
                - The percentage score based on correct answers
                - Details of any questions that were answered incorrectly
        """
        if not self.quiz_items:
            raise ValueError('Empty quiz. Add quiz items first.')
        
        wrong_questions = []  # List to store incorrectly answered questions

        # Iterate through each question in the quiz
        for i, item in enumerate(self.quiz_items, 1):
            # Format the question and its choices for display
            result = [f"Question {i}: {item.question}"]
            for j, choice in enumerate(item.choices, 1):
                result.append(f"     {j}: {choice}")

            # Display question and choices
            display = "\n".join(result)
            
            # Prompt the user to input an answer for the current question
            user_answer = input(display)
            
            # If user's answer is incorrect, add it to the wrong_questions list
            if user_answer.strip().lower() != item.answer.strip().lower():
                print('Incorrect')
                wrong_questions.append((item.question, item.answer, user_answer))
            else:
                print('Correct')

        # Calculate score percentage by the ratio of correct answers
        score = round((1 - len(wrong_questions) / len(self.quiz_items)) * 100, 2)

        # Prepare a summary of the quiz results
        quiz_result = f"You scored {score}% on the quiz!\n"
        quiz_result += f"You answered the following questions incorrectly:\n"

        # Detail the incorrect questions in the result summary
        for question, correct_answer, user_answer in wrong_questions:
            quiz_result += f"Question: {question}\nCorrect Answer: {correct_answer}\nYour Answer: {user_answer}\n"

        return quiz_result
