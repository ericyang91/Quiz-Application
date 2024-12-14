## Documentation

### **Interpretation of the project**

This project involves creating a GUI-based quiz application that allows users to design quizzes by adding questions, multiple-choice options, and correct answers. Users can then select quizzes from a list they’ve created and attempt them. Additional features include previewing quizzes and adding new items to existing ones. During the quiz, users must answer all questions within a given time limit, and their performance is evaluated with a score displayed at the end.

Several key considerations shaped the development process.

**Class Interactions:** The application relies on three main classes:

`Quiz_item`: Defines the details of an individual quiz question, including its description, multiple-choice options, and correct answer.  
`Quiz`: Represents a complete quiz consisting of multiple QuizItem instances.  
`MainApp`: Manages the overall application, including its functionalities and user interface.  

Planning the interaction between these classes was critical to ensure a modular and maintainable structure.

**Application Flow:** Careful planning was required to design the user journey. For example, determining where button clicks would take users and how they could navigate back to the main page was essential to provide a seamless experience.

**Instance Attributes:** Instance attributes played a vital role in maintaining the state across different parts of the application. They eliminated the need to explicitly pass variables between functions, simplifying the code and improving readability.

**Understanding Tkinter:** Mastery of the Tkinter module was crucial as it forms the foundation of the application's GUI. Leveraging Tkinter’s widgets and layout management tools ensured the interface was functional and user-friendly.

Future improvements to this application include adding features for deleting quizzes, as well as implementing save and load functionalities to enhance usability and persistence.

---

### **An analysis of the tasks and requirements, techniques, and/or algorithms you used to solve the problems or accomplish the tasks.**

**Analysis of the Tasks, Requirements, and Techniques:**  

This project requires a strong grasp of object-oriented programming (OOP) in Python to effectively define and organize classes, such as Quiz, Quiz_item, and MainApp, and to manage the interactions between them. Proficiency with the Tkinter module is essential for creating the graphical user interface (GUI). The project also involves event-driven programming, where the program's flow is controlled by events like user interactions (e.g., button clicks). Additionally, managing a countdown timer, updating the UI in real-time, and handling timeouts when the timer expires are key tasks. I also needed to set up attributes to store information such as the current Quiz object, correctly answered questions, and incorrectly answered questions, and ensure these are cleared when needed for future actions. Error handling and input validation are vital for providing a smooth user experience, along with implementing clear navigation options for starting, reattempting, and exiting the quiz. Widgets such as Label, Button, Entry, and Listbox were utilized to build the interface, while data structures like lists, tuples, dictionaries, and sets were employed to store various types of data. To address dynamic changes in the program, I developed a method to clear all widgets and reset widget references to None, as issues arose when attempting to access destroyed widgets. Instance attributes were used to streamline the flow of data between functions, eliminating the need to pass multiple arguments across functions.

