###
# 
#  登录窗口
#
###

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QMessageBox

from ui import sign_in_window

from account_io import AccountIO
from error_shower import error_shower
from SignUpWin import SignUpWindow

class SignInWindow(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        self.main_ui = sign_in_window.Ui_Sign_in_window()
        self.main_ui.setupUi(self)

        # 保存父窗口
        self._parent_window = parent

        # 固定窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # 创建按钮点击事件
        self.main_ui.sign_in_button.clicked.connect(lambda: self.sign_in_button_clicked())
        self.main_ui.sign_up_button.clicked.connect(lambda: self.sign_up_button_clicked())

        # 回车确认事件
        self.main_ui.Password_Inputer.returnPressed.connect(lambda: self.sign_in_button_clicked())

        # 初始化注册窗口
        self._sign_up_window = SignUpWindow(self._parent_window)

        # 初始化数据库读取器
        self.account_io = AccountIO()

        # 展示图片
        self.main_ui.background_image.setPixmap(QtGui.QPixmap('images/sign.jpg'))
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.3)  # 透明度设置
        self.main_ui.background_image.setGraphicsEffect(op)
        self.main_ui.background_image.setScaledContents(True)

        self.setWindowIcon(QtGui.QIcon('ico.ico'))
    
    # 窗口关闭事件
    def closeEvent(self, a0) -> None:
        self._parent_window.close()
        return super().closeEvent(a0)

    # 点击登录按钮事件
    def sign_in_button_clicked(self):
        user_type = 1 if self.main_ui.Teacher_QRadio.isChecked() else 2
        account = self.main_ui.account_Inputer.text()
        password = self.main_ui.Password_Inputer.text()

        # 判断账号信息是否未空
        if account == "":
            QMessageBox.warning(self, "警告", "未输入账号！", QMessageBox.Cancel)
            return
        if password == "":
            QMessageBox.warning(self, "警告", "未输入密码！", QMessageBox.Cancel)
            return

        # 验证账号
        ret = self.account_io.verify_account(user_type, account, password)
        if ret == "correct":
            number = self.account_io.get_number(user_type, account)
            if not error_shower(self, account):
                return
            name = self.account_io.get_name(user_type, number)
            if not error_shower(self, name):
                return
            class_number = self.account_io.get_class_number(number)
            if not error_shower(self, class_number):
                return
            self._parent_window.finish_sign_in(user_type, account, number, name, class_number)
            self.destroy()
        else:
            # 输出错误信息
            error_shower(self, ret)
    
    # 点击注册按钮事件
    def sign_up_button_clicked(self):
        # 初始化界面
        self._sign_up_window.main_ui.Student_QRadio.click()
        self._sign_up_window.main_ui.account_Inputer.setText("")
        self._sign_up_window.main_ui.Password_Inputer.setText("")
        self._sign_up_window.main_ui.Password_Inputer_2.setText("")
        self._sign_up_window.show()