from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QGridLayout
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        # Set the title of the window
        self.setWindowTitle("Age Calculator")
        # Create QGridLayout instance
        grid = QGridLayout()

        # Create Widgets (Labels and buttons)
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        birth_date_label = QLabel("Date of Birth MM/DD/YYYY:")
        self.birth_date_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Create a Grid Layout
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(birth_date_label, 1, 0)
        grid.addWidget(self.birth_date_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        # Set the grid for the main window
        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.birth_date_line_edit.text()
        date_of_year = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - date_of_year
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")


# QApplication instance 'app' is created to manage the application.
app = QApplication(sys.argv)
# An instance of the AgeCalculator class named age_calculator is created.
age_calculator = AgeCalculator()
# Main window show
age_calculator.show()
# The application event loop is started with app.exec().
# The sys.exit() call ensures that the Python interpreter exits properly when the application is closed.
sys.exit(app.exec())
