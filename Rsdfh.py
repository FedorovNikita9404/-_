from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle("Ты просто чудо!")
window.move(900, 70)
window.resize(400,200)
window.show()
line = QVBoxLayout()
button = QPushButton('Просто кнопка')
line.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(line)

def show_title():
    title = QLabel('ты приёмный')
    line.addWidget(title, alignment=Qt.AlignCenter)
    window.setLayout(line)

button.clicked.connect(show_title)
app.exec_()