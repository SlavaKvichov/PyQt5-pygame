from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget, QFileDialog

def folder_func():
    folderdir = QFileDialog.getExistingDirectory()
    print(folderdir)
    filenames = os.listdir(folderdir)
    print(filenames)
    for file in filenames:
        for req in REQUERMENTS:
            if file .endswith(req):
                img_list.addItem(file)


REQUERMENTS = ['jps']

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
layout_h = QHBoxLayout()
main_win.setLayout(layout_h)
layout_v1 = QVBoxLayout()
layout_h.addLayout(layout_v1)
folder = QPushButton('Папка')
folder.clicked.connect(folder_func)
layout_v1.addWidget(folder)
img_list = QListWidget()
layout_v1.addWidget(img_list)

layout_v2 = QVBoxLayout()
layout_h.addLayout(layout_v2)
img = QLabel('Картинка')
layout_v2.addWidget(img, alignment=Qt.AlignLeft)
layout_v2_h = QHBoxLayout()
layout_v2.addLayout(layout_v2_h)
button_left = QPushButton('Лево')
layout_v2_h.addWidget(button_left)
button_right = QPushButton('Право')
layout_v2_h.addWidget(button_right)
button_mirror = QPushButton('Зеркало')
layout_v2_h.addWidget(button_mirror)
button_blur = QPushButton('Резкость')
layout_v2_h.addWidget(button_blur)
button_grey = QPushButton('Ч/Б')
layout_v2_h.addWidget(button_grey)


main_win.show()
app.exec_()