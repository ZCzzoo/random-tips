# This Python file uses the following encoding: utf-8
import sys
import random

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from ui_form import Ui_randomtips

class randomtips(QMainWindow):
    g_tipslist = []
    g_tipssum = 0
    g_tipsindex = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_randomtips()
        self.ui.setupUi(self)

        self.ui.pushButton_previous.setEnabled(False)
        self.ui.pushButton_next.setEnabled(False)

        self.ui.action_open.triggered.connect(self.loadfile)
        self.ui.action_refresh.triggered.connect(self.listsort)
        self.ui.action_exit.triggered.connect(QApplication.quit)
        self.ui.action_readme.triggered.connect(self.readme)
        self.ui.pushButton_previous.clicked.connect(self.previous_clicked)
        self.ui.pushButton_next.clicked.connect(self.next_clicked)
        self.ui.label_title.linkActivated.connect(self.contentshow)

    #键盘操作
    def keyReleaseEvent(self, event):
        if event.key()==Qt.Key.Key_Left or event.key()==Qt.Key.Key_PageUp or event.key()==Qt.Key.Key_A or event.key()==Qt.Key.Key_Comma:
            self.previous_clicked()

        elif event.key()==Qt.Key.Key_Right or event.key()==Qt.Key.Key_PageDown or event.key()==Qt.Key.Key_D or event.key()==Qt.Key.Key_Period:
            self.next_clicked()

        elif event.key()==Qt.Key.Key_Return or event.key()==Qt.Key.Key_Enter or event.key()==Qt.Key.Key_Space:
            self.contentshow()

        else:
            pass


    #开打文件，重排列表
    def loadfile(self):
        d_openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','text files(*.txt , *.md)')
        self.readtolist(d_openfile_name[0])
        self.listsort()

    #载入文件，生成列表
    def readtolist(self, p_filename):
        global g_tipslist
        global g_tipssum
        global g_tipsindex

        with open(p_filename, 'r') as d_file:
            d_line = d_file.readline()
            d_row = ['','']

            self.g_tipslist.clear()
            self.g_tipssum = 0

            while d_line:
                #标题行
                if d_line.find('#')>=0:

                    if d_row[0]!='':
                        self.g_tipslist.append(d_row)
                        d_row = ['','']

                    # strip()用于去除行末尾的换行符
                    d_line.strip()
                    d_line = d_line.replace('#','')
                    d_row[0] = d_line

                #内容
                else:

                    d_row[1] = d_row[1] + d_line

                d_line = d_file.readline()

        if d_row[0]!='':
            self.g_tipslist.append(d_row)

        self.g_tipssum = len(self.g_tipslist)
        if self.g_tipssum>0:
            self.g_tipsindex = 1
        else:
            self.g_tipsindex = 0

    #列表重排
    def listsort(self):
        global g_tipsindex

        if len(self.g_tipslist)>0:
            random.shuffle(self.g_tipslist)
            self.g_tipsindex = 1

        self.tipshow()
        self.tipscursor()

    #显示提示
    def tipshow(self):
        if self.g_tipssum>0:
            self.ui.textEdit_content.setText('')
            self.ui.label_title.setText('<a href="#" style="text-decoration: none">' + self.g_tipslist[self.g_tipsindex-1][0] + '</a>')
            self.ui.label_status.setText(str(self.g_tipsindex) + ' / ' + str(self.g_tipssum))
        else:
            self.ui.textEdit_content.setText('')
            self.ui.label_title.setText('')
            self.ui.label_status.setText('0 / 0')

    #显示/隐藏内容
    def contentshow(self):
        if self.g_tipsindex>0:
            if self.ui.textEdit_content.toPlainText()=='':
                self.ui.textEdit_content.setText(self.g_tipslist[self.g_tipsindex-1][1])
            else:
                self.ui.textEdit_content.setText('')

    #按键可用
    def tipscursor(self):
        if self.g_tipssum>0:

            if self.g_tipsindex==1:
                self.ui.pushButton_previous.setEnabled(False)
            else:
                self.ui.pushButton_previous.setEnabled(True)

            if self.g_tipsindex>=self.g_tipssum:
                self.ui.pushButton_next.setEnabled(False)
            else:
                self.ui.pushButton_next.setEnabled(True)

        else:

            self.ui.pushButton_previous.setEnabled(False)
            self.ui.pushButton_next.setEnabled(False)

    #上一条
    def previous_clicked(self):
        global g_tipsindex

        if self.g_tipsindex>1:
            self.g_tipsindex -= 1
            self.tipshow()
            self.tipscursor()

    #下一条
    def next_clicked(self):
        global g_tipsindex

        if self.g_tipsindex<self.g_tipssum:
            self.g_tipsindex += 1
            self.tipshow()
            self.tipscursor()

    #说明
    def readme(self):
        d_readme = """<b>操作：</b><br>
                    1、按【载入】数据文件。<br>
                    2、按【上一条】或【下一条】切换提示。<br>
                    3、按【重排】可对提示进行重新随机排序。<br>
                    <br>
                    <b>快捷键：</b><br>
                    载入：<font color="blue">Ctrl + O</font><br>
                    重排：<font color="blue">Ctrl + R</font><br>
                    上一条：<font color="blue">←</font>  、<font color="blue">PgUp</font>  、<font color="blue">A</font>  、<font color="blue">,(&lt;)</font> <br>
                    下一条：<font color="blue">→</font>  、<font color="blue">PgDn</font> 、<font color="blue">D</font>  、<font color="blue">.(&gt;)</font> <br>
                    显示/隐藏内容: <font color="blue">︹(Space)</font> 、<font color="blue">↵(Enter)</font>
                    &nbsp; &nbsp; <br><br>
                    <b>文件格式：</b><br>
                    <font color="green">#</font><font color="red">[提示标题]</font><br>
                    <font color="red">[内容]</font><br>
                    <br>"""

        QMessageBox.about(self, '使用说明', d_readme)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = randomtips()
    widget.show()
    sys.exit(app.exec())
