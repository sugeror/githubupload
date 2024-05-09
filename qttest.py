import sys
from PyQt5.QtWidgets import QApplication,QWidget


class MyApp(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.initUI(width, height)
    def initUI(self ,w, h,m_w, m_h):
        self.setWindowTitle("나의 첫번째 어플리케이션")
        self.move(300,300)
        self.resize(w,h)
        self.show()

if __name__=='__main__':
    app= QApplication(sys.argv)
    ex= MyApp(50,20)
    sys.exit(app.exec_())