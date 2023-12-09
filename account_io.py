import hashlib
import DB_connector
import datetime

class AccountIO():
    
    # 初始化数据库
    def __init__(self) -> None:
        DB_connector.connector.init()
        if DB_connector.connector.status == "error":
            return "network error"
        
    # 根据账号获取学号
    def get_number(self, user_type, account):
        db_result = DB_connector.connector.run_select("SELECT number FROM account WHERE account = \'{}\' AND type = {};".format(account, user_type))
        if db_result == "error":
            return "database error"
        
        return db_result[0][0]
    
    # 根据账号获取md5信息
    def get_face_id(self, account):
        db_result = DB_connector.connector.run_select("SELECT face_id FROM account WHERE account = \'{}\' AND type = 2;".format(account))
        if db_result == "error":
            return "database error"
        
        return db_result[0][0]

    # 根据学号获取姓名
    def get_name(self, user_type, number):
        db_result = DB_connector.connector.run_select("SELECT name FROM {} WHERE number = {};".format("teacher" if user_type == 1 else "student", number))
        if db_result == "error":
            return "database error"
        
        return db_result[0][0]
    
    # 根据学号获取班级
    def get_class_number(self, number):
        db_result = DB_connector.connector.run_select("SELECT class FROM student WHERE number = {};".format(number))
        if db_result == "error":
            return "database error"
        
        db_result = DB_connector.connector.run_select("SELECT number FROM classes WHERE id = {};".format(db_result[0][0]))
        if db_result == "error":
            return "database error"
        
        return db_result[0][0]

    # 验证账号密码是否匹配
    def verify_account(self, user_type, account, password):

        # 判断账户是否存在
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM account WHERE account = \'{}\' AND type = {});".format(account, user_type))
        if db_result == "error":
            return "database error"
        elif db_result[0][0] == 0:
            return "inexistence"
        
        # 判断密码是否正确
        db_result = DB_connector.connector.run_select("SELECT password FROM account WHERE account = \'{}\' AND type = {};".format(account, user_type))
        if db_result == "error":
            return "database error"
        elif hashlib.sha256(password.encode('utf-8')).hexdigest() != db_result[0][0]:
            return "wrong password"
        else:
            if not DB_connector.connector.run_insert("UPDATE account SET last_login_time = \'{}\' WHERE account = \'{}\' AND type = {};".format(datetime.datetime.now(), account, user_type)):
                return "database error"
            return "correct"

    # 写入新注册的账户
    def write_account(self, id: str, password: str, user_type: int, number: str, md5_hash = None):

        # 验证密码是否符合要求
        if not 6 <= len(password) <= 18:
            return "illegal password"
        if not True in [c.isdigit() for c in password]:
            return "illegal password"
        if not True in [c.islower() for c in password]:
            return "illegal password"
        if not True in [c.isupper() for c in password]:
            return "illegal password"
        
        # 判断账户是否存在
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM account WHERE account = \'{}\');".format(id))
        if db_result == "error":
            return "database error"
        elif db_result[0][0] == 1:
            return "existence"
        
        # 判断职工号/学号是否存在
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM {} WHERE number = \'{}\');".format("teacher" if user_type == 1 else "student", number))
        if db_result == "error":
            return "database error"
        elif db_result[0][0] == 0:
            return "number inexistence"
        
        # 判断职工号/学号是否被注册过
        db_result = DB_connector.connector.run_select("SELECT register FROM {} WHERE number = \'{}\';".format("teacher" if user_type == 1 else "student", number))
        if db_result == "error":
            return "database error"
        elif db_result[0][0] == 1:
            return "number registered"
        
        # 写入注册信息
        if not DB_connector.connector.run_insert("UPDATE {} SET register = 1 WHERE number = \'{}\';".format("teacher" if user_type == 1 else "student", number)):
            return "database error"
        
        # 加密密码
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        # 写入账户
        if user_type == 1:
            if not DB_connector.connector.run_insert("INSERT INTO account (account, password, create_time, type, number) VALUES (\'{}\', \'{}\', \'{}\', {}, \'{}\');".format(id, password, datetime.datetime.now(), user_type, number)):
                return "database error"
        else:
            if not DB_connector.connector.run_insert("INSERT INTO account (account, password, create_time, type, number, face_id) VALUES (\'{}\', \'{}\', \'{}\', {}, \'{}\', \'{}\');".format(id, password, datetime.datetime.now(), user_type, number, md5_hash)):
                return "database error"

        return "success"