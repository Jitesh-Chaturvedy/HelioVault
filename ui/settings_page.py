from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Settings")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        layout.addWidget(title)
        layout.addStretch()