**Algorithm for `Quiz_item`:**
```
1. Create the Quiz_item Class:
    - Define a constructor to initialize an instance with the following attributes:
        1. question: The text of the quiz question.
        2. choices: A list of multiple-choice options.
        3. answer: The correct answer selected from the choices.
    - Perform validation during initialization:
        1. Ensure the question is a non-empty string. If not, raise an error.
        2. Ensure the choices are a non-empty list. If not, raise an error.
        3. Ensure the answer is one of the choices. If not, raise an error.

2. Define a Method to Change the Question:
    - Accept a new question as input.
    - Validate that the new question is a non-empty string.
    - Update the question attribute with the new value.

3. Define a Method to Change the Choices:
    - Accept a new list of choices as input.
    - Validate that the new list is non-empty and contains at least one option.
    - Update the choices attribute with the new list.

4. Define a Method to Change the Answer:
    - Accept a new answer as input.
    - Validate that the new answer exists in the current list of choices.
    - Update the answer attribute with the new value.

5. Define a Method to Return String Representation of the Quiz Item:
    - Return a formatted string representation of the quiz item.
    - Include:
        1. The question text.
        2. The choices, each prefixed by its index.
        3. The correct answer.
```
**Algorithm for `Quiz`:**
```
1. Create the Quiz Class:
    - Define a constructor to initialize an instance with the following attributes:
        1. quiz_name: Accepts quiz_name as input to initialize a Quiz instance.
        2. quiz_items: An empty list to hold Quiz_item objects, each representing a question, its choices, and the correct answer.

2. Define a Method to Add Quiz Items
    - Takes a Quiz_item object as a parameter.
    - Appends the given Quiz_item object to the quiz_items list.

3. Define a Method to Display Quiz Items
    - Iterates through quiz_items and formats each question, its choices, and the correct answer for display.
    - Raises a ValueError if quiz_items is empty.
    - Returns a formatted string with all questions, choices, and their correct answers.

4. Define a Method to Execute a Single Question
    - Takes the question number and a user-provided answer as inputs.
    - Validates the question number against the list of available quiz items.
    - Compares the user's answer with the correct answer for the specified question.
    - Raises a ValueError if the question number is invalid.
    - Returns 'Correct' if the answer matches; otherwise, 'Incorrect'.

5. Define a Method to Execute the Entire Quiz
    - Iterates through all quiz_items.
    - Displays each question and its choices to the user, prompting for an answer.
    - Tracks incorrectly answered questions.
    - Raises a ValueError if quiz_items is empty.
    - Calculates the score as a percentage of correct answers.
    - Returns a summary of the user's performance, including the final score as a percentage, a list of incorrectly answered questions with the correct answers and the user's responses.
```
**Algorithm for `MainApp`:**
```
1. Create and initiate the MainApp Class:
    - Define the MainApp class to manage the GUI-based quiz application.
    - Initialize the following attributes in the constructor:
        1. root: The Tkinter root window reference, with a title and geometry set.
        2. quizzes: A dictionary to store quiz objects by their names.
        3. current_quiz: Placeholder for the currently selected quiz object.
        4. correct_quiz_item_numbers and incorrect_quiz_item_numbers: Dictionaries to track the indexes and user responses for correct and incorrect quiz items.
    - Initiate the main menu screen the end of the constructor when the application starts.

2. Define the Method that Sets up the Main Menu:
    - Clears the window of any existing widgets.
    - Creates and displays widgets for the main menu:
        1. A title label.
        2. Buttons for "Create Quiz" or "Select Quiz".
        3. A label for creator information.
    - Checks for existing widgets to avoid redundant creation.

3. Define the Method that Holds the Screen for Quiz Name Creation:
    - Clears the window and sets up an interface for entering a quiz name when "Select Quiz" is clicked.
    - Displays:
        1. A label prompting the user to enter a quiz name.
        2. An entry field to capture the name.
        3. Buttons to "Create" or return to the "Main Menu".
    - Validates and processes the entered quiz name.

4. Define the Method that Verifies the Quiz Name Created:
    - Validates the user-input quiz name:
        1. Ensures the quiz name is not empty.
        2. Ensures the quiz name is unique and does not already exist in the quiz collection.
    - Displays error messages if the name is invalid or a success message if the quiz is created successfully.
    - Creates a new Quiz instance and stores it in the quizzes dictionary.
    - Sets the newly created quiz as the current quiz and proceeds to the next step in quiz creation.

5. Define the Method that Adds Quiz Details:
    - Clears the window of any existing widgets to prepare for the quiz details interface.
    - Initializes variables to store input data from entry fields for the question, choices, and correct answer.
    - Creates and displays the labels and entry fields for entering quiz details such as:
        1. Question description.
        2. Multiple-choice options (choices 1 to 4).
        3. Correct answer.
    - Displays buttons for saving the quiz item (Save Item), adding more questions (Clear to Add More), or returning to the main menu (Main Menu).
    - Ensures that each widget is only created once by checking for existing widgets and referencing them if already created.

6. Define the Method to Validate User-Input Quiz Details:
    - Validates the user-input quiz details by checking for any empty inputs, the uniqueness of each choice, and that the answer matches one of the choices.
    - Initializes a Quiz_item instance using the valid inputs and saves this to the current Quiz object.
    - Uses pop-up message boxes to alert the user of any invalid inputs or let them know that the Quiz was successfully created.

7. Define the Method that Allows Addition of Quiz Items:
    - Activated when "Clear to Add More" is clicked.
    - Clears the current user interface widgets.
    - Resets the quiz details entry form to allow the user to add another question.

8. Define the Method that Selects an Existing Quiz for Further Action:
    - Clears the window of any existing widgets.
    - Displays the quiz selection interface:
        1. A title label prompting the user to select a quiz.
        2. A listbox showing the available quizzes from self.quizzes.
        3. A "Select" button to confirm the selection.
        4. A "Main Menu" button to return to the main menu.
    - Checks for existing widgets to avoid redundant creation.

9. Define the Method that Verifies Quiz Selection:
    - Retrieves the selected quiz index from the listbox.
    - Verifies that a quiz is selected:
        1. If no quiz is selected, it shows an error message.
        2. If a quiz is selected, it retrieves the quiz name from the listbox and assigns the corresponding quiz object to self.current_quiz.

10. Define the Method that Sets Up the Selection Menu
    - Clears the window of any existing widgets.
    - Creates and displays widgets for the selection menu:
        1. A title label.
        2. Buttons for "Add Quiz Items", "Preview Quiz", "Take Quiz", "Main Menu".
    - Checks for existing widgets to avoid redundant creation. 

11. Define the Method that Allows Users to Preview the Selected Quiz:
    - Activated when "Preview Quiz" is selected.
    - Clears the window of any existing widgets.
    - Creates a scrollable content that includes the selected quiz's question description, the multiple-choice options, and the correct answer.
    - Displays buttons "Selection Menu" and "Main Menu" for navigation.

12. Define the Method that Sets Up the Quiz Interface
    - Activated when "Take Quiz" is selected.
    - Clears the window of any existing widgets.
    - Sets up the quiz interface for the specified quiz, initializing the display for questions, answer choices, timer, label to indicate the number of questions remaining, and user input fields.
    - Loads the quiz questions.

13. Define the Method that Loads a Quiz Question:
    - Retrieves the current quiz question.
    - Updates the label widgets to display the number of remainig questions, the current question number, and its description.
    - Loops through the label widgets to update each with the corresponding answer choices.
    - Captures the user's answer and triggers a method that processes this answer.

14. Define the Method that Processes User Answer:
    - Validates the user's answer and updates the feedback label to show whether the answer was "Correct" or "Incorrect"
    - Keeps track of the correct and incorrect answers.
    - Loads the next question.

15. Define the Method that determines whether or not to load the next question:
    - Increments the item number to move to the next question in the quiz.
    - Checks if there are more questions remaining.
    - If all questions are answered, calls method that shows the quiz results.
    - If there are more questions, call method that loads a quiz question.

16. Define the Method that Runs the Timer:
    - Checks if remaining_time is greater than zero.
        - If remaining_time > 0, updates the timer label to show the remaining time.
        - Decreases remaining_time by 1 second.
    - If remaining time is 0:
        - Updates the timer label to display "Time's up!".
        - Shows a pop-up alert notifying the user that the time is up.
    - Displays the quiz results.

17. Define the Method that Displays Quiz Result:
    - Upon exhausting all quiz items, cancels the countdown timer if it is active.
    - Clears the window of any existing widgets.
    - Displays the quiz title, the score in percentage, and any incorrect answers and the corresponding questions and their correct answers.
    - Display any unanswered questions along with their correct answers.

18. Define the Method that Clears Widgets and Resets Widget References:
    - Iterates through each child widget and destroys them.
    - Resets references to dynamically created widgets to ensure they can be reinitialized.
```
### An explanation of modules, classes, and functions you wrote and/or used in the system developed for the project

