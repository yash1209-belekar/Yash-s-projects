package employee.management.system;
import javax.swing.*;
import java.awt.*;
import java.time.Duration;

public class splash extends JFrame {
    splash() {
        ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/employee information system.gif"));
        Image i2 = i1.getImage().getScaledInstance(1170,650,Image.SCALE_DEFAULT);
        ImageIcon i3 = new ImageIcon(i2);
        JLabel image = new JLabel(i3);
        image.setBounds(0,0,1170,650);
        add(image);


       setSize(1070,630);
        setLocation(200,70);
        setLayout(null);
        setVisible(true);

        try{
            Thread.sleep(5200);
            setVisible(false);
            new Login();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    public static void main(String[] args) {
        new splash();
    }
}
