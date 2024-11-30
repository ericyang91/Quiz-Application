class Quiz_item:
    """
    Models a multiple-choice question.

    This class represents a multiple-choice question, including its question description,
    multiple-choice options, and the correct answer. 
    It includes methods for modifying the question text, 
    updating the multiple-choice options, and changing the correct answer while ensuring 
    the validity of the choices.

    Attributes:
        question (str): The text description of the multiple-choice question.
        choices (list): A list containing possible answer options.
        answer (str): The correct answer selected from the choices.

    Methods:
        change_question(new_question): Changes the question to a new one.
        change_choices(new_choices): Replaces the current choices with a list of new choices.
        change_answer(new_answer): Updates the correct answer if it matches one of the choices.
        __str__(): Provides a string representation of the Quiz_item.
    """

    def __init__(self, question: str, choices: list, answer: str):
        """
        Initializes a new Quiz_item instance.

        Parameters:
            question (str): The multiple-choice question.
            choices (list): A list of possible answer choices.
            answer (str): The correct answer from the choices.

        Raises:
            ValueError: If the question is not in the form of a string,
                        or choices is not in the form of a list, 
                        or if answer is not one of the choices.
        """
        # Parameter validation
        if not isinstance(question, str): # Use `isinstance()` to ensure that question is a string
            raise ValueError('The question description must be a string.') # If not, raise ValueError
        if not isinstance(choices, list):  # Use `isinstance()` to ensure that choices are in a list
            raise ValueError('Choices must be in the form of a list.')  # If not, raise ValueError
        if answer not in choices:  # Ensure the answer matches one of the choices
            raise ValueError('Answer must match one of the provided choices.')  # If not, raise ValueError
        
        # Assign instance attributes to corresponding variables
        self.question = question
        self.choices = choices
        self.answer = answer

    def change_question(self, new_question: str):
        """
        Method that changes the question description to a new one.

        Parameters:
            new_question (str): The new question to set.
        
        Raises:
            ValueError: If the question is not in the form of a string.

        """
        # Parameter validation
        if not isinstance(new_question, str): # Use `isinstance()` to ensure that question is a string
            raise ValueError('The question description must be a string.') # If not, raise ValueError
        
        # Update and reassign the question attribute
        self.question = new_question

    def change_choices(self, new_choices: list):
        """
        Method that changes the choices to a new list of choices.

        Parameters:
            new_choices (list): A new list of possible answer choices.

        Raises:
            ValueError: If the choices is empty, or
                        if the choices is not in a list.
        """
        # Parameter validation
        if not new_choices: # Ensure `new_choices` is not empty
            raise ValueError('The choices cannot be empty.') # Raise ValueError if empty
        if not isinstance(new_choices, list): # Ensure `new_choices` is a list
            raise ValueError('Choices must be in a form of a list.') # Raise ValueError if not a list
        
        # Update and reassign the choices attribute
        self.choices = new_choices

    def change_answer(self, new_answer):
        """
        Method that changes the correct answer to a new one.

        Parameters:
            new_answer (of any type): The new correct answer.

        Raises:
            ValueError: If the new answer is not one of the choices.
        """
        # Check if the new answer is in the current choices
        if new_answer in self.choices:
            self.answer = new_answer  # Update the answer attribute
        else:
            raise ValueError('Answer must match one of the choices.') # Raise ValueError if not

    def __str__(self):
        """
        Method that returns a string representation of the Quiz_item.

        This method provides a formatted string that includes the question,
        multiple-choice options, and the correct answer.

        Returns:
            str: A formatted string representation of the Quiz_item.
        """
        # Format the choices by using `join` and `enumerate` to feed into one string
        choices_str = ""
        for index, choice in enumerate(self.choices, 1):
            choices_str += f'{index}: {choice}\n'
        
        return f"Question: {self.question}\nChoices:\n{choices_str}\nCorrect Answer: {self.answer}"