from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)

app = QApplication([])

window = QWidget()
window.setWindowTitle('Кубик')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
rbtn_5 = QRadioButton('5')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
RadioGroup.addButton(rbtn_5)

layout1 = QHBoxLayout()   
layout2 = QVBoxLayout() 
layout3 = QVBoxLayout()
layout4 = QVBoxLayout()

layout2.addWidget(rbtn_1)
layout2.addWidget(rbtn_2)
layout3.addWidget(rbtn_3)
layout4.addWidget(rbtn_4) 
layout4.addWidget(rbtn_5)

layout1.addLayout(layout2)
layout1.addLayout(layout3) 
layout1.addLayout(layout4)

window.setLayout(layout1)
window.resize(300, 400)
window.show()
app.exec_()