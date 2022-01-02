import java.awt.*;
import javax.swing.*;
public abstract class Question {
	 static int xQuestions = 0;     
	 static int xCorrect = 0;     
	 QuestionDialog question;     
	 String correctAnswer;
	 Question(String question){
		 this.question = new QuestionDialog();
		 this.question.setLayout(new GridLayout(0,1));
		 this.question.add(new JLabel(" "+question+" ",JLabel.CENTER));
	 }
	 String ask() {
	 question.setVisible(true);
	 return question.answer;
	 }
	 void check() {         
		 xQuestions++;         
		 String answer = ask();         
		 if (answer.equals(correctAnswer)) {             
			 JOptionPane.showMessageDialog(null,"Correct!");             
			 xCorrect++;         
			 } 
		 else {             
			 JOptionPane.showMessageDialog(null,"Incorrect. The correct answer is "+correctAnswer+".");         
			 }     
		 } 
	 void initQuestionDialog() {
		 this.question.setModal(true);
		 this.question.pack();
		 this .question.setLocationRelativeTo(null);
	 }
	 static void showResults() {         
		 JOptionPane.showMessageDialog(null,xCorrect+" correct out of "+xQuestions+" questions");     
		 } 
	 }
