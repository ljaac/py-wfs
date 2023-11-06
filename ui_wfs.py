# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wfssbBhDn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(388, 588)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_import = QPushButton(self.widget)
        self.btn_import.setObjectName(u"btn_import")

        self.gridLayout_2.addWidget(self.btn_import, 0, 0, 1, 1)

        self.ckb_filter = QCheckBox(self.widget)
        self.ckb_filter.setObjectName(u"ckb_filter")

        self.gridLayout_2.addWidget(self.ckb_filter, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.btn_export = QPushButton(self.widget)
        self.btn_export.setObjectName(u"btn_export")

        self.gridLayout_2.addWidget(self.btn_export, 0, 3, 1, 1)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 4)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Word Frequency Statistics", None))
        self.btn_import.setText(QCoreApplication.translate("Form", u"Import", None))
        self.ckb_filter.setText(QCoreApplication.translate("Form", u"Filter", None))
        self.btn_export.setText(QCoreApplication.translate("Form", u"Export", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Word", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Frequency", None));
    # retranslateUi

