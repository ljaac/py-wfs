import os
import sys
import re
import pandas as pd
import images
from nltk.corpus import stopwords
from collections import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon
from wfs_ui import Ui_Form
from qt_material import apply_stylesheet


# 重写QTableWidgetItem，便于排序词频
class NumberTableWidgetItem(QTableWidgetItem):
    def __init__(self, value):
        super().__init__(str(value))

    def __lt__(self, other):
        if isinstance(other, QTableWidgetItem):
            try:
                return float(self.text()) < float(other.text())
            except ValueError:
                pass
        # 如果无法转换成数字，则按照字典序进行排序
        return super().__lt__(other)


class WFS(Ui_Form, QWidget):
    def __init__(self):
        self.words_text = ''
        super(WFS, self).__init__()
        self.setupUi(self)
        self.set_user()

    def set_user(self):
        self.setWindowIcon(QIcon(':/wfs.ico'))
        self.setAcceptDrops(True)
        self.set_connect()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() and len(event.mimeData().urls()) == 1:
            event.accept()
        else:
            event.ignort()

    def dropEvent(self, event):
        try:
            file_name = event.mimeData().urls()[0].toLocalFile()
            if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                self.excel_processing(file_name)
        except Exception as e:
            msg = str(e)
            QMessageBox.warning(self, "ERROR", msg, QMessageBox.Ok)

    def set_connect(self):
        self.btn_import.clicked.connect(self.excel_import)
        self.btn_export.clicked.connect(self.excel_export)
        self.ckb_filter.stateChanged.connect(self.excel_filter_changed)
        self.ckb_case_sensitive.stateChanged.connect(self.excel_case_sensitive_changed)

    def words_2_word_count(self, case_sensitive=False, filter_stop_words=False, sort=True):
        try:
            words_text = self.words_text
            # 区分大小写
            if not case_sensitive:
                words_text = words_text.lower()
            # 将字符串分割为单词列表
            words = words_text.split()
            # 过滤掉停用词
            if filter_stop_words:
                words = [word for word in words if (word not in stopwords.words('english'))]
            # 统计每个单词出现的次数
            word_count = Counter(words)
            # 是否排序输出
            if sort:
                word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
            # 显示到表格中
            self.show_words(word_count)
        except Exception as e:
            msg = str(e)
            QMessageBox.warning(self, "ERROR", msg, QMessageBox.Ok)

    def excel_processing(self, file_name):
        # 读取 excel 文件
        df = pd.read_excel(file_name)
        # 将单元格内容拼接为一个字符串
        text = ' '.join(df.stack().astype(str).tolist())
        # 删除所有符号
        self.words_text = re.sub(r'[^a-zA-Z0-9\s]+', '', text)
        # 输出结果
        self.words_2_word_count(Qt.Checked == self.ckb_case_sensitive.checkState(),
                                Qt.Checked == self.ckb_filter.checkState())

    def show_words(self, word_count):
        # 清空表格
        if self.tableWidget.rowCount() > 0:
            # 排序后再清空表格，否则可能因为之前排序导致行号错误未能正确清空，使其显示第二列信息缺失
            self.tableWidget.sortItems(1, Qt.DescendingOrder)
            self.tableWidget.model().removeRows(0, self.tableWidget.rowCount())
        self.tableWidget.setRowCount(len(word_count))
        words = list(word_count.keys())
        counts = list(word_count.values())
        for i, word in enumerate(words):
            item_word = NumberTableWidgetItem(str(word))
            self.tableWidget.setItem(i, 0, item_word)
            count = counts[i]
            item_count = NumberTableWidgetItem(str(count))
            self.tableWidget.setItem(i, 1, item_count)

    def excel_import(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(self.widget,
                                                       "Select Excel table",
                                                       os.getcwd(),
                                                       "Excel Files (*.xls*);;")
            if "" == file_name:
                return
            self.excel_processing(file_name)
        except Exception as e:
            msg = str(e)
            QMessageBox.warning(self, "ERROR", msg, QMessageBox.Ok)

    def excel_export(self):
        try:
            row_count = self.tableWidget.rowCount()
            if 0 == row_count:
                QMessageBox.warning(self, "Warning", "The table is empty. Please import the table first.",
                                    QMessageBox.Ok)
                return
            # 选择保存目录
            file_name, _ = QFileDialog.getSaveFileName(self.widget,
                                                       "Select a save path",
                                                       os.getcwd(),
                                                       "Excel Files (*.xlsx);;")
            if "" == file_name:
                return
            # 将QTableWidget数据存储到二维列表中
            data = []
            for i in range(row_count):
                row_data = []
                for j in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(i, j)
                    row_data.append(item.text() if item is not None else "")
                data.append(row_data)
            # 创建一个pandas数据帧
            df = pd.DataFrame(data, columns=[self.tableWidget.horizontalHeaderItem(j).text() for j in
                                             range(self.tableWidget.columnCount())])
            # 将数据帧写入Excel文件
            df.to_excel(file_name, index=False)
        except Exception as e:
            msg = str(e)
            QMessageBox.warning(self, "ERROR", msg, QMessageBox.Ok)

    def excel_filter_changed(self, checked):
        self.words_2_word_count(Qt.Checked == self.ckb_case_sensitive.checkState(), checked)

    def excel_case_sensitive_changed(self, checked):
        self.words_2_word_count(checked, Qt.Checked == self.ckb_filter.checkState())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''
        https://github.com/UN-GCPDS/qt-material
            ['dark_amber.xml',
         'dark_blue.xml',
         'dark_cyan.xml',
         'dark_lightgreen.xml',
         'dark_pink.xml',
         'dark_purple.xml',
         'dark_red.xml',
         'dark_teal.xml',
         'dark_yellow.xml',
         'light_amber.xml',
         'light_blue.xml',
         'light_cyan.xml',
         'light_cyan_500.xml',
         'light_lightgreen.xml',
         'light_pink.xml',
         'light_purple.xml',
         'light_red.xml',
         'light_teal.xml',
         'light_yellow.xml']
    '''
    apply_stylesheet(app, theme='dark_blue.xml')
    w = WFS()
    w.show()
    sys.exit(app.exec_())
