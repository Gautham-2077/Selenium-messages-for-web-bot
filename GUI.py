import sys
from messages_bot import run_automation 
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox
from PyQt5 import QtGui

class DialogBox(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedHeight(200)
        self.setFixedWidth(500)
        self.setWindowIcon(QtGui.QIcon('bot.png'))
        
    def initUI(self):
        self.setWindowTitle("Message Bot")
        layout = QVBoxLayout()

        # Profile Text Area
        profile_label = QLabel("Profile:")
        self.profile_text = QLineEdit()
        layout.addWidget(profile_label)
        layout.addWidget(self.profile_text)

        # CSV File Button
        csv_label = QLabel("CSV File:")
        self.csv_button = QPushButton("Select File")
        self.csv_button.clicked.connect(self.select_csv_file)
        layout.addWidget(csv_label)
        layout.addWidget(self.csv_button)

        # Custom Function Button
        custom_button = QPushButton("Custom Function")
        custom_button.clicked.connect(self.custom_function)
        layout.addWidget(custom_button)

        self.setLayout(layout)

    def select_csv_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if filepath:
            self.csv_button.setText(filepath)
            print(filepath)

    def custom_function(self):
        profile_text = self.profile_text.text()
        csv_filepath = self.csv_button.text()

        print(profile_text, csv_filepath)
        
        # Check if all fields are filled
        if profile_text and csv_filepath:
            run_automation(csv_filepath, profile_text)
        else:
        # If any field is empty, show a message box informing the user
            QMessageBox.warning(self, "Incomplete Fields", "Please fill in all fields before running the custom function.")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = DialogBox()
    dialog.exec_()
