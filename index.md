import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QAction,qApp,\
QFileDialog,QTextEdit,QHBoxLayout,QVBoxLayout,QPushButton,QMessageBox,QTextBrowser,\
QLabel
from PyQt5.QtGui import QIcon,QPixmap
import BACK

class Ico(QMainWindow):

   def __init__(self):
       super().__init__()
       self.initUI()

   def initUI(self):
       self.statusBar().showMessage('准备就绪')#状态栏

       self.setGeometry(500, 200, 960, 593.3)
       self.setWindowTitle('提取对话1.0')
       self.setWindowIcon(QIcon('./img/tubiao.jpg'))#这里需要一个图标

       self.bt1 = QPushButton('提取对话', self)
       self.bt1.clicked.connect(self.showtx2)

       self.tx1_label = QLabel('原文', self)
       self.tx2_label = QLabel('提取后台词', self)

       self.tx1 = QTextEdit(self)

       self.tx2 = QTextBrowser(self)

       self.tx1_v_layout = QVBoxLayout()
       self.tx2_v_layout = QVBoxLayout()
       self.button_layout=QHBoxLayout()
       self.text_layout = QHBoxLayout()
       self.all_h_layout=QVBoxLayout()

       self.tx1_v_layout.addWidget(self.tx1_label)
       self.tx1_v_layout.addWidget(self.tx1)

       self.tx2_v_layout.addWidget(self.tx2_label)
       self.tx2_v_layout.addWidget(self.tx2)

       self.button_layout.addWidget(self.bt1)

       self.text_layout.addLayout(self.tx1_v_layout)
       self.text_layout.addLayout(self.tx2_v_layout)
       self.all_h_layout.addLayout(self.text_layout)
       self.all_h_layout.addLayout(self.button_layout)

       main_widget = QWidget()
       main_widget.setLayout(self.all_h_layout)
       self.setCentralWidget(main_widget)

       exitAct = QAction( '退出', self)
       exitAct.setStatusTip('退出程序')
       exitAct.triggered.connect(qApp.quit)

       saveAct = QAction( '保存', self)
       saveAct.setStatusTip('选择目录保存')
       saveAct.triggered.connect(self.save_text)

       openAct = QAction( '打开', self)
       openAct.setStatusTip('打开文件')
       openAct.triggered.connect(self.openfile)

       shuomingAct=QAction('说明',self)
       shuomingAct.triggered.connect(self.about_)

       qqAct=QAction('有疑问请QQ联系',self)
       qqAct.triggered.connect(self.QQshow)
       menubar = self.menuBar()
       fileMenu = menubar.addMenu('文件')
       fileMenu.addAction(openAct)
       fileMenu.addAction(saveAct)
       fileMenu.addSeparator()#分隔符
       fileMenu.addAction(exitAct)

       guanyuMenu=menubar.addMenu('关于')
       guanyuMenu.addAction(shuomingAct)
       guanyuMenu.addAction(qqAct)

       self.show()

   def openfile(self):
       fname = QFileDialog.getOpenFileName(self, '打开文件', './')
       if fname[0]:
           with open(fname[0], 'r', encoding='gb18030', errors='ignore') as f:
               self.tx1.setText(f.read())

   def showtx2(self):
       STR=self.tx1.toPlainText()
       m=BACK.trans(STR)
       for l in m:
           for h in l:
              self.tx2.append(h)

   def save_text(self):
       fname = QFileDialog.getSaveFileName(self, '保存文件', './', ("*.txt"))
       if fname[0]:
           with open(fname[0], 'a+', encoding='gb18030', errors='ignore') as text_1:
               text_1.write(self.tx2.toPlainText())

   def about_(self):
       msgBox = QMessageBox.about(self,'说明','更多功能敬请期待')

   def QQshow(self):
       msgBox = QMessageBox(QMessageBox.NoIcon, '作者QQ', '')
       msgBox.setIconPixmap(QPixmap("./img/QQ.jpg"))
       msgBox.exec()

if __name__ == '__main__':
   bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
   path_to_dat = path.join(bundle_dir, 'other-file.dat')
   app = QApplication(sys.argv)
   ex = Ico()
   sys.exit(app.exec_())
