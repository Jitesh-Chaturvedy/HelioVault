from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QDateEdit,
    QComboBox
)
from PySide6.QtCore import QDate


MISSION_DATA = {
    "GOES": {
        "XRS": [],
        "SUVI": ["94 Å", "131 Å", "171 Å", "195 Å", "284 Å", "304 Å"]
    },
    "SDO": {
        "AIA": [
            "94 Å",
            "131 Å",
            "171 Å",
            "193 Å",
            "211 Å",
            "304 Å",
            "335 Å",
            "1600 Å",
            "1700 Å",
            "4500 Å"
        ],
        "HMI": []
    },
    "SOHO": {
        "LASCO": [],
        "EIT": []
    }
}


class SearchPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.connect_signals()
        self.update_instruments()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Header
        title = QLabel("Search Solar Data")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #111827;
        """)

        subtitle = QLabel(
            "Find and access data from multiple solar missions"
        )
        subtitle.setStyleSheet("""
            font-size: 14px;
            color: #6B7280;
        """)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # Search Card
        search_card = QFrame()
        search_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 18px;
                border: 1px solid #E5E7EB;
            }
        """)

        search_layout = QHBoxLayout(search_card)
        search_layout.setContentsMargins(20, 20, 20, 20)
        search_layout.setSpacing(20)

        field_style = """
            QDateEdit, QComboBox {
                border: 1px solid #E5E7EB;
                border-radius: 14px;
                padding: 10px;
                background: white;
                font-size: 14px;
            }

            QComboBox::drop-down {
                border: none;
            }
        """

        # Date Picker
        self.date_picker = QDateEdit()
        self.date_picker.setDate(QDate.currentDate())
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setMinimumHeight(50)
        self.date_picker.setStyleSheet(field_style)

        # Mission Dropdown
        self.mission_dropdown = QComboBox()
        self.mission_dropdown.addItems(
            sorted(MISSION_DATA.keys())
        )
        self.mission_dropdown.setMinimumHeight(50)
        self.mission_dropdown.setStyleSheet(field_style)

        # Instrument Dropdown
        self.instrument_dropdown = QComboBox()
        self.instrument_dropdown.setMinimumHeight(50)
        self.instrument_dropdown.setStyleSheet(field_style)

        # Parameter Dropdown
        self.parameter_dropdown = QComboBox()
        self.parameter_dropdown.setMinimumHeight(50)
        self.parameter_dropdown.setStyleSheet(field_style)

        # Search Button
        self.search_button = QPushButton("Search")
        self.search_button.setMinimumHeight(50)
        self.search_button.setFixedWidth(160)

        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #6D5DFB;
                color: white;
                border: none;
                border-radius: 14px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #5B4AF7;
            }
        """)

        # Add widgets in same row
        search_layout.addWidget(self.date_picker, 1)
        search_layout.addWidget(self.mission_dropdown, 1)
        search_layout.addWidget(self.instrument_dropdown, 1)
        search_layout.addWidget(self.parameter_dropdown, 1)
        search_layout.addWidget(self.search_button)

        main_layout.addWidget(search_card)

        # Help Card Placeholder
        help_card = QFrame()
        help_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 18px;
                border: 1px solid #E5E7EB;
            }
        """)

        help_layout = QVBoxLayout(help_card)

        help_title = QLabel("How it works (Dismissible)")
        help_title.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
        """)

        help_layout.addWidget(help_title)

        main_layout.addWidget(help_card)

        # Results Placeholder
        results_card = QFrame()
        results_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 18px;
                border: 1px solid #E5E7EB;
            }
        """)

        results_layout = QVBoxLayout(results_card)

        results_label = QLabel("Results will appear here")
        results_label.setStyleSheet("""
            font-size: 18px;
            color: #6B7280;
        """)

        results_layout.addWidget(results_label)

        main_layout.addWidget(results_card, 1)

    def connect_signals(self):
        self.mission_dropdown.currentTextChanged.connect(
            self.update_instruments
        )

        self.instrument_dropdown.currentTextChanged.connect(
            self.update_parameters
        )

    def update_instruments(self):
        mission = self.mission_dropdown.currentText()

        self.instrument_dropdown.clear()

        instruments = sorted(
            MISSION_DATA[mission].keys()
        )

        self.instrument_dropdown.addItems(instruments)

        self.update_parameters()

    def update_parameters(self):
        mission = self.mission_dropdown.currentText()
        instrument = self.instrument_dropdown.currentText()

        self.parameter_dropdown.clear()

        # Safety checks
        if not mission:
            return

        if not instrument:
            self.parameter_dropdown.setEnabled(False)
            self.parameter_dropdown.addItem(
                "No additional parameters"
            )
            return

        if mission not in MISSION_DATA:
            return

        if instrument not in MISSION_DATA[mission]:
            self.parameter_dropdown.setEnabled(False)
            self.parameter_dropdown.addItem(
                "No additional parameters"
            )
            return

        parameters = MISSION_DATA[mission][instrument]

        if parameters:
            self.parameter_dropdown.setEnabled(True)
            self.parameter_dropdown.addItems(parameters)
        else:
            self.parameter_dropdown.setEnabled(False)
            self.parameter_dropdown.addItem(
                "No additional parameters"
            )