from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QDateEdit,
    QComboBox,
    QTableWidget,
    QTableWidgetItem
)
from PySide6.QtCore import QDate, QTimer, Qt


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
    def __init__(self, download_page):
        super().__init__()

        self.download_page = download_page
        self.setup_ui()
        self.connect_signals()
        self.update_instruments()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

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
        """

        self.date_picker = QDateEdit()
        self.date_picker.setDate(QDate.currentDate())
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setMinimumHeight(50)
        self.date_picker.setStyleSheet(field_style)

        self.mission_dropdown = QComboBox()
        self.mission_dropdown.addItems(
            sorted(MISSION_DATA.keys())
        )
        self.mission_dropdown.setMinimumHeight(50)
        self.mission_dropdown.setStyleSheet(field_style)

        self.instrument_dropdown = QComboBox()
        self.instrument_dropdown.setMinimumHeight(50)
        self.instrument_dropdown.setStyleSheet(field_style)

        self.parameter_dropdown = QComboBox()
        self.parameter_dropdown.setMinimumHeight(50)
        self.parameter_dropdown.setStyleSheet(field_style)

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

            QPushButton:pressed {
                background-color: #4C3EE8;
            }
        """)

        search_layout.addWidget(self.date_picker, 1)
        search_layout.addWidget(self.mission_dropdown, 1)
        search_layout.addWidget(self.instrument_dropdown, 1)
        search_layout.addWidget(self.parameter_dropdown, 1)
        search_layout.addWidget(self.search_button)

        main_layout.addWidget(search_card)

        self.results_card = QFrame()
        self.results_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 18px;
                border: 1px solid #E5E7EB;
            }
        """)

        results_layout = QVBoxLayout(self.results_card)

        self.results_status = QLabel("No results yet")
        self.results_status.setStyleSheet("""
            font-size: 16px;
            color: #6B7280;
        """)

        self.results_table = QTableWidget()
        self.results_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #E5E7EB;
                border-radius: 12px;
                gridline-color: #E5E7EB;
                font-size: 14px;
            }

            QHeaderView::section {
            background-color: #F9FAFB;
            border: none;
            border-bottom: 1px solid #E5E7EB;
            padding: 8px;
            font-weight: bold;
            }

            QTableWidget::item {
                padding: 8px;
            }
        """)
        self.results_table.setColumnCount(5)
        self.results_table.setHorizontalHeaderLabels([
            "Select",
            "Filename",
            "Mission",
            "Instrument",
            "Parameter"
        ])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.horizontalHeader().setDefaultSectionSize(180)
        actions_layout = QHBoxLayout()

        self.select_all_btn = QPushButton("Select All")
        self.clear_selection_btn = QPushButton("Clear")
        self.download_selected_btn = QPushButton("Download Selected")
        self.search_button.setCursor(Qt.PointingHandCursor)
        self.select_all_btn.setCursor(Qt.PointingHandCursor)
        self.clear_selection_btn.setCursor(Qt.PointingHandCursor)
        self.download_selected_btn.setCursor(Qt.PointingHandCursor)
        action_button_style = """
            QPushButton {
                background-color: #F3F4F6;
                color: #111827;
                border: none;
                border-radius: 10px;
                padding: 10px 16px;
                font-size: 14px;
                font-weight: 500;
            }

            QPushButton:hover {
                background-color: #E5E7EB;
            }

            QPushButton:pressed {
                background-color: #D1D5DB;
            }
        """

        self.select_all_btn.setStyleSheet(action_button_style)
        self.clear_selection_btn.setStyleSheet(action_button_style)

        self.download_selected_btn.setStyleSheet("""
            QPushButton {
                background-color: #6D5DFB;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 18px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #5B4AF7;
            }
                                                 
            QPushButton:pressed {
                background-color: #4C3EE8;}
        """)

        actions_layout.addWidget(self.select_all_btn)
        actions_layout.addWidget(self.clear_selection_btn)
        actions_layout.addStretch()
        actions_layout.addWidget(self.download_selected_btn)

        results_layout.addLayout(actions_layout)
        results_layout.addWidget(self.results_status)
        results_layout.addWidget(self.results_table)

        main_layout.addWidget(self.results_card, 1)

    def connect_signals(self):
        self.mission_dropdown.currentTextChanged.connect(
            self.update_instruments
        )

        self.instrument_dropdown.currentTextChanged.connect(
            self.update_parameters
        )

        self.search_button.clicked.connect(
            self.start_search
        )
        self.select_all_btn.clicked.connect(
            self.select_all_results
        )

        self.clear_selection_btn.clicked.connect(
            self.clear_selection
        )

        self.download_selected_btn.clicked.connect(
            self.download_selected
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

        if not mission or not instrument:
            return

        if instrument not in MISSION_DATA[mission]:
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

    def start_search(self):
        self.search_button.setText("Searching...")
        self.search_button.setEnabled(False)

        self.results_table.clearContents()
        self.results_table.setRowCount(0)

        self.results_status.setText(
            "Searching solar data...\nPlease wait."
        )
        self.results_status.setStyleSheet("""
            font-size: 16px;
            color: #6B7280;
            padding: 20px;
        """)

        QTimer.singleShot(
            2000,
            self.populate_results
        )
    def populate_results(self):
        mission = self.mission_dropdown.currentText()
        instrument = self.instrument_dropdown.currentText()
        parameter = self.parameter_dropdown.currentText()

        fake_results = [
            "file_001.fits",
            "file_002.fits",
            "file_003.fits"
        ]

        self.results_table.setRowCount(
            len(fake_results)
        )

        for row, file_name in enumerate(fake_results):
            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox_item.setCheckState(Qt.Unchecked)

            self.results_table.setItem(
                row, 0, checkbox_item
            )

            self.results_table.setItem(
                row, 1, QTableWidgetItem(file_name)
            )

            self.results_table.setItem(
                row, 2, QTableWidgetItem(mission)
            )

            self.results_table.setItem(
                row, 3, QTableWidgetItem(instrument)
            )

            self.results_table.setItem(
                row, 4, QTableWidgetItem(parameter)
            )

        self.results_status.setText(
            f"{len(fake_results)} results found"
        )

        self.search_button.setText("Search")
        self.search_button.setEnabled(True)

    def select_all_results(self):
        for row in range(self.results_table.rowCount()):
            item = self.results_table.item(row, 0)
            item.setCheckState(Qt.Checked)


    def clear_selection(self):
        for row in range(self.results_table.rowCount()):
            item = self.results_table.item(row, 0)
            item.setCheckState(Qt.Unchecked)


    def download_selected(self):
        selected_files = []

        for row in range(self.results_table.rowCount()):
            item = self.results_table.item(row, 0)

            if item.checkState()==Qt.Checked:
                file_name = self.results_table.item(
                    row, 1
                ).text()

                selected_files.append(file_name)

        for file_name in selected_files:
            self.download_page.add_download(file_name)
        self.clear_selection()