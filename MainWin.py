###
# 
#  主窗口
#
###
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFrame, QLabel, QPushButton, QGraphicsOpacityEffect
import datetime

from ui import main_window

from CreateExamWin import CreateExamWindow
from AnswerExamWin import AnswerExamWindow
from SignInWin import SignInWindow
from FaceIDWin import FaceIDWindow
from AnalysisWin import AnalysisWindow
from exams_io import ExamIO
from error_shower import error_shower

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = main_window.Ui_main_window()
        self.main_ui.setupUi(self)

        # 参数
        self.isLogin = False

        # 将组件保存在list里
        self.exam_frame_list: list[QFrame] = [
            self.main_ui.exam_1,
            self.main_ui.exam_2,
            self.main_ui.exam_3,
            self.main_ui.exam_4,
            self.main_ui.exam_5,
            self.main_ui.exam_6,
            self.main_ui.exam_7,
            self.main_ui.exam_8,
            self.main_ui.exam_9,
            self.main_ui.exam_10,
            self.main_ui.exam_11,
            self.main_ui.exam_12,
            self.main_ui.exam_13,
            self.main_ui.exam_14,
            self.main_ui.exam_15]
        self.exam_name_label_list: list[QLabel] = [
            self.main_ui.exam_name_1,
            self.main_ui.exam_name_2,
            self.main_ui.exam_name_3,
            self.main_ui.exam_name_4,
            self.main_ui.exam_name_5,
            self.main_ui.exam_name_6,
            self.main_ui.exam_name_7,
            self.main_ui.exam_name_8,
            self.main_ui.exam_name_9,
            self.main_ui.exam_name_10,
            self.main_ui.exam_name_11,
            self.main_ui.exam_name_12,
            self.main_ui.exam_name_13,
            self.main_ui.exam_name_14,
            self.main_ui.exam_name_15]
        self.exam_start_time_label_list: list[QLabel] = [
            self.main_ui.start_time_1,
            self.main_ui.start_time_2,
            self.main_ui.start_time_3,
            self.main_ui.start_time_4,
            self.main_ui.start_time_5,
            self.main_ui.start_time_6,
            self.main_ui.start_time_7,
            self.main_ui.start_time_8,
            self.main_ui.start_time_9,
            self.main_ui.start_time_10,
            self.main_ui.start_time_11,
            self.main_ui.start_time_12,
            self.main_ui.start_time_13,
            self.main_ui.start_time_14,
            self.main_ui.start_time_15]
        self.exam_end_time_label_list: list[QLabel] = [
            self.main_ui.end_time_1,
            self.main_ui.end_time_2,
            self.main_ui.end_time_3,
            self.main_ui.end_time_4,
            self.main_ui.end_time_5,
            self.main_ui.end_time_6,
            self.main_ui.end_time_7,
            self.main_ui.end_time_8,
            self.main_ui.end_time_9,
            self.main_ui.end_time_10,
            self.main_ui.end_time_11,
            self.main_ui.end_time_12,
            self.main_ui.end_time_13,
            self.main_ui.end_time_14,
            self.main_ui.end_time_15]
        self.exam_start_button_list: list[QPushButton] =[
            self.main_ui.start_exam_button_1,
            self.main_ui.start_exam_button_2,
            self.main_ui.start_exam_button_3,
            self.main_ui.start_exam_button_4,
            self.main_ui.start_exam_button_5,
            self.main_ui.start_exam_button_6,
            self.main_ui.start_exam_button_7,
            self.main_ui.start_exam_button_8,
            self.main_ui.start_exam_button_9,
            self.main_ui.start_exam_button_10,
            self.main_ui.start_exam_button_11,
            self.main_ui.start_exam_button_12,
            self.main_ui.start_exam_button_13,
            self.main_ui.start_exam_button_14,
            self.main_ui.start_exam_button_15]
        
        # 初始化界面
        for exam_frame in self.exam_frame_list:
            exam_frame.setFrameShadow(QFrame.Sunken)
            exam_frame.setStyleSheet("background-color:white")
            exam_frame.hide()
        self.main_ui.create_exam.hide()

        # 创建按钮点击事件
        self.main_ui.sign_out.clicked.connect(lambda: self.sign_in()) # 退出登录按钮
        self.main_ui.create_exam.clicked.connect(lambda: self.create_exam()) # 创建考试按钮

        self.exam_start_button_list[0].clicked.connect(lambda: self.start_exam_button_click(0))
        self.exam_start_button_list[1].clicked.connect(lambda: self.start_exam_button_click(1))
        self.exam_start_button_list[2].clicked.connect(lambda: self.start_exam_button_click(2))
        self.exam_start_button_list[3].clicked.connect(lambda: self.start_exam_button_click(3))
        self.exam_start_button_list[4].clicked.connect(lambda: self.start_exam_button_click(4))
        self.exam_start_button_list[5].clicked.connect(lambda: self.start_exam_button_click(5))
        self.exam_start_button_list[6].clicked.connect(lambda: self.start_exam_button_click(6))
        self.exam_start_button_list[7].clicked.connect(lambda: self.start_exam_button_click(7))
        self.exam_start_button_list[8].clicked.connect(lambda: self.start_exam_button_click(8))
        self.exam_start_button_list[9].clicked.connect(lambda: self.start_exam_button_click(9))
        self.exam_start_button_list[10].clicked.connect(lambda: self.start_exam_button_click(10))
        self.exam_start_button_list[11].clicked.connect(lambda: self.start_exam_button_click(11))
        self.exam_start_button_list[12].clicked.connect(lambda: self.start_exam_button_click(12))
        self.exam_start_button_list[13].clicked.connect(lambda: self.start_exam_button_click(13))
        self.exam_start_button_list[14].clicked.connect(lambda: self.start_exam_button_click(14))

        # 初始化登录窗口
        self._sign_in_window = SignInWindow(self)

        # 初始化创建考试窗口
        self._create_exam_window = CreateExamWindow(self)

        # 初始化人脸识别窗口
        self._face_id_window = FaceIDWindow()

        # 初始化答题窗口
        self._answer_exam_window = AnswerExamWindow(self)

        # 初始化分析窗口
        self._analysis_window = AnalysisWindow()

        # # 初始化数据库读取器
        self.exam_io = ExamIO()

        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/background.jpg)}")

        self.setWindowIcon(QIcon('ico.ico'))
    
    # 弹出登录窗口
    def sign_in(self):
        # 初始化界面
        self._sign_in_window.main_ui.Student_QRadio.click()
        self._sign_in_window.main_ui.account_Inputer.setText("")
        self._sign_in_window.main_ui.Password_Inputer.setText("")
        self._sign_in_window.show()
        self.hide()
    
    # 完成登录
    def finish_sign_in(self, user_type, account, number, name, class_number):
        self.main_ui.account_label.setText(account)
        self.main_ui.user_type.setText("学生" if user_type == 2 else "老师")
        self.main_ui.name_label.setText(name)
        self.isLogin = True
        self.user_type = user_type
        self.account = account
        self.number = number
        self.class_number = class_number
        self.page_num = 1
        self.fresh_page()
        self.show()

    # 弹出创建考试窗口
    def create_exam(self, exam_id = None):
        self._create_exam_window.show()
        self._create_exam_window.teacher_number = self.number
        self._create_exam_window.main_ui.release_exam_button.setText("发布试卷")
        self._create_exam_window.main_ui.release_exam_button.setEnabled(True)
        if not exam_id is None:
            self._create_exam_window.exam_id = exam_id
            info = self.exam_io.get_exam_info_by_id(exam_id)
            if not error_shower(self, info):
                return
            self._create_exam_window.main_ui.exam_name_input.setText(info[0])
            self._create_exam_window.main_ui.start_time_editor.setDateTime(info[1])
            self._create_exam_window.main_ui.end_time_editor.setDateTime(info[2])
            self._create_exam_window.main_ui.exam_time_editor.setValue(info[3])
            self._create_exam_window.main_ui.exam_mode_combo_box.setCurrentIndex(info[4])
            if info[4] == 0:
                self._create_exam_window.main_ui.get_questions_num_input.setValue(info[5])
            else:
                self._create_exam_window.main_ui.is_random_box.setCheckState(True if info[5] == 1 else False)
            self._create_exam_window.main_ui.show_selected_classes_input.setText(info[6])
            if info[7] == 1:
                self._create_exam_window.main_ui.release_exam_button.setText("已发布")
                self._create_exam_window.main_ui.release_exam_button.setEnabled(False)
            self._create_exam_window.load_questions()
            self._create_exam_window.read_question()
            self._create_exam_window.save_question()

    # 点击开始考试按钮
    def start_exam_button_click(self, id):
        
        # 判断用户类型
        if self.user_type == 1:
            info = self.exam_io.get_exam_info_by_id(self.available_id_list[int((self.page_num - 1) * 15 + id)])
            if not error_shower(self, info):
                return
            
            # 判断试卷是否已发布
            if info[7] == 0:
                self.create_exam(self.available_id_list[int((self.page_num - 1) * 15 + id)])
            else:
                self._analysis_window.show()
                self._analysis_window.init_exam(self.available_id_list[int((self.page_num - 1) * 15 + id)])
        else:
            submit_stats = self.exam_io.get_submit_stats(self.available_id_list[int((self.page_num - 1) * 15 + id)], self.number)
            if not error_shower(self, submit_stats):
                return
            
            # 判断试卷是否提交
            if submit_stats == "submitted":
                pass
            else:
                self._face_id_window.show()
                ret = self._face_id_window.start_detect(self.account)
                self._face_id_window.destroy()
                if ret != "success":
                    QMessageBox.warning(self, "警告", "人脸识别异常！请联系管理员。", QMessageBox.Cancel)
                    return
                self._answer_exam_window.showFullScreen()
                self.hide()
                self._answer_exam_window.init_exam(self.available_id_list[int((self.page_num - 1) * 15 + id)])

    # 刷新界面
    def fresh_page(self):
        if self.user_type == 1:
            self.main_ui.create_exam.show()
        else:
            self.main_ui.create_exam.hide()
        self.main_ui.sign_out.setEnabled(True)

        exam_info_list = self.exam_io.get_all_exam_info()
        if not error_shower(self, exam_info_list):
            return
        
        # 查找所有符合要求的试卷
        self.available_id_list = []
        for exam_info in exam_info_list:
            if self.user_type == 2 and self.class_number in exam_info[2].split(",") and exam_info[3] == 1:
                self.available_id_list.append(exam_info[0])
            elif self.user_type == 1 and self.number == exam_info[1]:
                self.available_id_list.append(exam_info[0])
        
        # 判断按钮是否可点击
        max_page = abs(len(self.available_id_list) - 1) / 15 + 1
        if max_page <= self.page_num:
            self.page_num = max_page
            self.main_ui.next_page.setEnabled(False)
        else:
            self.main_ui.next_page.setEnabled(True)

        if self.page_num == 1:
            self.main_ui.last_page.setEnabled(False)
        else:
            self.main_ui.last_page.setEnabled(True)

        # 设置所有考试信息
        for idx in range(int((self.page_num - 1) * 15), int(self.page_num * 15)):
            if idx >= len(self.available_id_list):
                self.exam_frame_list[idx % 15].hide()
                continue
            info = self.exam_io.get_exam_info_by_id(self.available_id_list[idx])
            if not error_shower(self, info):
                return
            self.exam_frame_list[idx % 15].show()
            self.exam_name_label_list[idx % 15].setText(info[0])
            self.exam_start_time_label_list[idx % 15].setText(info[1].strftime('%Y-%m-%d %H:%M:%S'))
            self.exam_end_time_label_list[idx % 15].setText(info[2].strftime('%Y-%m-%d %H:%M:%S'))

            submit_stats = self.exam_io.get_submit_stats(self.available_id_list[idx], self.number)
            if not error_shower(self, submit_stats):
                return

            if self.user_type == 1:
                self.exam_start_button_list[idx % 15].setEnabled(True)
                if info[7] == 0:
                    self.exam_start_button_list[idx % 15].setText("编辑题目")
                else:
                    self.exam_start_button_list[idx % 15].setText("情况分析")
            elif self.user_type == 2:
                if datetime.datetime.now() < info[1]:
                    self.exam_start_button_list[idx % 15].setEnabled(False)
                    self.exam_start_button_list[idx % 15].setText("考试未开始")
                elif submit_stats == "submitted":
                    self.exam_start_button_list[idx % 15].setEnabled(False)
                    self.exam_start_button_list[idx % 15].setText("试卷已提交")
                elif datetime.datetime.now() > info[2]:
                    self.exam_start_button_list[idx % 15].setEnabled(False)
                    self.exam_start_button_list[idx % 15].setText("考试已结束")
                else:
                    self.exam_start_button_list[idx % 15].setEnabled(True)
                    self.exam_start_button_list[idx % 15].setText("开始考试")