# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_exam_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_create_exam_window(object):
    def setupUi(self, create_exam_window):
        create_exam_window.setObjectName("create_exam_window")
        create_exam_window.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(create_exam_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.exam_name_input = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exam_name_input.sizePolicy().hasHeightForWidth())
        self.exam_name_input.setSizePolicy(sizePolicy)
        self.exam_name_input.setObjectName("exam_name_input")
        self.horizontalLayout.addWidget(self.exam_name_input)
        self.delete_exam_button = QtWidgets.QPushButton(self.frame)
        self.delete_exam_button.setObjectName("delete_exam_button")
        self.horizontalLayout.addWidget(self.delete_exam_button)
        self.save_exam_button = QtWidgets.QPushButton(self.frame)
        self.save_exam_button.setObjectName("save_exam_button")
        self.horizontalLayout.addWidget(self.save_exam_button)
        self.release_exam_button = QtWidgets.QPushButton(self.frame)
        self.release_exam_button.setObjectName("release_exam_button")
        self.horizontalLayout.addWidget(self.release_exam_button)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.questions_num_label = QtWidgets.QLabel(self.frame_5)
        self.questions_num_label.setObjectName("questions_num_label")
        self.horizontalLayout_3.addWidget(self.questions_num_label)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_18 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_2 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_17.addWidget(self.label_2)
        self.start_time_editor = QtWidgets.QDateTimeEdit(self.frame_18)
        self.start_time_editor.setObjectName("start_time_editor")
        self.horizontalLayout_17.addWidget(self.start_time_editor)
        self.verticalLayout_2.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_3 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_18.addWidget(self.label_3)
        self.end_time_editor = QtWidgets.QDateTimeEdit(self.frame_19)
        self.end_time_editor.setObjectName("end_time_editor")
        self.horizontalLayout_18.addWidget(self.end_time_editor)
        self.verticalLayout_2.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_19.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_10 = QtWidgets.QLabel(self.frame_20)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_19.addWidget(self.label_10)
        self.exam_time_editor = QtWidgets.QSpinBox(self.frame_20)
        self.exam_time_editor.setMinimum(1)
        self.exam_time_editor.setMaximum(1440)
        self.exam_time_editor.setObjectName("exam_time_editor")
        self.horizontalLayout_19.addWidget(self.exam_time_editor)
        self.verticalLayout_2.addWidget(self.frame_20)
        self.frame_15 = QtWidgets.QFrame(self.frame_3)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_15.setSpacing(3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_5 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_15.addWidget(self.label_5)
        self.exam_mode_combo_box = QtWidgets.QComboBox(self.frame_15)
        self.exam_mode_combo_box.setObjectName("exam_mode_combo_box")
        self.exam_mode_combo_box.addItem("")
        self.exam_mode_combo_box.addItem("")
        self.horizontalLayout_15.addWidget(self.exam_mode_combo_box)
        self.verticalLayout_2.addWidget(self.frame_15)
        self.random_exam_frame = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.random_exam_frame.sizePolicy().hasHeightForWidth())
        self.random_exam_frame.setSizePolicy(sizePolicy)
        self.random_exam_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.random_exam_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.random_exam_frame.setObjectName("random_exam_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.random_exam_frame)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.random_exam_frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.get_questions_num_input = QtWidgets.QSpinBox(self.random_exam_frame)
        self.get_questions_num_input.setMinimum(1)
        self.get_questions_num_input.setMaximum(100)
        self.get_questions_num_input.setObjectName("get_questions_num_input")
        self.horizontalLayout_4.addWidget(self.get_questions_num_input)
        self.verticalLayout_2.addWidget(self.random_exam_frame)
        self.fixed_mode_frame = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixed_mode_frame.sizePolicy().hasHeightForWidth())
        self.fixed_mode_frame.setSizePolicy(sizePolicy)
        self.fixed_mode_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fixed_mode_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fixed_mode_frame.setObjectName("fixed_mode_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fixed_mode_frame)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_16 = QtWidgets.QFrame(self.fixed_mode_frame)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_5.addWidget(self.frame_16)
        self.is_random_box = QtWidgets.QCheckBox(self.fixed_mode_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_random_box.sizePolicy().hasHeightForWidth())
        self.is_random_box.setSizePolicy(sizePolicy)
        self.is_random_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.is_random_box.setAutoFillBackground(False)
        self.is_random_box.setObjectName("is_random_box")
        self.horizontalLayout_5.addWidget(self.is_random_box)
        self.frame_17 = QtWidgets.QFrame(self.fixed_mode_frame)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_5.addWidget(self.frame_17)
        self.verticalLayout_2.addWidget(self.fixed_mode_frame)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.classes_combo_box = QtWidgets.QComboBox(self.frame_9)
        self.classes_combo_box.setObjectName("classes_combo_box")
        self.horizontalLayout_6.addWidget(self.classes_combo_box)
        self.insert_class_button = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insert_class_button.sizePolicy().hasHeightForWidth())
        self.insert_class_button.setSizePolicy(sizePolicy)
        self.insert_class_button.setObjectName("insert_class_button")
        self.horizontalLayout_6.addWidget(self.insert_class_button)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.show_selected_classes_input = QtWidgets.QTextEdit(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_selected_classes_input.sizePolicy().hasHeightForWidth())
        self.show_selected_classes_input.setSizePolicy(sizePolicy)
        self.show_selected_classes_input.setObjectName("show_selected_classes_input")
        self.verticalLayout_5.addWidget(self.show_selected_classes_input)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.question_name_input = QtWidgets.QTextEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_name_input.sizePolicy().hasHeightForWidth())
        self.question_name_input.setSizePolicy(sizePolicy)
        self.question_name_input.setObjectName("question_name_input")
        self.horizontalLayout_8.addWidget(self.question_name_input)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.option1_frame = QtWidgets.QFrame(self.frame_4)
        self.option1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option1_frame.setObjectName("option1_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.option1_frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.option1_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.option1_name_input = QtWidgets.QLineEdit(self.option1_frame)
        self.option1_name_input.setObjectName("option1_name_input")
        self.horizontalLayout_9.addWidget(self.option1_name_input)
        self.option1_check_box = QtWidgets.QCheckBox(self.option1_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option1_check_box.setFont(font)
        self.option1_check_box.setObjectName("option1_check_box")
        self.horizontalLayout_9.addWidget(self.option1_check_box)
        self.verticalLayout_6.addWidget(self.option1_frame)
        self.option2_frame = QtWidgets.QFrame(self.frame_4)
        self.option2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option2_frame.setObjectName("option2_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.option2_frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.option2_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.option2_name_input = QtWidgets.QLineEdit(self.option2_frame)
        self.option2_name_input.setObjectName("option2_name_input")
        self.horizontalLayout_11.addWidget(self.option2_name_input)
        self.option2_check_box = QtWidgets.QCheckBox(self.option2_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option2_check_box.setFont(font)
        self.option2_check_box.setObjectName("option2_check_box")
        self.horizontalLayout_11.addWidget(self.option2_check_box)
        self.verticalLayout_6.addWidget(self.option2_frame)
        self.option3_frame = QtWidgets.QFrame(self.frame_4)
        self.option3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option3_frame.setObjectName("option3_frame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.option3_frame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.option3_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.option3_name_input = QtWidgets.QLineEdit(self.option3_frame)
        self.option3_name_input.setObjectName("option3_name_input")
        self.horizontalLayout_12.addWidget(self.option3_name_input)
        self.option3_check_box = QtWidgets.QCheckBox(self.option3_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option3_check_box.setFont(font)
        self.option3_check_box.setObjectName("option3_check_box")
        self.horizontalLayout_12.addWidget(self.option3_check_box)
        self.verticalLayout_6.addWidget(self.option3_frame)
        self.option4_frame = QtWidgets.QFrame(self.frame_4)
        self.option4_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option4_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option4_frame.setObjectName("option4_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.option4_frame)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.option4_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.option4_name_input = QtWidgets.QLineEdit(self.option4_frame)
        self.option4_name_input.setObjectName("option4_name_input")
        self.horizontalLayout_13.addWidget(self.option4_name_input)
        self.option4_check_box = QtWidgets.QCheckBox(self.option4_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option4_check_box.setFont(font)
        self.option4_check_box.setObjectName("option4_check_box")
        self.horizontalLayout_13.addWidget(self.option4_check_box)
        self.verticalLayout_6.addWidget(self.option4_frame)
        self.option5_frame = QtWidgets.QFrame(self.frame_4)
        self.option5_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option5_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option5_frame.setObjectName("option5_frame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.option5_frame)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.option5_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        self.option5_name_input = QtWidgets.QLineEdit(self.option5_frame)
        self.option5_name_input.setObjectName("option5_name_input")
        self.horizontalLayout_14.addWidget(self.option5_name_input)
        self.option5_check_box = QtWidgets.QCheckBox(self.option5_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option5_check_box.setFont(font)
        self.option5_check_box.setObjectName("option5_check_box")
        self.horizontalLayout_14.addWidget(self.option5_check_box)
        self.verticalLayout_6.addWidget(self.option5_frame)
        self.option6_frame = QtWidgets.QFrame(self.frame_4)
        self.option6_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option6_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option6_frame.setObjectName("option6_frame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.option6_frame)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.option6_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.option6_name_input = QtWidgets.QLineEdit(self.option6_frame)
        self.option6_name_input.setObjectName("option6_name_input")
        self.horizontalLayout_16.addWidget(self.option6_name_input)
        self.option6_check_box = QtWidgets.QCheckBox(self.option6_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.option6_check_box.setFont(font)
        self.option6_check_box.setObjectName("option6_check_box")
        self.horizontalLayout_16.addWidget(self.option6_check_box)
        self.verticalLayout_6.addWidget(self.option6_frame)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10.addWidget(self.frame_13)
        self.page_label = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_label.sizePolicy().hasHeightForWidth())
        self.page_label.setSizePolicy(sizePolicy)
        self.page_label.setObjectName("page_label")
        self.horizontalLayout_10.addWidget(self.page_label)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_10.addWidget(self.frame_14)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.last_question_button = QtWidgets.QPushButton(self.frame_8)
        self.last_question_button.setObjectName("last_question_button")
        self.horizontalLayout_7.addWidget(self.last_question_button)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7.addWidget(self.frame_10)
        self.delete_question_button = QtWidgets.QPushButton(self.frame_8)
        self.delete_question_button.setObjectName("delete_question_button")
        self.horizontalLayout_7.addWidget(self.delete_question_button)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7.addWidget(self.frame_11)
        self.next_question_button = QtWidgets.QPushButton(self.frame_8)
        self.next_question_button.setObjectName("next_question_button")
        self.horizontalLayout_7.addWidget(self.next_question_button)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        create_exam_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(create_exam_window)
        self.statusbar.setObjectName("statusbar")
        create_exam_window.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(create_exam_window)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(create_exam_window)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(create_exam_window)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(create_exam_window)
        self.action_5.setObjectName("action_5")
        self.action_7 = QtWidgets.QAction(create_exam_window)
        self.action_7.setObjectName("action_7")

        self.retranslateUi(create_exam_window)
        QtCore.QMetaObject.connectSlotsByName(create_exam_window)

    def retranslateUi(self, create_exam_window):
        _translate = QtCore.QCoreApplication.translate
        create_exam_window.setWindowTitle(_translate("create_exam_window", "创建考试"))
        self.label.setText(_translate("create_exam_window", "考试名称："))
        self.delete_exam_button.setText(_translate("create_exam_window", "删除试卷"))
        self.save_exam_button.setText(_translate("create_exam_window", "保存试卷"))
        self.release_exam_button.setText(_translate("create_exam_window", "发布试卷"))
        self.label_4.setText(_translate("create_exam_window", "题目数量："))
        self.questions_num_label.setText(_translate("create_exam_window", "0"))
        self.label_2.setText(_translate("create_exam_window", "开始时间："))
        self.label_3.setText(_translate("create_exam_window", "截止时间："))
        self.label_10.setText(_translate("create_exam_window", "考试时间（分钟）："))
        self.label_5.setText(_translate("create_exam_window", "考试模式："))
        self.exam_mode_combo_box.setItemText(0, _translate("create_exam_window", "随机抽题"))
        self.exam_mode_combo_box.setItemText(1, _translate("create_exam_window", "所有题目"))
        self.label_6.setText(_translate("create_exam_window", "抽题数量："))
        self.is_random_box.setText(_translate("create_exam_window", "随机顺序"))
        self.label_7.setText(_translate("create_exam_window", "参与的班级："))
        self.insert_class_button.setText(_translate("create_exam_window", "添加"))
        self.label_8.setText(_translate("create_exam_window", "题目："))
        self.label_9.setText(_translate("create_exam_window", "选项1:"))
        self.option1_check_box.setText(_translate("create_exam_window", "正确选项"))
        self.label_11.setText(_translate("create_exam_window", "选项2:"))
        self.option2_check_box.setText(_translate("create_exam_window", "正确选项"))
        self.label_12.setText(_translate("create_exam_window", "选项3:"))
        self.option3_check_box.setText(_translate("create_exam_window", "正确选项"))
        self.label_13.setText(_translate("create_exam_window", "选项4:"))
        self.option4_check_box.setText(_translate("create_exam_window", "正确选项"))
        self.label_14.setText(_translate("create_exam_window", "选项5:"))
        self.option5_check_box.setText(_translate("create_exam_window", "正确选项"))
        self.label_16.setText(_translate("create_exam_window", "选项6:"))
        self.option6_check_box.setText(_translate("create_exam_window", "正确选项"))
        self.page_label.setText(_translate("create_exam_window", "1/1"))
        self.last_question_button.setText(_translate("create_exam_window", "上一题"))
        self.delete_question_button.setText(_translate("create_exam_window", "删除题目"))
        self.next_question_button.setText(_translate("create_exam_window", "下一题"))
        self.action.setText(_translate("create_exam_window", "新建"))
        self.action.setShortcut(_translate("create_exam_window", "Ctrl+N"))
        self.action_2.setText(_translate("create_exam_window", "打开"))
        self.action_2.setShortcut(_translate("create_exam_window", "Ctrl+O"))
        self.action_4.setText(_translate("create_exam_window", "保存"))
        self.action_4.setShortcut(_translate("create_exam_window", "Ctrl+S"))
        self.action_5.setText(_translate("create_exam_window", "另存为"))
        self.action_5.setShortcut(_translate("create_exam_window", "Ctrl+Shift+S"))
        self.action_7.setText(_translate("create_exam_window", "退出"))
