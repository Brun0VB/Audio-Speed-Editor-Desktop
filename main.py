import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale
from ui.mainWindow import MainWindow

if __name__ == "__main__":
    QLocale.setDefault(QLocale.Language.C)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 200)
    window.show()
    sys.exit(app.exec())