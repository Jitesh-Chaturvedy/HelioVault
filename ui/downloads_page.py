from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class DownloadsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Downloads")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        layout.addWidget(title)
        layout.addStretch()