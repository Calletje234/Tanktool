from PyQt5.QtWidgets import *
from GUI.Optional_options import OptionalOptions
from GUI.Radio_button import RadioButton
from Init_search import InitiateSearch


class MainScreen(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Tank Tool")
        self.main_frame = QVBoxLayout()

        # Create UI Elements
        self.plaats = QLabel("Plaats")
        self.location = QLineEdit()
        self.zoeken = QPushButton("Zoek")
        self.location_nearest = QTextEdit()
        self.radio_buttons = RadioButton()
        self.ui_buttons = self.radio_buttons.return_radio_buttons()
        self.optional_options = OptionalOptions()
        self.options_fields = self.optional_options.return_optional_options_layout()

        # Set Search Function
        self.zoeken.clicked.connect(lambda: self.get_information())

        # Add Items to GUI
        self.main_frame.addWidget(self.plaats)
        self.main_frame.addWidget(self.location)
        self.main_frame.addLayout(self.ui_buttons)
        self.main_frame.addLayout(self.options_fields)
        self.main_frame.addWidget(self.zoeken)
        self.main_frame.addWidget(self.location_nearest)

        self.setLayout(self.main_frame)
        self.setGeometry(500, 500, 500, 500)

    def get_information(self):
        fuel_type = self.radio_buttons.return_selected_buttons()
        location = self.location.text()
        car_usage = self.optional_options.return_car_usage()
        fill_amount = self.optional_options.return_amount_tank_fill()
        max_distance = self.optional_options.return_max_distance_drive()
        run_info = InitiateSearch(location, fuel_type, car_usage, fill_amount, max_distance)
        self.location_nearest.setPlainText(run_info.find_station())

