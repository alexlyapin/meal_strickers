import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QPushButton,
    QFileDialog,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label Generator")

        # Create the main widget and layout
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        # Create the file selection control
        file_button = QPushButton("Select Excel Document")
        file_button.clicked.connect(self.select_file)
        layout.addWidget(file_button)

        # Create the combo box to select a sheet
        sheet_combo = QComboBox()
        layout.addWidget(sheet_combo)

        # Create the button to generate the final document
        generate_button = QPushButton("Generate Final Document")
        layout.addWidget(generate_button)

        # Set the main widget and layout
        self.setCentralWidget(main_widget)

    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.exec()
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            file_path = selected_files[0]
            # TODO: Handle the selected file path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
