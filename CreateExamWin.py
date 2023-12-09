###
# 
#  考试创建窗口
#
###

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFrame, QLineEdit, QCheckBox

from ui import create_exam_window

from info_io import InfoIO
from exams_io import ExamIO
from question import Question
from error_shower import error_shower

class CreateExamWindow(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.main_ui = create_exam_window.Ui_create_exam_window()
        self.main_ui.setupUi(self)
        self._parent_window = parent

        # 初始化界面
        self.option_frame: list[QFrame] = [
            self.main_ui.option1_frame,
            self.main_ui.option2_frame,
            self.main_ui.option3_frame,
            self.main_ui.option4_frame,
            self.main_ui.option5_frame,
            self.main_ui.option6_frame
        ]
        self.option_name: list[QLineEdit] = [
            self.main_ui.option1_name_input,
            self.main_ui.option2_name_input,
            self.main_ui.option3_name_input,
            self.main_ui.option4_name_input,
            self.main_ui.option5_name_input,
            self.main_ui.option6_name_input
        ]
        self.option_check_box: list[QCheckBox] = [
            self.main_ui.option1_check_box,
            self.main_ui.option2_check_box,
            self.main_ui.option3_check_box,
            self.main_ui.option4_check_box,
            self.main_ui.option5_check_box,
            self.main_ui.option6_check_box
        ]
        
        # 绑定事件
        self.main_ui.exam_mode_combo_box.currentIndexChanged.connect(lambda: self.changeModeEvent(self.main_ui.exam_mode_combo_box.currentIndex()))
        self.main_ui.question_name_input.textChanged.connect(lambda: self.changeQuestionNameEvent(self.main_ui.question_name_input.toPlainText()))
        self.main_ui.last_question_button.clicked.connect(lambda: self.last_question_button_clicked())
        self.main_ui.next_question_button.clicked.connect(lambda: self.next_question_button_clicked())
        self.main_ui.save_exam_button.clicked.connect(lambda: self.save_question())
        self.main_ui.delete_question_button.clicked.connect(lambda: self.delete_question())
        self.main_ui.insert_class_button.clicked.connect(lambda: self.insert_class())
        self.main_ui.delete_exam_button.clicked.connect(lambda: self.delete_exam())
        self.main_ui.release_exam_button.clicked.connect(lambda: self.release_exam())
        
        # 初始化数据库读取器
        self.info_io = InfoIO()
        self.exam_io = ExamIO()

        self.setObjectName("CreateWin")
        self.setStyleSheet("#CreateWin{border-image:url(images/background.jpg)}")

        self.setWindowIcon(QtGui.QIcon('ico.ico'))

    # 显示后初始化
    def showEvent(self, a0) -> None:

        ### 初始化
        # 读取所有班级
        all_classes_number = self.info_io.get_classes()
        if not error_shower(self, all_classes_number):
            self.destroy()
        self.main_ui.classes_combo_box.addItems([item[0] for item in all_classes_number])

        # 初始化参数
        self.questions: list[Question] = [] # 每道题
        self.current_question_index: int = 0 # 当前题目索引
        self.exam_id = self.exam_io.get_new_exam_id() # 在数据库中的id
        if not error_shower(self, self.exam_id):
            self.destroy()
        self.teacher_number: str = "" # 老师账户id

        # 设定时间
        self.main_ui.start_time_editor.setDateTime(QtCore.QDateTime.currentDateTime())
        self.main_ui.end_time_editor.setDateTime(QtCore.QDateTime.currentDateTime())

        # 设置最大抽题数量
        self.main_ui.get_questions_num_input.setMinimum(1)
        self.main_ui.get_questions_num_input.setMaximum(0)

        # 隐藏所有题目窗口
        self.main_ui.fixed_mode_frame.hide()
        
        # 初始化按钮可用性
        self.main_ui.last_question_button.setEnabled(False)
        self.main_ui.next_question_button.setEnabled(False)

        # 重置ui
        self.main_ui.show_selected_classes_input.setText("")
        self.main_ui.exam_name_input.setText("")
        self.main_ui.exam_mode_combo_box.setCurrentIndex(0)
        self.main_ui.is_random_box.setCheckState(False)
        self.main_ui.questions_num_label.setText("0")

        return super().showEvent(a0)
    
    # 关闭创建考试窗口并保存数据
    def closeEvent(self, a0) -> None:
        self.save_question()
        self._parent_window.fresh_page()
        return super().closeEvent(a0)
    
    # 上一题按钮事件
    def last_question_button_clicked(self):
        
        # 保存本题内容
        self.save_question()

        # 切换索引
        self.current_question_index -= 1
        if self.current_question_index == 0:
            self.main_ui.last_question_button.setEnabled(False)
        self.main_ui.next_question_button.setEnabled(True)
        self.main_ui.page_label.setText("{}/{}".format(self.current_question_index + 1, len(self.questions)))

        # 读取题目
        self.read_question()
    
    # 下一题按钮事件
    def next_question_button_clicked(self):

        # 保存本题内容
        self.save_question()

        # 切换索引
        self.current_question_index += 1
        if len(self.questions) == self.current_question_index:
            self.main_ui.next_question_button.setEnabled(False)
            self.main_ui.page_label.setText("{}/{}".format(self.current_question_index + 1, len(self.questions) + 1))
        else:
            self.main_ui.page_label.setText("{}/{}".format(self.current_question_index + 1, len(self.questions)))
            
        # 读取题目
        self.read_question()
        self.main_ui.last_question_button.setEnabled(True)
    
    # 保存本题内容
    def save_question(self):

        # 判断是否有题
        if self.main_ui.question_name_input.toPlainText() == "" and self.current_question_index == len(self.questions):
            return
        
        question = Question(self.main_ui.question_name_input.toPlainText(), *[name.text() for name in self.option_name])
        for idx in range(len(self.option_check_box)):
            question.options[idx].isCorrect = self.option_check_box[idx].isChecked()
        if len(self.questions) == self.current_question_index:
            self.questions.append(question)
        else:
            self.questions[self.current_question_index] = question
        
        # 设置抽题数量最大值
        self.main_ui.get_questions_num_input.setMaximum(len(self.questions))
        if len(self.questions) > 0:
            self.main_ui.get_questions_num_input.setMinimum(1)

        # 更新题目数量显示
        self.main_ui.questions_num_label.setText(str(len(self.questions)))

        # 保存进入数据库
        mode_para = int(self.main_ui.get_questions_num_input.text()) if self.main_ui.exam_mode_combo_box.currentIndex() == 0 else 1 if self.main_ui.is_random_box.checkState() else 0
        ret = self.exam_io.write_exam_info(
            self.exam_id, 
            self.teacher_number,
            self.main_ui.exam_name_input.text(), 
            self.main_ui.start_time_editor.dateTime(),
            self.main_ui.end_time_editor.dateTime(),
            self.main_ui.exam_time_editor.value(),
            self.main_ui.exam_mode_combo_box.currentIndex(),
            mode_para,
            self.main_ui.show_selected_classes_input.toPlainText())
        if not error_shower(self, ret):
            return
        ret = self.exam_io.write_exam_table(self.exam_id, self.questions)
        if not error_shower(self, ret):
            return
    
    # 删除题目
    def delete_question(self):
        self.main_ui.question_name_input.setText("")
        for idx in range(len(self.option_name)):
            self.option_name[idx].setText("")
            self.option_check_box[idx].setCheckState(False)
        if len(self.questions) > self.current_question_index:
            del self.questions[self.current_question_index]
        self.read_question()

        # 设置抽题数量最大值
        self.main_ui.get_questions_num_input.setMaximum(len(self.questions))
        if len(self.questions) > 0:
            self.main_ui.get_questions_num_input.setMinimum(1)
        else:
            self.main_ui.get_questions_num_input.setMinimum(0)

        # 更新题目数量显示
        self.main_ui.questions_num_label.setText(str(len(self.questions)))
    
    # 读取题目
    def read_question(self):

        # 判断是否为新题
        if len(self.questions) == self.current_question_index:
            self.main_ui.question_name_input.setText("")
            for idx in range(len(self.option_name)):
                self.option_name[idx].setText("")
                self.option_check_box[idx].setCheckState(False)
            return
        
        # 读取已保存的题
        self.main_ui.question_name_input.setText(self.questions[self.current_question_index].name)
        for idx in range(len(self.questions[self.current_question_index].options)):
            self.option_name[idx].setText(self.questions[self.current_question_index].options[idx].name)
            self.option_check_box[idx].setCheckState(self.questions[self.current_question_index].options[idx].isCorrect)
    
    # 添加班级
    def insert_class(self):
        text = self.main_ui.show_selected_classes_input.toPlainText()
        if text == "":
            self.main_ui.show_selected_classes_input.setText(self.main_ui.classes_combo_box.currentText())
            return
        
        # 判断班级是否已添加
        class_list = text.split(",")
        if not self.main_ui.classes_combo_box.currentText() in class_list:
            self.main_ui.show_selected_classes_input.setText(text + "," + self.main_ui.classes_combo_box.currentText())
        else:
            QMessageBox.warning(self, "警告", "班级已添加！", QMessageBox.Cancel)

    # 从数据库中载入题目
    def load_questions(self):
        self.questions = []
        questions_info = self.exam_io.get_all_questions(self.exam_id)
        if not error_shower(self, questions_info):
            return
        for idx in range(len(questions_info)):
            question = Question(questions_info[idx][1])
            for idx2 in range(len(question.options)):
                question.options[idx2].name = questions_info[idx][idx2 * 2 + 2]
                question.options[idx2].isCorrect = True if questions_info[idx][idx2 * 2 + 3] == 1 else False
            self.questions.append(question)

    # 删除试卷
    def delete_exam(self):
        ret = QMessageBox.question(self, '警告', '你确定要删除吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.No:
            return
        ret = self.exam_io.delete_exam(self.exam_id)
        if not error_shower(self, ret):
            return
        self._parent_window.fresh_page()
        self.destroy()

    # 发布试卷
    def release_exam(self):
        ret = QMessageBox.question(self, '警告', '你确定要发布吗？发布后无法取消。', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.No:
            return
        ret = self.exam_io.release_exam(self.exam_id)
        if not error_shower(self, ret):
            return
        
        self.main_ui.release_exam_button.setText("已发布")
        self.main_ui.release_exam_button.setEnabled(False)
    
    # 考试模式切换事件
    def changeModeEvent(self, tag):
        if tag == 0:
            self.main_ui.fixed_mode_frame.hide()
            self.main_ui.random_exam_frame.show()
        elif tag == 1:
            self.main_ui.random_exam_frame.hide()
            self.main_ui.fixed_mode_frame.show()
    
    # 改变题目事件
    def changeQuestionNameEvent(self, text):
        if text != "":
            self.main_ui.next_question_button.setEnabled(True)
        elif len(self.questions) == self.current_question_index:
            self.main_ui.next_question_button.setEnabled(False)
