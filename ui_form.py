# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_randomtips(object):
    def setupUi(self, randomtips):
        if not randomtips.objectName():
            randomtips.setObjectName(u"randomtips")
        randomtips.resize(800, 600)
        self.action_open = QAction(randomtips)
        self.action_open.setObjectName(u"action_open")
        self.action_refresh = QAction(randomtips)
        self.action_refresh.setObjectName(u"action_refresh")
        self.action_exit = QAction(randomtips)
        self.action_exit.setObjectName(u"action_exit")
        self.action_readme = QAction(randomtips)
        self.action_readme.setObjectName(u"action_readme")
        self.centralwidget = QWidget(randomtips)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 72))
        font = QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.textEdit_content = QTextEdit(self.centralwidget)
        self.textEdit_content.setObjectName(u"textEdit_content")
        font1 = QFont()
        font1.setPointSize(12)
        self.textEdit_content.setFont(font1)
        self.textEdit_content.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_content)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.horizontalLayout_2.addWidget(self.label_status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_previous = QPushButton(self.centralwidget)
        self.pushButton_previous.setObjectName(u"pushButton_previous")

        self.horizontalLayout.addWidget(self.pushButton_previous)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout.addWidget(self.pushButton_next)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.SpanningRole, self.verticalLayout)

        randomtips.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(randomtips)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        randomtips.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(randomtips)
        self.statusbar.setObjectName(u"statusbar")
        randomtips.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_refresh)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_readme)

        self.retranslateUi(randomtips)

        QMetaObject.connectSlotsByName(randomtips)
    # setupUi

    def retranslateUi(self, randomtips):
        randomtips.setWindowTitle(QCoreApplication.translate("randomtips", u"\u968f\u673a\u63d0\u793a", None))
        self.action_open.setText(QCoreApplication.translate("randomtips", u"\u8f7d\u5165", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("randomtips", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_refresh.setText(QCoreApplication.translate("randomtips", u"\u91cd\u6392", None))
#if QT_CONFIG(shortcut)
        self.action_refresh.setShortcut(QCoreApplication.translate("randomtips", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_exit.setText(QCoreApplication.translate("randomtips", u"\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("randomtips", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_readme.setText(QCoreApplication.translate("randomtips", u"\u8bf4\u660e", None))
#if QT_CONFIG(shortcut)
        self.action_readme.setShortcut(QCoreApplication.translate("randomtips", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.label_title.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_title.setText(QCoreApplication.translate("randomtips", u"<html><head/><body><p><br/></p></body></html>", None))
        self.textEdit_content.setHtml(QCoreApplication.translate("randomtips", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'HarmonyOS Sans SC'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_status.setText(QCoreApplication.translate("randomtips", u"0 / 0", None))
        self.pushButton_previous.setText(QCoreApplication.translate("randomtips", u"\u4e0a\u4e00\u6761", None))
        self.pushButton_next.setText(QCoreApplication.translate("randomtips", u"\u4e0b\u4e00\u6761", None))
        self.menu.setTitle(QCoreApplication.translate("randomtips", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("randomtips", u"\u5173\u4e8e", None))
    # retranslateUi

