###
# 
#  开始考试窗口
#
###

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFrame, QPushButton, QCheckBox
import random
import datetime
import cv2

from ui import answer_exam_window

from exams_io import ExamIO
from face import face_id
from question import Question
from error_shower import error_shower

class AnswerExamWindow(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.main_ui = answer_exam_window.Ui_answer_exam_window()
        self.main_ui.setupUi(self)
        self._parent_window = parent

        # 初始化界面
        self.option_frame_list: list[QFrame] = [
            self.main_ui.option1_frame,
            self.main_ui.option2_frame,
            self.main_ui.option3_frame,
            self.main_ui.option4_frame,
            self.main_ui.option5_frame,
            self.main_ui.option6_frame,
        ]
        self.option_button_list: list[QPushButton] = [
            self.main_ui.option_button_1,
            self.main_ui.option_button_2,
            self.main_ui.option_button_3,
            self.main_ui.option_button_4,
            self.main_ui.option_button_5,
            self.main_ui.option_button_6
        ]
        self.option_check_box_list: list[QCheckBox] = [
            self.main_ui.option1_check_box,
            self.main_ui.option2_check_box,
            self.main_ui.option3_check_box,
            self.main_ui.option4_check_box,
            self.main_ui.option5_check_box,
            self.main_ui.option6_check_box
        ]
        for option_frame in self.option_frame_list:
            option_frame.hide()

        # 初始化数据库读取器
        self.exam_io = ExamIO()

        # 绑定事件
        self.main_ui.next_question_button.clicked.connect(lambda: self.next_page_click())
        self.main_ui.last_question_button.clicked.connect(lambda: self.last_page_click())
        self.main_ui.submit_exam_button.clicked.connect(lambda: self.submit_exam_click())
        self.option_button_list[0].clicked.connect(lambda: self.change_check_box(0))
        self.option_button_list[1].clicked.connect(lambda: self.change_check_box(1))
        self.option_button_list[2].clicked.connect(lambda: self.change_check_box(2))
        self.option_button_list[3].clicked.connect(lambda: self.change_check_box(3))
        self.option_button_list[4].clicked.connect(lambda: self.change_check_box(4))
        self.option_button_list[5].clicked.connect(lambda: self.change_check_box(5))

        # 人脸检测
        self.face_detect = face_id.FaceDetector()

        self.setObjectName("AnswerWin")
        self.setStyleSheet("#AnswerWin{border-image:url(images/background.jpg)}")

        self.setWindowIcon(QtGui.QIcon('ico.ico'))

    # 初始化考试界面
    def init_exam(self, exam_id):
        self.exam_id = exam_id
        exam_info = self.exam_io.get_exam_info_by_id(exam_id)
        self.main_ui.exam_name_label.setText(exam_info[0])
        self.end_time = datetime.datetime.now() + datetime.timedelta(minutes=exam_info[3])
        self.main_ui.remaining_label.setText(str(exam_info[3]) + ":00")

        self.questions: list[Question] = []
        questions_info = self.exam_io.get_all_questions(self.exam_id)
        if not error_shower(self, questions_info):
            return
        for idx in range(len(questions_info)):
            question = Question(questions_info[idx][1])
            question.question_id = questions_info[idx][0]
            for idx2 in range(len(question.options)):
                question.options[idx2].name = questions_info[idx][idx2 * 2 + 2]
            self.questions.append(question)

        if exam_info[4] == 0:
            self.questions = random.sample(self.questions, exam_info[5])
        elif exam_info[5] == 1:
            random.shuffle(self.questions)

        # 页码
        self.page_num = 1
        
        self.fresh_page()
        self.show_camera()

    # 改变check_box
    def change_check_box(self, id: int):
        self.option_check_box_list[id].setCheckState(not self.option_check_box_list[id].checkState())

    # 上一页翻页
    def last_page_click(self):
        self.save_check()
        self.page_num -= 1
        self.fresh_page()

    # 下一页翻页
    def next_page_click(self):
        self.save_check()
        self.page_num += 1
        self.fresh_page()

    # 刷新界面
    def fresh_page(self):
        self.main_ui.page_label.setText("{}/{}".format(self.page_num, len(self.questions)))
        
        self.main_ui.last_question_button.setEnabled(False if self.page_num == 1 else True)
        self.main_ui.next_question_button.setEnabled(False if self.page_num == len(self.questions) else True)

        self.main_ui.question_name_label.setText(self.questions[self.page_num - 1].name)
        for idx in range(len(self.questions[self.page_num - 1].options)):
            if self.questions[self.page_num - 1].options[idx].name == "" or self.questions[self.page_num - 1].options[idx].name is None:
                self.option_frame_list[idx].hide()
                continue
            self.option_frame_list[idx].show()
            self.option_button_list[idx].setText(self.questions[self.page_num - 1].options[idx].name)
            self.option_check_box_list[idx].setCheckState(self.questions[self.page_num - 1].options[idx].isCorrect)

    # 保存选择
    def save_check(self):
        for idx in range(len(self.questions)):
            self.questions[self.page_num - 1].options[idx].isCorrect = self.option_check_box_list[idx].checkState()

    # 交卷按钮点击
    def submit_exam_click(self):
        ret = QMessageBox.question(self, '警告', '你确定要交卷吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.No:
            return
        self.submit_exam()

    # 交卷
    def submit_exam(self):
        self.save_check()
        self.exam_io.submit_exam(self.exam_id, self.questions, self._parent_window.number)
        self._parent_window.show()
        self._parent_window.fresh_page()
        self.cap.release()
        self.cap = None
        self.destroy()

    # 显示图像和计时器
    def show_camera(self):
        try:
            self.cap = cv2.VideoCapture(0)
        except:
            QMessageBox.warning(self, "警告", "无摄像头权限！", QMessageBox.Cancel)
            self.destroy()
            return "faith"
        
        exceptions_cnt = 0
        fatal_exceptions_cnt = 0
        while True:

            if self.cap is None:
                return

            ret, frame = self.cap.read()
            if not ret:
                QMessageBox.warning(self, "警告", "无摄像头权限！", QMessageBox.Cancel)
                fatal_exceptions_cnt += 1
            else:
                if not self.face_detect.detect_face(frame):
                    exceptions_cnt += 1
                    if exceptions_cnt >= 30:
                        QMessageBox.warning(self, "警告", "摄像头异常！", QMessageBox.Cancel)
                        exceptions_cnt = 0
                        fatal_exceptions_cnt += 1
                else:
                    exceptions_cnt = 0
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (320, 240))
                qt_frame = QtGui.QImage(
                    frame.data,
                    frame.shape[1],
                    frame.shape[0],
                    frame.shape[1] * 3,
                    QtGui.QImage.Format_RGB888)
                self.main_ui.camera_label.setPixmap(QtGui.QPixmap(qt_frame))
            
            # 异常过多强制交卷
            if fatal_exceptions_cnt >= 5:
                QMessageBox.warning(self, "警告", "异常次数过多，已强制交卷！", QMessageBox.Cancel)
                self.submit_exam()
                return

            # 计算考试时间
            remaining_time = self.end_time - datetime.datetime.now()
            if remaining_time.seconds <= 0:
                QMessageBox.warning(self, "警告", "时间结束，已强制交卷！", QMessageBox.Cancel)
                self.submit_exam()
                return
            self.main_ui.remaining_label.setText(f"{remaining_time.seconds // 60}:{remaining_time.seconds % 60}")
            cv2.waitKey(1)

    # 退出则强制交卷
    def closeEvent(self, a0) -> None:
        self.submit_exam()
        return super().closeEvent(a0)