###
# 
#  人脸识别窗口
#
###

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGraphicsOpacityEffect
import cv2

from ui import face_id_window

from account_io import AccountIO
from face import face_id
from error_shower import error_shower

class FaceIDWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.main_ui = face_id_window.Ui_face_id_window()
        self.main_ui.setupUi(self)

        # 初始化界面
        self.main_ui.info_label.hide()
        self.main_ui.sign_in_button.hide()

        # 初始化人脸识别按钮
        self.train_face = face_id.FaceTrain()
        self.detect_face = face_id.FaceDetector()

        # 初始化数据库读取器
        self.account_io = AccountIO()

        # 展示图片
        self.main_ui.background_image.setPixmap(QtGui.QPixmap('images/sign.jpg'))
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.3)  # 透明度设置为0.5
        self.main_ui.background_image.setGraphicsEffect(op)
        self.main_ui.background_image.setScaledContents(True)

        self.setWindowIcon(QtGui.QIcon('ico.ico'))

    # 训练人脸
    def start_train(self, account):
        try:
            self.cap = cv2.VideoCapture(0)
        except:
            QMessageBox.warning(self, "警告", "无摄像头权限！", QMessageBox.Cancel)
            return "faith"
        
        ret = self.train_face.get_new_face(self.cap, account, self.main_ui.info_label, self.main_ui.camera_label)
        self.cap.release()
        if not error_shower(self, ret):
            return "faith"
        md5_hash = self.train_face.train_new_face(account)
        return md5_hash

    # 识别人脸
    def start_detect(self, account):
        try:
            self.cap = cv2.VideoCapture(0)
        except:
            QMessageBox.warning(self, "警告", "无摄像头权限！", QMessageBox.Cancel)
            return "faith"

        md5_hash = self.detect_face.check_md5(account)
        real_md5 = self.account_io.get_face_id(account)
        if real_md5 != md5_hash:
            self.cap.release()
            return "faith"
        
        ret = self.detect_face.scan_face(self.cap, account, self.main_ui.camera_label)
        self.cap.release()
        if not error_shower(self, ret):
            return "faith"
        return ret

    # 关闭事件
    def closeEvent(self, a0) -> None:
        self.cap.release()
        return super().closeEvent(a0)