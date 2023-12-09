###
# 
#  注册窗口
#
###

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QMessageBox

from ui import sign_up_window

from account_io import AccountIO
from error_shower import error_shower

class SignUpWindow(QMainWindow):
    def __init__(self, _main_window):
        QMainWindow.__init__(self)
        self.main_ui = sign_up_window.Ui_Sign_up_window()
        self.main_ui.setupUi(self)
        self._main_window = _main_window

        # 固定窗口大小
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # 默认学生选项
        self.main_ui.Student_QRadio.click()

        # 创建按钮点击事件
        self.main_ui.Sign_up_button.clicked.connect(lambda: self.sign_up_button_clicked())

        # 回车确认事件
        self.main_ui.Password_Inputer_2.returnPressed.connect(lambda: self.sign_up_button_clicked())

        # 初始化数据库读取器
        self.account_io = AccountIO()

        # 展示图片
        self.main_ui.background_image.setPixmap(QtGui.QPixmap('images/sign.jpg'))
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.3)  # 透明度设置为0.5
        self.main_ui.background_image.setGraphicsEffect(op)
        self.main_ui.background_image.setScaledContents(True)

        self.setWindowIcon(QtGui.QIcon('ico.ico'))
    
    # 注册按钮点击事件
    def sign_up_button_clicked(self):
        user_type = 1 if self.main_ui.Teacher_QRadio.isChecked() else 2
        account = self.main_ui.account_Inputer.text()
        number = self.main_ui.number_Inputer.text()
        password = self.main_ui.Password_Inputer.text()
        password2 = self.main_ui.Password_Inputer_2.text()

        # 判断账号信息是否未空
        if account == "":
            QMessageBox.warning(self, "警告", "未输入账号！", QMessageBox.Cancel)
            return
        if number == "":
            QMessageBox.warning(self, "警告", "未输入职工号/学号！", QMessageBox.Cancel)
            return


        # 判断两次输入是否一致
        if password != password2:
            QMessageBox.warning(self, "警告", "密码不符合规范！", QMessageBox.Cancel)
            return
        
        # 注册人脸
        md5_hash = None
        if user_type == 2:
            self._main_window._face_id_window.show()
            md5_hash = self._main_window._face_id_window.start_train(account)
            self._main_window._face_id_window.destroy()
            if md5_hash == "faith":
                QMessageBox.warning(self, "警告", "人脸注册失败！", QMessageBox.Cancel)
                return
        
        # 尝试保存账户
        ret = self.account_io.write_account(account, password, user_type, number, md5_hash)
        if ret == "success":
            QMessageBox.about(self, "成功", "注册成功！")
            self.destroy()
        else:
            # 输出错误信息
            error_shower(self, ret)