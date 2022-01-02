<h1>2.UoP-Java_Projects</h1>

<h3> a. The assignment will be assessed using the following criteria:

Does the submission include the file "SuperPower.java"?
Does the file include a public class called "SuperPower"?
Does the class include a public method called "main"?
Is the "main" method static?
Does the main method have a String assignment statement that uses "JOptionPane.showInputDialog"?
Does the main method have a statement that uses "JOptionPane.showMessageDialog"?
Does the program convert the String from "JOptionPane.showInputDialog" using the "toUpperCase" method?
Does the submission include a screenshot that shows an Input dialog that asks, "What is your superpower?"
Does the submission include a screenshot that shows a Message dialog stating "<power> TO THE RESCUE!", where "<power>" is the input converted to upper case?</h3>

<h3> b. Your assignment will be graded by your peers using the following criteria:

Does the submission include a file "QuestionDialog.java" with a class that extends "JDialog" and implements "ActionListener"?
Does the class "QuestionDialog" have a method "actionPerformed" that uses its "ActionEvent" parameter to set the instance variable "answer" and then calls the inherited "dispose" method?
Does the submission include a file "Question.java" with a constructor that initializes instance variable "question", gives it a single-column grid layout, and adds a text label using the constructor's String parameter?
Does class "Question" have a method "ask" that makes the instance variable "question" visible and returns the value "question.answer"?
Does class "Question" have a method "initQuestionDialog" that makes instance variable "question" modal, sets its size with "pack", and positions it in the center of the screen?
Does the class "TrueFalseQuestion" have a method "addButton" that constructs a button using its String parameter, adds the instance variable "question" as a listener for that button, and adds the button to its "JPanel" parameter?
Does the class "TrueFalseQuestion" have a constructor that calls its superclass constructor with its first String parameter, calls "addButton" to add "TRUE" and "FALSE" buttons to a panel, adds that panel to the instance variable "question", calls "initQuestionDialog", and initializes the instance variable "correctAnswer" with its second String parameter?
Does class "MultipleChoiceQuestion" have a method "addChoice" that creates a panel with a border layout, creates a button using its first String parameter, adds the instance variable "question" as a listener for that button, adds the button to the left side of the panel, adds a label to the center of the panel using its second String parameter, and adds the panel to the instance variable "question"?
Does the class "MultpleChoiceQuestion" have a constructor that calls its superclass constructor with its first parameter, calls "addChoice" using its next five parameters, calls "initQuestionDialog", and initializes the instance variable "correctAnswer" with its last parameter?</h3>
