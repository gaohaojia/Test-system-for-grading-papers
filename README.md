# 出卷评卷考试系统
#### 高颢嘉 赵则璇

## 软件特点
### 信息安全
- 人脸信息全部存在本地，避免隐私泄露，只将人脸信息的 MD5 码保存云端。
- 密码通过 sha256 加密后保存云端，避免密码泄露，传输全程不会出现密码原文。
### 防作弊
- 人脸信息文件 MD5 码保存云端，每次进行人脸验证时进行 MD5 码校验，避免学生篡改本地人脸信息。
- 账号信息全部保存在云端，学生无法篡改。
- 试卷信息全部保存在云端，学生无法作弊，学生端获取不到正确答案。
- 考完试后学生无法立刻获取成绩信息，避免多个学生间交流答案。
- 考试前需要人脸校验，避免替考。
- 注册账号需与教务提供的学号对应，且一个学号只能注册一个账号，避免多个账号同时答题。
- 考试期间摄像头全程监控，若没有摄像头权限、摄像头中未出现人脸或出现多个人脸则会报错，连续报错五次则强制提交试卷。
- 考试开始后界面会全屏显示。
- 考试开始后关闭考试页面会强制提交试卷。
- 考试时间截止后会强制提交试卷。
- 学生作答情况保存在云端，学生提交后无法篡改。
### 多种考试方式
- 考试模式可选“随机抽题”模式或“所有题目”模式。
- “随机抽题”模式支持自定义抽题数量。
- “所有题目”模式支持随机题目顺序。
- 老师端发布的题目可单选可多选，最多支持六个选项，提供老师高自由度选择。
- 老师可自定义考试开始日期时间、考试结束日期时间和学生考试时间。
- 老师可自定义参与考试的班级。
- 老师可选择是否发布考试。
### 考试情况分析
- 老师可查看当前已提交人数。
- 老师可查看当前提交学生的平均分。
- 老师可单独查看每道题的答题情况。
### 其他特点
- 考试试卷保存云端，老师可以多端编辑同一试卷，方便老师在学校电脑和自己笔记本间切换。
- 管理员可查看每个账号最近一次登录时间，避免恶意登录。
- 跨平台支持，软件支持 Windows、Mac OS、Linux使用。

## 使用方式
安装所需包文件。
```bash
pip install PyQt5 opencv-python opencv-contrib-python pymysql pyyaml matplotlib
```
在服务器上建立 mysql 数据库，具体如下：\
student:
| id | number | name | class | register |
| -- | ------ | ---- | ----- | -------- |
| int | varchar(255) |  varchar(255) | int | tinyint(1) |

teacher:
| id | number | name | register |
| -- | ------ | ---- | -------- |
| int | varchar(255) |  varchar(255) | tinyint(1) |

type:
| id | type |
| -- | ---- |
| int | varchar(255) |

exams:
| id | name | create_teacher | start_time | end_time | exam_time | mode | mode_para | classes | isRelease |
| -- | ---- | -------------- | ---------- | -------- | --------- | ---- | --------- | ------- | --------- |
| int | varchar(255) |  varchar(255) | datetime | datetime | int | int | int | varchar(255) | tinyint(1) |

classes:
| id | number | name |
| -- | ------ | ---- |
| int | varchar(255) | varchar(255) |

account:
| id | account | password | create_time | type | numebr | last_login_time | face_id |
| -- | ------- | -------- | ----------- | ---- | ------ | --------------- | ------- |
| int | varchar(255) |  varchar(255) | datetime | int | varchar(255) | datetime | varchar(255) |

配置用于连接 mysql 数据库的 key.yml 文件，将其放在文件根目录。
```
host: 
port: 
user: 
passwd: 
db: 
```

运行，体验我们的程序。
```bash
python main_run.py
```
