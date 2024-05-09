from PyQt5.QtWidgets import  (QApplication , QMainWindow,
                              QLineEdit,QPushButton,QPlainTextEdit,QVBoxLayout,QWidget)
import sys
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWidget = QWidget()
        self.listAdd=[]
        self.listMul=[]
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.buttunMul = QPushButton("누적곱하기")
        self.buttunSum = QPushButton("누적 합")
        self.guguBtn = QPushButton("구구단 버튼")
        self.textbox = QPlainTextEdit("2*1" +str(2*1) +"="+"2\n2*2" +str(2*2) +"="+"4\n ")
        self.lineEditMul = QLineEdit()
        self.lineEditSum = QLineEdit()
        self.guguEdit = QLineEdit()
        self.mainLayout.addWidget(self.mainWidget)
        self.mainLayout.addWidget(self.buttonMul)
        self.mainLayout.addWidget(self.buttonSum)
        self.mainLayout.addWidget(self.guguBtn)
        self.mainLayout.addWidget(self.lineEditMul)
        self.mainLayout.addWidget(self.lineEditSum)
        self.mainLayout.addWidget(self.textbox)
        self.buttonMul.clicked.connect(self.listMul)
        self.guguBtn.clicked.connect(self.gugu)
        self.setCentralWidget(self.mainWidget)
        self.textbox.setPlainText("asdfafa\ndsafaf") #여기는 구구단 츌력
    def mul(self,checked):
        print('mul 버튼이 눌렸어요',self.lineEditMul.text())
        self.listAdd.append(self.lineEditMul.text())
        self.total=0
        if len(self.listMUl)>=5:
            for i in self.listMul:
                self.total+= int(i)
            self.listMul=[]
            self.lineEditMul.setText("리스트의 누적 곱 은 "+str(self.total))
    def add(self,checked):
        print('add 버튼이 눌렸어요',self.lineEditSum.text())
        self.listAdd.append(self.lineEditSum.text())
        self.total=0
        if len(self.listAdd)>=5:
            for i in self.listAdd:
                self.total+= int(i)
            self.listAdd=[]
            self.lineEditSum.setText("리스트의 누적 합은 "+str(self.total))
    def gugu(self):
        print("구구단 버튼이 눌렸어요")
        #5번째 입력된 값으로 구구단을 구하세요
        str=""
        for i in range(10):
            str_1=self.listAdd[0] #리스트의 마지막 값으로 구구단
            print(str_1 ,type(str_1))
            str+= "\n".join([f"{str_1} x {i} = {int(str_1)*i}" for i in range(1,10)])
            print(str)
            self.textbox.setPlainText(str)
app =QApplication(sys.argv)
w= MainWindow() #MainWindow 객체 생성시 생성자에서 2개의 window 객체 생성
#멤버변수 cnt의 값이 3의 배수일 경우와 그렇지 않은 경우의 서로 다른 윈도우를 표시하고 다른
#윈도우는 종료함
w.show()
app.exec()