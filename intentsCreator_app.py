# Copyright (C) 2023 by Nikodem "Med0kin" Kuliś
# This file is part of the intentsCreator project,
# and is released under the "MIT License Agreement".
# Please see the LICENSE file that should have been included
# as part of this package.

import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import json_maker as jmaker
import json_merger as jmerger


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("intentsCreator")
        self.width = 800
        self.height = 600
        #self.setMinimumSize(self.width, self.height)
        self.dictionary = jmaker.new_json()

        self.setup_UI()
        self.show()
    

    def setup_UI(self):
        # Main Layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # Top Layout
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)
        # Top Left Layout
        self.top_left_layout = QVBoxLayout()
        self.top_layout.addLayout(self.top_left_layout)
        # Top Right Layout
        self.top_right_layout = QVBoxLayout()
        self.top_layout.addLayout(self.top_right_layout)
        # Bottom Layout
        self.bottom_layout = QVBoxLayout()
        self.main_layout.addLayout(self.bottom_layout)
        # Bottom Left Layout
        self.bottom_left_layout = QVBoxLayout()
        self.bottom_layout.addLayout(self.bottom_left_layout)
        # Bottom Right Layout
        self.bottom_right_layout = QVBoxLayout()
        self.bottom_layout.addLayout(self.bottom_right_layout)

        # Top Left Widgets
        self.tag_label = QLabel("Tag:")
        self.top_left_layout.addWidget(self.tag_label)
        self.tag_line_edit = QLineEdit()
        self.top_left_layout.addWidget(self.tag_line_edit)

        # Top Right Widgets
        self.tag_list = QListWidget()
        self.top_right_layout.addWidget(self.tag_list)

        # Bottom Left Widgets
        self.pattern_label = QLabel("Pattern:")
        self.bottom_left_layout.addWidget(self.pattern_label)
        self.pattern_line_edit = QLineEdit()
        self.bottom_left_layout.addWidget(self.pattern_line_edit)

        self.pattern_list = QListWidget()
        self.bottom_left_layout.addWidget(self.pattern_list)

        # Bottom Right Widgets
        self.response_label = QLabel("Response:")
        self.bottom_right_layout.addWidget(self.response_label)
        self.response_line_edit = QLineEdit()
        self.bottom_right_layout.addWidget(self.response_line_edit)

        self.response_list = QListWidget()
        self.bottom_right_layout.addWidget(self.response_list)

        # Bottom Widgets
        self.filename_label = QLabel("File name:")
        self.bottom_layout.addWidget(self.filename_label)
        self.filename_line_edit = QLineEdit()
        self.bottom_layout.addWidget(self.filename_line_edit)

        self.save_button = QPushButton("Save")
        self.bottom_layout.addWidget(self.save_button)
        self.load_button = QPushButton("Load")
        self.bottom_layout.addWidget(self.load_button)
        self.clear_button = QPushButton("Clear")
        self.bottom_layout.addWidget(self.clear_button)
        self.exit_button = QPushButton("Exit")
        self.bottom_layout.addWidget(self.exit_button)


        # Buttons connections
        button_list = [self.save_button, self.load_button, self.clear_button, self.exit_button]
        for button in button_list:
            button.clicked.connect(self.button_clicked)

        # List connections
        lists_list = [self.tag_list, self.pattern_list, self.response_list]
        for list in lists_list:
            list.itemClicked.connect(self.list_clicked)

        # Line Edit connections
        line_edit_list = [self.tag_line_edit, self.pattern_line_edit, self.response_line_edit, self.filename_line_edit]
        for line_edit in line_edit_list:
            line_edit.returnPressed.connect(self.line_edit_return_pressed)


    # if delete is pressed, delete selected item
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            if self.tag_list.hasFocus():
                self.delete_tag()

    def delete_tag(self):
        tag = self.tag_list.currentItem().text()
        self.tag_list.takeItem(self.tag_list.currentRow())
        print(self.dictionary)


    # Button functions
    def button_clicked(self):
        button = self.sender()
        if button.text() == "Save":
            if self.filename_line_edit.text().endswith(".json"):
                jmaker.export_json(self.dictionary, self.filename_line_edit.text())
            else:
                raise Exception("Wrong file extension")

        elif button.text() == "Load":
            if self.filename_line_edit.text().endswith(".json"):
                self.dictionary = jmaker.import_json(self.filename_line_edit.text())
            else:
                raise Exception("Wrong file extension")

        elif button.text() == "Clear":
            self.dictionary = jmaker.new_json()
            self.tag_list.clear()
            self.pattern_list.clear()
            self.response_list.clear()

        elif button.text() == "Exit":
            self.exit()

    # List functions
    def list_clicked(self):
        list = self.sender()
        if list == self.tag_list:
            self.tag_line_edit.setText(list.currentItem().text())
        elif list == self.pattern_list:
            self.pattern_line_edit.setText(list.currentItem().text())
        elif list == self.response_list:
            self.response_line_edit.setText(list.currentItem().text())

    # Line Edit functions
    def line_edit_return_pressed(self):
        line_edit = self.sender()
        if line_edit == self.tag_line_edit:
            self.tag_list.addItem(line_edit.text())
            self.dictionary = jmaker.add_tag(self.dictionary, line_edit.text())
            print("tag")
        elif line_edit == self.pattern_line_edit:
            self.pattern_list.addItem(line_edit.text())
            self.dictionary = jmaker.add_pattern(self.dictionary, self.tag_line_edit.text(), line_edit.text())
            print("pattern")
        elif line_edit == self.response_line_edit:
            self.response_list.addItem(line_edit.text())
            print("response")

#Main
myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()