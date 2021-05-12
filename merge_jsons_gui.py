import sys

from PySide6.QtWidgets import *

import pandas as pd


class MergeFiles(QDialog):

    def __init__(self, parent=None):
        super(MergeFiles, self).__init__(parent)
        self.setWindowTitle("Merge Files")
        self.q_file_dialog = QFileDialog()
        self.button_a = QPushButton("select a file")
        self.button_a_label = QLabel("")
        self.button_a.clicked.connect(self.select_file_a)
        self.button_b = QPushButton("select b file")
        self.button_b_label = QLabel("")
        self.button_b.clicked.connect(self.select_file_b)
        self.line_edit = QLineEdit("input result directory")
        self.button_c = QPushButton("get result")
        self.file_a_path = ""
        self.file_b_path = ""
        self.button_c.clicked.connect(
            lambda: self.get_result(self.file_a_path, self.file_b_path, self.line_edit.text()))
        self.progress_bar = QProgressBar()
        self.progress_bar.setGeometry(30, 40, 200, 25)
        self.progress_bar.setValue(0)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_a)
        self.layout.addWidget(self.button_a_label)
        self.layout.addWidget(self.button_b)
        self.layout.addWidget(self.button_b_label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button_c)
        self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)

    def select_file_a(self):
        self.q_file_dialog.setFileMode(QFileDialog.ExistingFile)
        self.q_file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        self.file_a_path = self.q_file_dialog.getOpenFileName()[0]
        self.button_a_label.setText("file a: " + self.file_a_path)

    def select_file_b(self):
        self.q_file_dialog.setFileMode(QFileDialog.ExistingFile)
        self.q_file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        self.file_b_path = self.q_file_dialog.getOpenFileName()[0]
        self.button_b_label.setText("file b: " + self.file_b_path)

    def get_result(self, file_a_dir, file_b_dir, result_dir):
        a = pd.read_json(file_a_dir, lines=True)
        self.progress_bar.setValue(16.66)
        b = pd.read_json(file_b_dir, lines=True)
        self.progress_bar.setValue(33.32)
        result = pd.concat([a, b])
        self.progress_bar.setValue(49.98)
        result.groupby("timestamp")
        self.progress_bar.setValue(66.64)
        result["timestamp"] = result["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
        self.progress_bar.setValue(83.3)
        result.to_json(result_dir, orient="records", lines=True)
        self.progress_bar.setValue(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    merge_file = MergeFiles()
    merge_file.show()
    sys.exit(app.exec_())
