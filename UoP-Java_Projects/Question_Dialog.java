import java.awt.event.*;
import javax.swing.*;
import javax.swing.JOptionPane;
public class QuestionDialog extends JDialog implements ActionListener {
	String answer;
	public void actionPerformed(ActionEvent e) {
		answer = e.getActionCommand();
		dispose();
	}

}
