from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QFrame
)
from PySide6.QtCore import Qt

from ui.search_page import SearchPage
from ui.downloads_page import DownloadsPage
from ui.library_page import LibraryPage
from ui.settings_page import SettingsPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HelioVault")
        self.resize(1400, 850)

        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(260)

        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(20, 20, 20, 20)
        sidebar_layout.setSpacing(20)

        self.title = QLabel("HelioVault")
        self.title.setAlignment(Qt.AlignLeft)

        self.search_btn = QPushButton("Search")
        self.downloads_btn = QPushButton("Downloads")
        self.library_btn = QPushButton("Library")
        self.settings_btn = QPushButton("Settings")

        self.buttons = [
            self.search_btn,
            self.downloads_btn,
            self.library_btn,
            self.settings_btn
        ]

        for btn in self.buttons:
            btn.setMinimumHeight(50)

        sidebar_layout.addWidget(self.title)
        sidebar_layout.addSpacing(20)

        for btn in self.buttons:
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        self.stack = QStackedWidget()

        
        self.downloads_page = DownloadsPage()
        self.search_page = SearchPage(
            download_page=self.downloads_page
        )
        self.library_page = LibraryPage()
        self.settings_page = SettingsPage()

        self.stack.addWidget(self.search_page)
        self.stack.addWidget(self.downloads_page)
        self.stack.addWidget(self.library_page)
        self.stack.addWidget(self.settings_page)

        self.search_btn.clicked.connect(
            lambda: self.switch_page(0)
        )
        self.downloads_btn.clicked.connect(
            lambda: self.switch_page(1)
        )
        self.library_btn.clicked.connect(
            lambda: self.switch_page(2)
        )
        self.settings_btn.clicked.connect(
            lambda: self.switch_page(3)
        )

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stack)

        self.switch_page(0)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)

        for btn in self.buttons:
            btn.setProperty("active", False)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

        active_btn = self.buttons[index]
        active_btn.setProperty("active", True)
        active_btn.style().unpolish(active_btn)
        active_btn.style().polish(active_btn)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #F8F9FC;
                font-family: Segoe UI;
            }

            QFrame {
                background-color: white;
                border-right: 1px solid #E6E8EC;
            }

            QLabel {
                color: #111827;
            }

            QLabel#title {
                font-size: 26px;
                font-weight: bold;
            }

            QPushButton {
                background-color: white;
                border: none;
                border-radius: 14px;
                padding: 14px;
                text-align: left;
                font-size: 15px;
            }

            QPushButton:hover {
                background-color: #F3F4F6;
            }

            QPushButton[active="true"] {
                background-color: #6D5DFB;
                color: white;
                font-weight: bold;
            }
        """)

        self.title.setObjectName("title")