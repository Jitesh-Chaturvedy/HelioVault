from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton,
    QProgressBar,
    QScrollArea
)
from PySide6.QtCore import Qt


class DownloadCard(QFrame):
    def __init__(self, file_name, status="Queued", progress=0):
        super().__init__()

        self.file_name = file_name
        self.status = status
        self.progress = progress
        self.timestamp = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        self.setup_ui()

    def setup_ui(self):
        self.setFixedHeight(82)

        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ECECEC;
                border-radius: 14px;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(18)

        # Left section (filename + timestamp)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(3)

        file_label = QLabel(self.file_name)
        file_label.setStyleSheet("""
            border: none;
            background: transparent;
            font-size: 13px;
            font-weight: 600;
            color: #111827;
        """)

        time_label = QLabel(self.timestamp)
        time_label.setStyleSheet("""
            border: none;
            background: transparent;
            font-size: 11px;
            color: #6B7280;
        """)

        left_layout.addWidget(file_label)
        left_layout.addWidget(time_label)

        # Status chip
        status_label = QLabel(self.status)
        status_label.setAlignment(Qt.AlignCenter)
        status_label.setFixedSize(80, 28)

        status_label.setStyleSheet("""
            QLabel {
                background-color: #FEF3C7;
                color: #92400E;
                border: none;
                border-radius: 8px;
                font-size: 11px;
                font-weight: 600;
            }
        """)

        # Progress section
        progress_layout = QHBoxLayout()
        progress_layout.setSpacing(10)

        progress_bar = QProgressBar()
        progress_bar.setValue(self.progress)
        progress_bar.setTextVisible(False)
        progress_bar.setFixedHeight(8)

        progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #F3F4F6;
                border: none;
                border-radius: 4px;
            }

            QProgressBar::chunk {
                background-color: #6D5DFB;
                border-radius: 4px;
            }
        """)

        percent_label = QLabel(f"{self.progress}%")
        percent_label.setStyleSheet("""
            border: none;
            background: transparent;
            font-size: 12px;
            font-weight: 600;
            color: #111827;
        """)
        percent_label.setFixedWidth(35)

        progress_layout.addWidget(progress_bar)
        progress_layout.addWidget(percent_label)

        layout.addLayout(left_layout, 4)
        layout.addWidget(status_label, 1)
        layout.addLayout(progress_layout, 4)


class DownloadsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.download_cards = []

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(28, 24, 28, 24)
        main_layout.setSpacing(18)

        # Header
        title = QLabel("Downloads")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: 700;
            color: #111827;
        """)

        subtitle = QLabel(
            "Monitor and manage your data downloads"
        )
        subtitle.setStyleSheet("""
            font-size: 13px;
            color: #6B7280;
        """)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # Stats section
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(14)

        self.total_card = self.create_stat_card(
            "Total", "0"
        )

        self.active_card = self.create_stat_card(
            "Downloading", "0"
        )

        self.completed_card = self.create_stat_card(
            "Completed", "0"
        )

        self.failed_card = self.create_stat_card(
            "Failed", "0"
        )

        stats_layout.addWidget(self.total_card)
        stats_layout.addWidget(self.active_card)
        stats_layout.addWidget(self.completed_card)
        stats_layout.addWidget(self.failed_card)

        main_layout.addLayout(stats_layout)

        # Filter row
        filters_layout = QHBoxLayout()
        filters_layout.setSpacing(18)

        for label in [
            "All",
            "Downloading",
            "Completed",
            "Failed"
        ]:
            btn = QPushButton(label)

            btn.setCursor(Qt.PointingHandCursor)

            btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    border: none;
                    font-size: 13px;
                    font-weight: 500;
                    color: #4B5563;
                }

                QPushButton:hover {
                    color: #6D5DFB;
                }
            """)

            filters_layout.addWidget(btn)

        filters_layout.addStretch()

        main_layout.addLayout(filters_layout)

        # Scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background: transparent;
            }

            QScrollBar:vertical {
                width: 8px;
                border: none;
                background: transparent;
            }

            QScrollBar::handle:vertical {
                background: #D1D5DB;
                border-radius: 4px;
                min-height: 20px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        self.scroll_content = QWidget()

        self.cards_layout = QVBoxLayout(self.scroll_content)
        self.cards_layout.setSpacing(12)
        self.cards_layout.setContentsMargins(0, 0, 8, 0)

        self.cards_layout.addStretch()

        self.scroll_area.setWidget(self.scroll_content)

        main_layout.addWidget(self.scroll_area)

    def create_stat_card(self, title, value):
        card = QFrame()
        card.setFixedHeight(76)

        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #ECECEC;
                border-radius: 14px;
            }
        """)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 10, 16, 10)
        layout.setSpacing(4)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            border: none;
            background: transparent;
            font-size: 11px;
            color: #6B7280;
        """)

        value_label = QLabel(value)
        value_label.setStyleSheet("""
            border: none;
            background: transparent;
            font-size: 22px;
            font-weight: 700;
            color: #111827;
        """)

        card.value_label = value_label

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        return card

    def update_stats(self):
        total = len(self.download_cards)

        self.total_card.value_label.setText(str(total))

        queued_count = len([
            card for card in self.download_cards
            if card.status == "Queued"
        ])

        self.active_card.value_label.setText(
            str(queued_count)
        )

        self.completed_card.value_label.setText("0")
        self.failed_card.value_label.setText("0")

    def add_download(self, file_name):
        card = DownloadCard(file_name)

        self.download_cards.append(card)

        self.cards_layout.insertWidget(
            self.cards_layout.count() - 1,
            card
        )

        self.update_stats()