1. **Modules**
    - *tkinter*: Python's standard GUI toolkit. I used tkinter to build the main interface of the program. Widgets such as Button, Label, Entry, Listbox were used to build the graphical user-interactive program. They also allowed for the event-driven component of the program.   

2. **Classes**
    - *Quiz_item*: This class models a multiple-choice question. It represents a multiple-choice question, including its question description, multiple-choice options, and the correct answer. It includes methods for modifying the question text, updating the multiple-choice options, and changing the correct answer while ensuring the validity of the choices.
    - *Quiz*: This class represents a quiz, with functionalities for adding, displaying, and executing quiz items. This class supports taking the quiz one question at a time or executing the entire quiz. Each quiz item is expected to contain a question, a list of multiple-choice options, and the correct answer.
    - *MainApp*: Main application class for the Quiz Application. This class is responsible for managing the different stages of the quiz application, including displaying the main menu, creating quizzes, selecting quizzes, taking quizzes, and displaying results. The application provides a user-friendly interface for interacting with quizzes, allowing users to create, select, preview, and take quizzes. After completing a quiz, users are shown their score and a list of incorrect or unanswered questions.


3. **Functions and methods in Quiz_item**
    - change_question(new_question): Changes the question to a new one.
    - change_choices(new_choices): Replaces the current choices with a list of new choices.
    - change_answer(new_answer): Updates the correct answer if it matches one of the choices.
    - \_\_str\_\_(): Provides a string representation of the Quiz_item.

4. **Functions and methods in Quiz**
    - add_quiz_items(quiz_item): Adds a new quiz item to the quiz.
    - display_quiz_items(): Returns a formatted string displaying all questions, choices, and answers in the quiz.
    - execute_single_question(question_number, user_answer): Executes a single question and checks if the answer is correct.
    - execute_entire_quiz(): Executes the entire quiz, prompting the user for answers to each question and calculating the score based on correct answers.

