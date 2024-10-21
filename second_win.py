from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt6.QtGui import QFont
from inst import *
from final_win import *

time = ""
def check_int(text):
    try:
        return int(text)
    except:
        return False

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_layout = QHBoxLayout()
        self.l_layout = QVBoxLayout()
        self.r_layout = QVBoxLayout()
        self.name = QLabel(txt_name)
        self.hintname = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.hintage = QLineEdit(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.starttest2 = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.starttest3 = QPushButton(txt_starttest3)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.timer1 = QLabel(txt_timer)
        self.l_layout.addWidget(self.name, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.hintname, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.age, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.hintage, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.test1, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.starttest1, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.hinttest1, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.test2, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.starttest2, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.test3, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.starttest3, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.hinttest2, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.hinttest3, alignment = Qt.AlignmentFlag.AlignLeft)
        self.l_layout.addWidget(self.sendresults, alignment = Qt.AlignmentFlag.AlignCenter)
        self.r_layout.addWidget(self.timer1, alignment = Qt.AlignmentFlag.AlignCenter)
        self.h_layout.addLayout(self.l_layout)
        self.h_layout.addLayout(self.r_layout)
        self.setLayout(self.h_layout)
    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1event)
        self.timer.start(1000)

    def timer1event(self):
        global time         
        time = time.addSecs(-1)
        self.timer1.setText(time.toString("hh:mm:ss"))
        #self.timer1.setFont(QFont("Times", 36, QFont.bold))
        font = QFont()
        font.setPointSize(36)
        self.timer1.setFont(font)
        self.timer1.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2event)
        self.timer.start(1500)

    def timer2event(self):
        global time
        time = time.addSecs(-1)
        self.timer1.setText(time.toString("hh:mm:ss")[6:8])
        #self.timer1.setFont(QFont("Times", 36, QFont.bold))
        font = QFont()
        font.setPointSize(36)
        self.timer1.setFont(font)
        self.timer1.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_puls(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(1000)

    def timer3event(self):
        global time
        time = time.addSecs(-1)
        self.timer1.setText(time.toString("hh:mm:ss"))
        #self.timer1.setFont(QFont("Times", 36, QFont.bold))
        font = QFont()
        font.setPointSize(36)
        self.timer1.setFont(font)
        self.timer1.setStyleSheet("color: rgb(251, 52, 59)")
        if int(time.toString("hh:mm:ss")[6:8]) == 0:
            self.timer.stop() 
        elif int(time.toString("hh:mm:ss")[6:8]) <= 45 and int(time.toString("hh:mm:ss")[6:8]) >= 16:
            self.timer1.setStyleSheet("color: rgb(125,247,69)") 
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timer1.setStyleSheet("color: rgb(251, 52, 59)")

    def next_click(self):
        hintinfo1 = check_int(self.hintage.text())
        hintinfo2 = check_int(self.hinttest1.text())
        hintinfo3 = check_int(self.hinttest2.text())
        hintinfo4 = check_int(self.hinttest3.text())
        if hintinfo1 == False or hintinfo2 == False or hintinfo3 == False or hintinfo4 == False:
            self.timer1.setText("Обратите внимание на правильность данных, допущена ошибка!")
            self.timer1.setStyleSheet("color: rgb(251, 52, 59)")
        else:
            self.hide()
            self.fw = FinalWin(self.hintname.text(), hintinfo1, hintinfo2, hintinfo3, hintinfo4)

    def connects(self):
        self.sendresults.clicked.connect(self.next_click)
        self.starttest1.clicked.connect(self.timer_test)
        self.starttest2.clicked.connect(self.timer_sits)
        self.starttest3.clicked.connect(self.timer_puls)
        