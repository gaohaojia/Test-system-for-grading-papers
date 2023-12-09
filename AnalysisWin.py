###
# 
#  考试创建窗口
#
###

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFrame, QLineEdit, QCheckBox
import matplotlib.pyplot as plt
import cv2

from ui import analysis_window

from info_io import InfoIO
from exams_io import ExamIO
from question import Question
from error_shower import error_shower

class AnalysisWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = analysis_window.Ui_analysis_window()
        self.main_ui.setupUi(self)

       # 初始化数据库读取器
        self.exam_io = ExamIO()

        # 绑定事件
        self.main_ui.next_question_button.clicked.connect(lambda: self.next_page_click())
        self.main_ui.last_question_button.clicked.connect(lambda: self.last_page_click())

        self.setObjectName("AnalysisWin")
        self.setStyleSheet("#AnalysisWin{border-image:url(images/background.jpg)}")

        self.setWindowIcon(QtGui.QIcon('ico.ico'))

    # 初始化考试界面
    def init_exam(self, exam_id):
        self.exam_id = exam_id
        exam_info = self.exam_io.get_exam_info_by_id(exam_id)
        self.main_ui.exam_name_label.setText(exam_info[0])

        self.questions: list[Question] = []
        questions_info = self.exam_io.get_all_questions(self.exam_id)
        if not error_shower(self, questions_info):
            return
        for idx in range(len(questions_info)):
            question = Question(questions_info[idx][1])
            question.question_id = questions_info[idx][0]
            for idx2 in range(len(question.options)):
                question.options[idx2].name = questions_info[idx][idx2 * 2 + 2]
                question.options[idx2].isCorrect = True if questions_info[idx][idx2 * 2 + 3] == 1 else False
            self.questions.append(question)

        # 计算正确题目
        correct_list = []
        for question in self.questions:
            correct = []
            for option in question.options:
                correct.append(1 if option.isCorrect else 0)
            correct_list.append(correct)
        
        # 获取所有提交试卷信息
        self.all_submitted_list = self.exam_io.get_all_submitted(self.exam_id)
        if not error_shower(self, self.all_submitted_list):
            self.destroy()
            return
        
        # 计算分数
        self.all_submitted_list = [submitted[1:] for submitted in self.all_submitted_list]
        cache = []
        for submitted in self.all_submitted_list:
            option_cache = []
            for option in submitted:
                if option is None:
                    option_cache.append(None)
                else:
                    option_cache.append([int(a) for a in option.split(",")])
            cache.append(option_cache)
        self.all_submitted_list = cache
        self.all_score_list = []
        for submitted in self.all_submitted_list:
            score_list = []
            for idx in range(len(self.questions)):
                if submitted[idx] is None:
                    continue
                score_list.append(1 if submitted[idx] == correct_list[idx] else 0)
            self.all_score_list.append(score_list)
        
        self.main_ui.average_score_label.setText(str(0 if len(self.all_score_list) == 0 else sum([sum(score) for score in self.all_score_list]) / (len(self.all_score_list) * len(self.all_score_list[0]))))
        self.main_ui.submitted_count_label.setText(str(len(self.all_score_list)))

        # 页码
        self.page_num = 1
        
        self.fresh_page()

    # 上一页翻页
    def last_page_click(self):
        self.page_num -= 1
        self.fresh_page()

    # 下一页翻页
    def next_page_click(self):
        self.page_num += 1
        self.fresh_page()

    # 刷新界面
    def fresh_page(self):
        self.main_ui.page_label.setText("{}/{}".format(self.page_num, len(self.questions)))
        
        self.main_ui.last_question_button.setEnabled(False if self.page_num == 1 else True)
        self.main_ui.next_question_button.setEnabled(False if self.page_num == len(self.questions) else True)

        self.main_ui.question_name_label.setText(self.questions[self.page_num - 1].name)

        # 显示数据分析
        A_cnt = sum([0 if submitted[self.page_num - 1] is None else submitted[self.page_num - 1][0] for submitted in self.all_submitted_list])
        B_cnt = sum([0 if submitted[self.page_num - 1] is None else submitted[self.page_num - 1][1] for submitted in self.all_submitted_list])
        C_cnt = sum([0 if submitted[self.page_num - 1] is None else submitted[self.page_num - 1][2] for submitted in self.all_submitted_list])
        D_cnt = sum([0 if submitted[self.page_num - 1] is None else submitted[self.page_num - 1][3] for submitted in self.all_submitted_list])
        E_cnt = sum([0 if submitted[self.page_num - 1] is None else submitted[self.page_num - 1][4] for submitted in self.all_submitted_list])
        F_cnt = sum([0 if submitted[self.page_num - 1] is None else submitted[self.page_num - 1][5] for submitted in self.all_submitted_list])

        if [A_cnt, B_cnt, C_cnt, D_cnt, E_cnt, F_cnt] == [0, 0, 0, 0, 0, 0]:
            self.main_ui.image_label.clear()
            self.main_ui.image_label.setText("暂无数据！")
            return
        else:
            self.main_ui.image_label.setText("")

        plt.clf()
        plt.bar(['A', 'B', 'C', 'D', 'E', 'F'], [A_cnt, B_cnt, C_cnt, D_cnt, E_cnt, F_cnt])
 
        plt.title("data analysis")
        plt.xlabel("option")
        plt.ylabel("count")
        
        plt.savefig("cache.png")
        frame = cv2.imread("cache.png")
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qt_frame = QtGui.QImage(
            frame.data,
            frame.shape[1],
            frame.shape[0],
            frame.shape[1] * 3,
            QtGui.QImage.Format_RGB888)
        self.main_ui.image_label.setPixmap(QtGui.QPixmap(qt_frame))