5. **Functions and methods in MainApp**
    - \_\_ini\_\_(self, root): Initializes the application and the main window.
    - main_menu(self): Displays the main menu with options to create, select, or take a quiz.
    - create_quiz_name(self): Allows the user to enter a quiz name and proceed to quiz creation.
    - quiz_name_verification(self, quiz_name): Verifies the quiz name for validity before creating the quiz.
    - create_quiz_details(self): Sets up the interface for entering quiz question details.
    - quiz_details_verification(self): Verifies and saves the question details for a quiz item.
    - add_more(self): Allows the user to add more questions to a quiz.
    - select_quiz(self): Displays the interface for selecting an existing quiz.
    - selection_verification(self): Verifies the user's quiz selection and proceeds to the next screen.
    - selection_menu(self): Displays options such as adding quiz items, previewing, or taking the quiz.
    - preview_quiz(self): Shows a preview of the selected quiz before taking it.
    - quiz_setup(self): Prepares the quiz interface with questions, choices, and answer validation.
    - load_question(self): Loads and displays the current quiz question with answer choices.
    - process_answer(self, user_answer): Processes the answer, provides feedback, and loads the next question.
    - load_next_question(self): Loads the next question or displays results if all questions are answered.
    - countdown(self, remaining_time, total_time): Handles the countdown timer for the quiz.
    - display_results(self): Displays the quiz results, including score, incorrect answers, and unanswered questions.


### **USER GUIDE**

Welcome! Thank you for using the Quiz Application!   
We have prepared this guide to walk you through the features and usage of this quiz application.   

1. **Starting the App**   
Upon launching this application, you will be presented with two options in the Main Menu:  
The `Create Quiz` button will allow you to create a quiz that you can tackle later.  
The `Select Quiz` button will give you a list of quizzes that you can select from.  

2. **Creating a Quiz**  
Upon clicking the `Create Quiz` button, you will be directed to an interface that allows you to name the new quiz.  
Make sure to choose a name that does not already exist!  
You will also be presented with a page that prompts you to enter quiz details such as the question description, the multiple-choice options, and the correct answer.  
You should not leave any fields blank! Also, make sure that the multiple-choice options do not overlap, and that the answer matches one of the choices.  
If you are satisfied with the details, you can click `Save Item` to add the question to the quiz. To add more items, click the `Clear to Add More` button, which will clear all fields to allow you to create a new item. However, make sure you click `Save Item` before clicking `Clear to Add More` to save your work!  

3. **Selecting a Quiz**  
Once you have created your quizzes, you can select one to play!   
In the Main Menu, click `Select Quiz`. This will present you with a list box that contains the names of the quizzes you have created. You can click one and click the `Select` button. This button will take you to a page that contains different options that you can explore with the selected quiz.  

4. **Adding Items to the Quiz**  
One of these options allows you to add more questions to the selected quiz. Simply click `Add Quiz Items` to add more items to the quiz.  

5. **Previewing the Quiz**  
You also have the option to preview the selected quiz. You can click `Preview Quiz` to view the list of quizzes with their question description, the multiple-choice options, and the correct answers.  

6. **Taking the Quiz**  
Once the quiz is selected, you can click `Take Quiz` to start the quiz!  
The timer will start counting down from the specified time. The time limit will depend on the length of the quiz.
Answer each question by typing your answer in the provided input field. Make sure to type in the actual answers and not the option numbers!  
After submitting your answer for each question, feedback will be shown indicating whether your answer was correct or incorrect.  
The quiz will continue until all questions have been answered or the time runs out.  

7. **Time Limit**  
You are given a set amount of time to complete the quiz. The total time and the remaining time is displayed at the top of the quiz interface, along with the total number of questions in the quiz and the number of questions remaining.  
If the timer runs out, a "Time's up!" message will appear, and you will be brought to a page where your score is shown.  

8. **Viewing Results**  
After the quiz ends, either due to the timer running out or all questions being answered, the results will be displayed.  
Your score (percentage of correct answers) will be shown.  
A list of incorrect answers (with your response and the correct answer) will be shown in a scrollable section.  
Any unanswered questions will also be listed with the correct answer.  
You can return to the main menu by clicking the "Main Menu" button.  

9. **Returning to the Main Menu**  
At any time, you can return to the main menu by selecting the "Main Menu" button, which will clear the current quiz interface and allow you to select a different quiz.  

10. **System Requirements**  
This application requires a Tkinter-compatible Python environment to run.  
Good luck and have fun!
