from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QLabel,
    QMessageBox,
    QGridLayout,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

# from services.audio_processor import process_audio


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Speed Editor")
        self.setWindowIcon(QIcon("assets/main_icon.png"))

        self.main_layout = QVBoxLayout()
        self.speed_layout = QGridLayout()
        self.speed_layout.setAlignment(Qt.AlignHCenter)

        self.label = QLabel("Nenhum arquivo selecionado")

        self.select_button = QPushButton("Selecionar Áudio")
        self.select_button.clicked.connect(self.select_file)

        self.label_speed = QLabel("Velocidade Desejada (0,5 a 2,0):")

        self.speed_input = QDoubleSpinBox()
        self.speed_input.setMaximum(2.00)
        self.speed_input.setMinimum(0.50)
        self.speed_input.setSingleStep(0.01)

        self.process_button = QPushButton("Processar")
        self.process_button.clicked.connect(self.process)

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.select_button)
        self.speed_layout.addWidget(self.label_speed, 0, 0)
        self.speed_layout.addWidget(self.speed_input, 0, 1)
        self.main_layout.addLayout(self.speed_layout)
        self.main_layout.addWidget(self.process_button)

        self.setLayout(self.main_layout)

        self.file_path = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Selecionar áudio", "", "Audio Files (*.mp3 *.wav *.aac *.m4a)"
        )

        if file_path:
            self.file_path = file_path
            self.label.setText(file_path)

    def process(self):
        if not self.file_path:
            QMessageBox.critical(self, "Erro", "Nenhum arquivo selecionado")
            return

        try:
            speed = float(self.speed_input.text())
            # output = process_audio(self.file_path, speed)
            # QMessageBox.information(self, "Sucesso", f"Arquivo salvo como:\n{output}")
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
        except Exception:
            QMessageBox.critical(self, "Erro", "Falha ao processar áudio.")
