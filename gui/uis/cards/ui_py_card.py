# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'py_cardaoHjum.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_Card(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(301, 250)
        Form.setMinimumSize(QSize(301, 250))
        Form.setMaximumSize(QSize(301, 250))
        Form.setStyleSheet(u"background:#fffaf0")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_info_layout = QVBoxLayout()
        self.label_info_layout.setObjectName(u"label_info_layout")

        self.horizontalLayout_2.addLayout(self.label_info_layout)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(136, 147))
        self.frame.setMaximumSize(QSize(136, 147))
        self.frame.setStyleSheet(u"background:lightblue")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_operation_layout = QHBoxLayout()
        self.btn_operation_layout.setObjectName(u"btn_operation_layout")

        self.verticalLayout_2.addLayout(self.btn_operation_layout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

