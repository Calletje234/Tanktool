from PyQt5.QtWidgets import *


class RadioButton(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Create Radio Buttons
        self.euro = QRadioButton("Euro 95")
        self.diesel = QRadioButton("Diesel")
        self.lpg = QRadioButton("LPG")
        self.super = QRadioButton("Super")

        # Set Initial state
        self.euro.setChecked(True)
        self.euro_checked = 1
        self.diesel_checked = 0
        self.lpg_checked = 0
        self.super_checked = 0

        # Create Radio Button Layout
        self.radioLayout = QGridLayout()

        # Set Buttons Functions
        self.euro.toggled.connect(lambda: self.euro_radio_button())
        self.diesel.toggled.connect(lambda: self.diesel_radio_button())
        self.lpg.toggled.connect(lambda: self.lpg_radio_button())
        self.super.toggled.connect(lambda: self.super_radio_button())

        # Add Buttons to Layout
        self.radioLayout.addWidget(self.euro, 0, 0)
        self.radioLayout.addWidget(self.diesel, 0, 1)
        self.radioLayout.addWidget(self.lpg, 0, 2)
        self.radioLayout.addWidget(self.super, 0, 3)

    def euro_radio_button(self):
        if self.euro_checked == 1:
            self.euro.setChecked(False)
            self.euro_checked = 0
            self.diesel.setChecked(False)
            self.diesel_checked = 0
            self.lpg.setChecked(False)
            self.lpg_checked = 0
            self.super.setChecked(False)
            self.super_checked = 0

        elif self.euro_checked == 0:
            self.euro.setChecked(True)
            self.euro_checked = 1
            self.diesel.setChecked(False)
            self.diesel_checked = 0
            self.lpg.setChecked(False)
            self.lpg_checked = 0
            self.super.setChecked(False)
            self.super_checked = 0

    def diesel_radio_button(self):
        if self.diesel_checked == 1:
            self.euro.setChecked(False)
            self.euro_checked = 0
            self.diesel.setChecked(False)
            self.diesel_checked = 0
            self.lpg.setChecked(False)
            self.lpg_checked = 0
            self.super.setChecked(False)
            self.super_checked = 0

        elif self.diesel_checked == 0:
            self.euro.setChecked(False)
            self.euro_checked = 0
            self.diesel.setChecked(True)
            self.diesel_checked = 1
            self.lpg.setChecked(False)
            self.lpg_checked = 0
            self.super.setChecked(False)
            self.super_checked = 0

    def lpg_radio_button(self):
        if self.lpg_checked == 1:
            self.euro.setChecked(False)
            self.euro_checked = 0
            self.diesel.setChecked(False)
            self.diesel_checked = 0
            self.lpg.setChecked(False)
            self.lpg_checked = 0
            self.super.setChecked(False)
            self.super_checked = 0

        elif self.lpg_checked == 0:
            self.euro.setChecked(False)
            self.euro_checked = 0
            self.diesel.setChecked(False)
            self.diesel_checked = 0
            self.lpg.setChecked(True)
            self.lpg_checked = 1
            self.super.setChecked(False)
            self.super_checked = 0

    def super_radio_button(self):
        if self.super_checked == 1:
            self.euro.setChecked(False)
            self.euro_checked = 0
            self.diesel.setChecked(False)
            self.diesel_checked = 0
            self.lpg.setChecked(False)
            self.lpg_checked = 0
            self.super.setChecked(False)
            self.super_checked = 0

        elif self.super_checked == 0:
            self.euro.setChecked(False)
            self.euro_checked = 0
            self.diesel.setChecked(False)
            self.diesel_checked = 0
            self.lpg.setChecked(False)
            self.lpg_checked = 0
            self.super.setChecked(True)
            self.super_checked = 1

    def return_radio_buttons(self):
        return self.radioLayout

    def return_selected_buttons(self):
        if self.euro_checked == 1:
            return "Euro 95"
        elif self.diesel_checked == 1:
            return "Diesel"
        elif self.lpg_checked == 1:
            return "LPG"
        elif self.super_checked == 1:
            return "Super"
