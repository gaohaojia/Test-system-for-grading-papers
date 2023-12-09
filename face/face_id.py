from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
import cv2
import numpy as np
import os
import shutil
import hashlib

class FaceTrain():
    def __init__(self) -> None:

        # 加载OpenCV人脸检测分类器Haar
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # LBPH方法
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    # 识别人脸
    def get_new_face(self, camera: cv2.VideoCapture, account, info_label: QLabel, image_label: QLabel):

        # 重置目录train_data
        filepath = "train_data"
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        else:
            shutil.rmtree(filepath)
            os.mkdir(filepath)

        sample_num = 0  # 已经获得的样本数
        while True:

            pictur_num = 200 # 训练样本数
            ret, frame = camera.read()

            if not ret:
                return "camera error"
            
            frame = cv2.resize(frame, (320, 240))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 检测人脸
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            # 框选人脸，for循环保证一个能检测的实时动态视频流
            for (x, y, w, h) in faces:
                
                # 人脸标记画框
                cv2.rectangle(frame, (x, y), (x + w, y + w), (255, 0, 0))
                sample_num += 1
                
                # 保存图像
                cv2.imwrite("./train_data/User." + account + '.' + str(sample_num) + '.jpg', gray[y:y + h, x:x + w])

            cv2.waitKey(1)
            if sample_num == pictur_num - 1:
                info_label.setText("保存中...请稍后...")
            elif sample_num >= pictur_num:
                return "success"
            else:

                # 输出预览信息
                info_label.show()
                info_label.setText("{:.1f}%".format(sample_num * 100.0 / pictur_num))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                qt_frame = QtGui.QImage(
                    frame.data,
                    frame.shape[1],
                    frame.shape[0],
                    frame.shape[1] * 3,
                    QtGui.QImage.Format_RGB888)
                image_label.setPixmap(QtGui.QPixmap(qt_frame))
    
    # 训练人脸识别模型
    def train_new_face(self, account):
        
        path = 'train_data'

        # 初始化识别的方法
        recog = self.recognizer

        # 调用函数训练
        faces, ids = self.get_images_and_labels(path)

        # 训练模型
        recog.train(faces, np.array(ids))
        
        # 保存模型
        yml = account + ".yml"
        rec_f = open(yml, "w+")
        rec_f.close()
        recog.save(yml)

        # 计算MD5码
        with open(account + ".yml") as f:
            m = hashlib.md5()
            while True:
                data = f.read(4096).encode('utf-8')
                if not data:
                    break
                m.update(data)
            md5_hash = m.hexdigest()

        # 清除缓存
        shutil.rmtree(path)
        
        return md5_hash
    
    # 获取训练数据集
    def get_images_and_labels(self, path):
        
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        
        # 新建list
        face_samples = []
        ids = []

        # 遍历图片路径
        for image_path in image_paths:

            # 转为灰度图片
            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 将图片转化为数组
            img_np = np.array(img, 'uint8')

            if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
                continue

            # 调用人脸分类器
            detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

            faces = detector.detectMultiScale(img_np)

            # 将图片添加到list中
            for (x, y, w, h) in faces:
                face_samples.append(img_np[y:y + h, x:x + w])
                ids.append(1)
        return face_samples, ids
    

class FaceDetector():
    def __init__(self) -> None:
        # 加载OpenCV人脸检测分类器Haar
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # LBPH方法
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    # 校验MD5码
    def check_md5(self, account):
        try:
            with open(account + ".yml") as f:
                m = hashlib.md5()
                while True:
                    data = f.read(4096).encode('utf-8')
                    if not data:
                        break
                    m.update(data)
                md5_hash = m.hexdigest()
            return md5_hash
        except:
            return ""

    # 识别人脸
    def scan_face(self, camera: cv2.VideoCapture, account, image_label: QLabel):

        # 载入模型
        self.recognizer.read(account + ".yml")
        sum_poss = 0
        for times in range(1000):
            times += 1
            cur_poss = 0

            ret, frame = camera.read()
            if not ret:
                return "camera error"
            
            frame = cv2.resize(frame, (320, 240))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 识别人脸
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5
            )

            # 进行校验
            for (x, y, w, h) in faces:

                # 画矩形
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # 调用分类器的预测函数
                idnum, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
                conf = confidence

                if 65 > conf:
                    cur_poss = 1
                else:
                    cur_poss = 0
                sum_poss += cur_poss

            # 输出预览信息
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            qt_frame = QtGui.QImage(
                frame.data,
                frame.shape[1],
                frame.shape[0],
                frame.shape[1] * 3,
                QtGui.QImage.Format_RGB888)
            image_label.setPixmap(QtGui.QPixmap(qt_frame))
            cv2.waitKey(1)

            if sum_poss >= 2:
                return "success"
            
        return "faith"
    
    # 检测是否有人脸
    def detect_face(self, frame):
        frame = cv2.resize(frame, (320, 240))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 识别人脸
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        return True if len(faces) == 1 else False