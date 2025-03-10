import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLineEdit, QRadioButton, QComboBox, QGroupBox, QSpacerItem, QSizePolicy, QFormLayout)
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        main_layout = QVBoxLayout()

        # Identitas
        identitas_group = QGroupBox("Identitas (vertical box layout)")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama : nama_anda"))
        identitas_layout.addWidget(QLabel("Nim : nim_anda"))
        identitas_layout.addWidget(QLabel("Kelas : kelas_anda"))
        identitas_group.setLayout(identitas_layout)
        main_layout.addWidget(identitas_group)
        
        # Navigation Buttons
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)

        # Centered Form User Registration
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()

        full_name = QLineEdit()
        email = QLineEdit()
        phone = QLineEdit()
        gender_male = QRadioButton("Male")
        gender_female = QRadioButton("Female")
        country_box = QComboBox()
        country_box.addItems(["Select", "USA", "UK", "Canada", "Australia"])

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(gender_male)
        gender_layout.addWidget(gender_female)

        form_layout.addRow("Full Name:", full_name)
        form_layout.addRow("Email:", email)
        form_layout.addRow("Phone:", phone)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", country_box)
        
        form_group.setLayout(form_layout)
        form_group.setFixedWidth(300)  # Menyesuaikan lebar formulir
        
        # Spacer untuk memusatkan form dalam border penuh
        center_layout = QVBoxLayout()
        center_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        center_layout.addWidget(form_group, alignment=Qt.AlignCenter)
        center_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addLayout(center_layout)

        # Actions Buttons
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton("Submit"))
        action_layout.addWidget(QPushButton("Cancel"))
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)
        self.setWindowTitle("User Registration Form")
        self.setGeometry(100, 100, 400, 500)  # Menyesuaikan ukuran border penuh

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.show()
    sys.exit(app.exec_())