from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit
from inst import *

class FinalWin(QWidget):
    def __init__(self, username, age, t1, t2, t3):
        super().__init__()
        self.username = username
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.set_appear()
        self.initUI()
        self.show()
        self.index_Rufie()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.layout = QVBoxLayout()
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def index_Rufie(self):
        final_index = (4 * (int(self.t1)  + int(self.t2) + int(self.t3))-200)/10
        self.index.setText(txt_index + str(final_index))
        if int(self.age) >= 15:
            if final_index >= 15:
                rate_workheart = txt_res1
            elif final_index < 15 and final_index >= 11:
                rate_workheart = txt_res2
            elif final_index < 11 and final_index >= 6:
                rate_workheart = txt_res3
            elif final_index < 6 and final_index >= 0.5:
                rate_workheart = txt_res4
            elif final_index <= 0.4:
                rate_workheart = txt_res5
        elif int(self.age) <= 14 and int(self.age) >= 13:
            if final_index >= 16.5:
                rate_workheart = txt_res1
            elif final_index < 16.5 and final_index >= 12.5:
                rate_workheart = txt_res2
            elif final_index < 12.5 and final_index >= 7.5:
                rate_workheart = txt_res3
            elif final_index < 7.5 and final_index >= 2:
                rate_workheart = txt_res4
            elif final_index <= 1.9:
                rate_workheart = txt_res5
        elif int(self.age) <= 12 and int(self.age) >= 11:
            if final_index >= 18:
                rate_workheart = txt_res1
            elif final_index < 18 and final_index >= 14:
                rate_workheart = txt_res2
            elif final_index < 14 and final_index >= 9:
                rate_workheart = txt_res3
            elif final_index < 9 and final_index >= 3.5:
                rate_workheart = txt_res4
            elif final_index <= 3.4:
                rate_workheart = txt_res5
        elif int(self.age) <= 10 and int(self.age) >= 9:
            if final_index >= 19.5:
                rate_workheart = txt_res1
            elif final_index < 19.5 and final_index >= 15.5:
                rate_workheart = txt_res2
            elif final_index < 15.5 and final_index >= 10.5:
                rate_workheart = txt_res3
            elif final_index < 10.5 and final_index >= 5:
                rate_workheart = txt_res4
            elif final_index <= 4.9:
                rate_workheart = txt_res5
        elif int(self.age) <= 8 and int(self.age) >= 7:
            if final_index >= 21:
                rate_workheart = txt_res1
            elif final_index < 21 and final_index >= 17:
                rate_workheart = txt_res2
            elif final_index < 17 and final_index >= 12:
                rate_workheart = txt_res3
            elif final_index < 12 and final_index >= 6.5:
                rate_workheart = txt_res4
            elif final_index <= 6.5:
                rate_workheart = txt_res5
        self.workheart.setText(self.username + txt_workheart + rate_workheart)

        

        

        