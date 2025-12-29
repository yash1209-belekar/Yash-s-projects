package employee.management.system;

import javax.swing.*;
import java.awt.*;
import java.awt.Color.*;
import java.awt.Font.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Login  extends JFrame implements ActionListener {

    JTextField tusername;

    JPasswordField tpassword;

    JButton login, Exit;




    Login() {

        JLabel username = new JLabel("Username");
        username.setBounds(180,170,100,30);
        add(username);
        setForeground(Color.white);
        tusername = new JTextField();
        tusername.setBounds(290,170,150,30);
        add(tusername);

        JLabel password = new JLabel("Password");
        password.setBounds(180,220,100,30);
        add(password);

        tpassword = new JPasswordField();
        tpassword.setBounds(290,220,150,30);
        add(tpassword);

        login = new JButton("LOGIN");
        login.setBounds(190,390,250,40);
        login.setBackground(Color.black);
        login.setForeground(Color.white);
        login.addActionListener(this);
        add(login);

        Exit = new JButton("EXIT");
        Exit.setBounds(450,390,250,40);
        Exit.setBackground(Color.black);
        Exit.setForeground(Color.white);
        Exit.addActionListener(this);
        add(Exit);

        ImageIcon i11 = new ImageIcon(ClassLoader.getSystemResource("icons/48.gif"));
        Image i22 =i11.getImage().getScaledInstance(190,220,Image.SCALE_FAST);
        ImageIcon i33 = new ImageIcon(i22);
        JLabel imgg = new JLabel(i33);
        imgg.setBounds(510,130,170,200);
        add(imgg);

        ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/45.png"));
        Image i2 =i1.getImage().getScaledInstance(900,600,Image.SCALE_FAST);
        ImageIcon i3 = new ImageIcon(i2);
        JLabel img = new JLabel(i3);
        img.setBounds(0,0,900,600);
        add(img);


        setSize(900,600);
        setLocation(300,70);
        setLayout(null);
        setVisible(true);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource()==login){
            try {
                String username = tusername.getText();
                String password = tpassword.getText();

                connection conn =new connection();

                String query = "select * from login where username = '"+ username +"' and password = '"+ password +"'";
                ResultSet resultSet = conn.statement.executeQuery(query);
                if (resultSet.next()) {
                    setVisible(false);
                    new Main_class();

                }else  {
                    JOptionPane.showMessageDialog(null,"Incorrect username or password");
                }

            }catch(Exception E) {}

        }else if (e.getSource()==Exit){
            System.exit(69696);
        }

    }

    public static void main(String[] args) {
        new Login();
    }



}
