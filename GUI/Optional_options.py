from PyQt5.QtWidgets import *


class OptionalOptions(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.options_layout = QGridLayout()

        # Create Edit Fields and Set Standard Text
        self.km_per_liter = QLineEdit()
        self.tank_amount = QLineEdit()
        self.max_distance = QLineEdit()
        self.km_per_liter.setPlaceholderText("10")
        self.tank_amount.setPlaceholderText("30")
        self.max_distance.setPlaceholderText("10")

        # Create Labels
        self.km_liter_label = QLabel("Verbruik van de Auto, '1 op: '")
        self.tank_label = QLabel("Hoeveelheid te tanken: ")
        self.distance_label = QLabel("Maximale afstand te rijden: ")

        self.add_items_to_frame()

    def add_items_to_frame(self):
        self.options_layout.addWidget(self.km_liter_label,0,0)
        self.options_layout.addWidget(self.km_per_liter,0,1)
        self.options_layout.addWidget(self.tank_label,1,0)
        self.options_layout.addWidget(self.tank_amount,1,1)
        self.options_layout.addWidget(self.distance_label,2,0)
        self.options_layout.addWidget(self.max_distance,2,1)

    def return_optional_options_layout(self):
        return self.options_layout

    def return_car_usage(self):
        if self.km_per_liter.text() == "":
            return "10"
        else:
            return self.km_per_liter.text()

    def return_amount_tank_fill(self):
        if self.tank_amount.text() == "":
            return "30"
        else:
            return self.tank_amount.text()

    def return_max_distance_drive(self):
        if self.max_distance.text() == "":
            return "10"
        else:
            return self.max_distance.text()
