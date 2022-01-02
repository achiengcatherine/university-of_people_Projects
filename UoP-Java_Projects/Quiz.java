import javax.swing.JOptionPane;
public class Quiz {
	public static void main(String[] args) {
		Question question = new TrueFalseQuestion("riding is Enjoyable!","Y");
			    question.check();
			    
		        question = new TrueFalseQuestion("square of 2 is 6?","n");
	
		        question.check();
		        question = new TrueFalseQuestion("which one is not true?","false");
		    	
		        question.check();
						
		MultipeChoiceQuestion question2 = new MultipeChoiceQuestion(
				"Which subjects did you score high grage?",
				"Mathematics,English,History",
				"Physics,Chemistry,Kiswahili",
				"Biology",
				"Business",
				"None",
				"A"); //correct answer
		question2.check();
		MultipeChoiceQuestion question3 = new MultipeChoiceQuestion(
				"How many subjects do you take?",
				"Seven",
				"Nine",
				"Six",
				"Eight",
				"Ten",
				"D"); //correct answer
		question3.check();
		MultipeChoiceQuestion question4 = new MultipeChoiceQuestion(
				"How many marks did you score?",
				"300",
				"250",
				"450",
				"350",
				"400",
				"C"); //correct answer
		question4.check();
		MultipeChoiceQuestion question5 = new MultipeChoiceQuestion(
				"How many students are you in total?",
				"100",
				"130",
				"85",
				"74",
				"150",
				"E"); //correct answer
		question5.check();
		MultipeChoiceQuestion.showResults();
				
	}
}
