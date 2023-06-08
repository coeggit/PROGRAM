import javax.swing.*;

public class RunFormImage {
    public static void main(String[] args) {
        JFrame jFrame = new JFrame("Form Image");
        jFrame.setContentPane(new FormImage().getRootP());
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jFrame.setLocationRelativeTo(null);
        jFrame.setSize(400,400);
        jFrame.setVisible(true);
    }
}
