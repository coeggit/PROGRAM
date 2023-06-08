import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class FormImage {
    private JTextField textNomor;
    private JComboBox comboJenis;
    private JComboBox comboBank;
    private JTextField textNama;
    private JButton saveButton;
    private JButton browseImageButton;
    private JPanel rootP;
    private JTextArea textArea;
    private JLabel imageimage;
    public String selectedFile;

    public FormImage() {
        saveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                textArea.setText("");
                String nomor = textNomor.getText();
                String jenis = comboJenis.getSelectedItem().toString();
                String bank = comboBank.getSelectedItem().toString();
                String nama = textNama.getText();
                // String gambar = imageimage.getText();

                String result = String.format("Nomor kartu:"+nomor+" \nJenis ATM:"+jenis+" \nBank:"+bank+" \nNama Pemilik:"+nama+"\nGambar:"+selectedFile);

                textArea.append(result);
            }
        });

        browseImageButton.addActionListener(new ActionListener() { 
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser file = new JFileChooser();

                file.setCurrentDirectory(new File(System.getProperty("user.home")));
                FileNameExtensionFilter filter = new FileNameExtensionFilter("*.IMAGES", "jpg", "jpeg", "png");
                file.addChoosableFileFilter(filter);

                int result = file.showOpenDialog(null);
                if (result == JFileChooser.APPROVE_OPTION) {
                    selectedFile = file.getSelectedFile().getName();
                    String pathSrc = file.getSelectedFile().getAbsolutePath();
                    JOptionPane.showMessageDialog(null, pathSrc);

                    ImageIcon i = new ImageIcon(pathSrc);
                    Image x = i.getImage().getScaledInstance(imageimage.getWidth(), imageimage.getHeight(), Image.SCALE_DEFAULT);

                    imageimage.setIcon(new ImageIcon(x));
                    textArea.append(pathSrc);

                }
            }
        });

        
    }

    public JPanel getRootP() {
        return rootP;
    }
}


