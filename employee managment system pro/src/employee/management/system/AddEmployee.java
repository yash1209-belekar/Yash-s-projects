package employee.management.system;

import javax.swing.*;
import java.awt.*;

public class AddEmployee extends JFrame {

    JTextField tname,tfname,taddress,tpone,taadhhar,temail,tsalary,tdesignation;
    JButton b1,b2,b3,b4;

    AddEmployee(){
        getContentPane().setBackground(new Color(163, 255, 188));

        JLabel heading = new JLabel("Add Employee Detail");
        heading.setBounds(320,30,500,50);
        heading.setFont(new Font("Times New Roman",Font.BOLD,25));
        add(heading);




        setSize(900,700);
        setLayout(null);
        setLocation(300,50);
        setVisible(true);


    }
    public static void main(String[] args) {
        new AddEmployee();
    }
}
