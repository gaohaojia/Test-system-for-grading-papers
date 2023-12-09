from PyQt5.QtWidgets import QMessageBox

# 输出错误信息弹窗
def error_shower(obj, ret):
    error_msg = {
        "wrong password": "密码错误！",
        "inexistence": "账号不存在！",
        "existence": "账号已存在！",
        "wrong password": "密码错误！",
        "illegal password": "密码不符合规范！",
        "number inexistence": "职工号/学号不存在！有疑问请联系管理员。",
        "number registered": "职工号/学号已被注册！有疑问请联系管理员。",
        "network error": "网络错误！请检查网络连接。",
        "database error": "数据库错误！请联系管理员。",
        "camera error": "摄像头权限有问题！"
    }
    try:
        ret = error_msg[ret]
        QMessageBox.warning(obj, "警告", ret, QMessageBox.Cancel)
        return False
    except:
        return True