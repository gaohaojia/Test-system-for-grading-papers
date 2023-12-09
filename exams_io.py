import DB_connector
from question import Question

class ExamIO():

    # 初始化数据库
    def __init__(self) -> None:
        DB_connector.connector.init()
        if DB_connector.connector.status == "error":
            return "network error"

    # 写入试卷信息
    def write_exam_info(self, id, create_teacher, name, start_time, end_time, exam_time, mode, mode_para, classes):

        # 判断该试卷是否存在
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM exams WHERE id = {});".format(id))
        if db_result == "error":
            return "database error"
        
        # 不存在则创建试卷
        if db_result[0][0] == 0:
            if not DB_connector.connector.run_insert("INSERT INTO exams (id, name, create_teacher, isRelease) VALUES ({}, \'{}\', \'{}\', 0);".format(id, name, create_teacher)):
                return "database error"
        
        # 写入数据
        if not DB_connector.connector.run_insert(
            "UPDATE exams SET name=\'{}\', \
            start_time=\'{}\', \
            end_time=\'{}\', \
            exam_time={}, \
            mode={}, \
            mode_para={}, \
            classes=\'{}\' WHERE id={};".format(
                name, 
                start_time.toString("yyyy-MM-dd hh:mm:ss"), 
                end_time.toString("yyyy-MM-dd hh:mm:ss"), 
                exam_time,
                mode, 
                mode_para, 
                classes, 
                id)):
            return "database error"
        
        return "success"
    
    # 写入试卷题目
    def write_exam_table(self, id, questions: list[Question]):
        if not DB_connector.connector.run_other("drop table if EXISTS exam_{}".format(id)):
            return "database error"
        if not DB_connector.connector.run_other(
            "CREATE table exam_{} (\
            id INT primary key auto_increment,\
            name VARCHAR(255),\
            option1 VARCHAR(255),\
            option1_state TINYINT(1),\
            option2 VARCHAR(255),\
            option2_state TINYINT(1),\
            option3 VARCHAR(255),\
            option3_state TINYINT(1),\
            option4 VARCHAR(255),\
            option4_state TINYINT(1),\
            option5 VARCHAR(255),\
            option5_state TINYINT(1),\
            option6 VARCHAR(255),\
            option6_state TINYINT(1))".format(id)):
            return "database error"
        for question in questions:
            msg = "\'{}\'".format(question.name)
            for option in question.options:
                msg += ", \'{}\', {}".format(option.name, 1 if option.isCorrect else 0)
            if not DB_connector.connector.run_insert(
                "INSERT INTO exam_{} (name,\
                option1, option1_state,\
                option2, option2_state,\
                option3, option3_state,\
                option4, option4_state,\
                option5, option5_state,\
                option6, option6_state)\
                VALUES ({})".format(id, msg)):
                return "database error"
        return "success"
    
    # 获取所有题目信息
    def get_all_questions(self, id):
        db_result = DB_connector.connector.run_select("SELECT * FROM exam_{};".format(id))
        if db_result == "error":
            return "database error"
        return db_result

    # 获取新试卷id
    def get_new_exam_id(self):
        db_result = DB_connector.connector.run_select("SELECT id FROM exams ORDER BY id DESC limit 1;")
        if db_result == "error":
            return "database error"
        return 1 if len(db_result) == 0 else int(db_result[0][0]) + 1

    # 获取所有试卷信息
    def get_all_exam_info(self):

        # 判断是否存在试卷
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM exams);")
        if db_result == "error":
            return "database error"
        if db_result[0][0] == 0:
            return []

        db_result = DB_connector.connector.run_select("SELECT id, create_teacher, classes, isRelease FROM exams;")
        if db_result == "error":
            return "database error"
        
        return db_result
    
    # 通过试卷id获取试卷信息
    def get_exam_info_by_id(self, id):
        db_result = DB_connector.connector.run_select("SELECT name, start_time, end_time, exam_time, mode, mode_para, classes, isRelease FROM exams WHERE id={};".format(id))
        if db_result == "error":
            return "database error"
        
        return db_result[0]
    
    # 删除试卷
    def delete_exam(self, id):
        if not DB_connector.connector.run_other("drop table if EXISTS exam_{}".format(id)):
            return "database error"
        if not DB_connector.connector.run_insert("DELETE FROM exams WHERE id={};".format(id)):
            return "database error"
        return "success"
    
    # 发布试卷
    def release_exam(self, id):
        if not DB_connector.connector.run_insert("UPDATE exams SET isRelease=1 WHERE id={};".format(id)):
            return "database error"
        return "success"
    
    # 学生交卷
    def submit_exam(self, id, questions: list[Question], student_number):

        # 判断该试卷之前是否有人提交过
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM information_schema.tables WHERE table_name = \'submit_exam_{}\');".format(id))
        if db_result == "error":
            return "database error"
        
        # 不存在则创建提交表
        if db_result[0][0] == 0:
            
            # 获取考试题目数量
            question_cnt = DB_connector.connector.run_select("SELECT count(*) FROM exam_{};".format(id))
            if question_cnt == "error":
                return "database error"
            
            # 创建提交表
            sql = "CREATE table submit_exam_{} (student_number INT primary key".format(id)
            for i in range(question_cnt[0][0]):
                sql += ",option{} VARCHAR(255)".format(i + 1)
            sql += ");"

            if not DB_connector.connector.run_other(sql):
                return "database error"
        
        # 插入数值
        sql = "INSERT INTO submit_exam_{} (student_number".format(id)
        for question in questions:
            sql += ",option{}".format(question.question_id)
        sql += ") VALUES (\'{}\'".format(student_number)
        for question in questions:
            str = ""
            for option in question.options:
                str += "1," if option.isCorrect else "0,"
            str = str[:-1]
            sql += ",\'{}\'".format(str)
        sql += ");"
        if not DB_connector.connector.run_insert(sql):
            return "database error"
        
        return "success"
    
    # 获取是否已提交状态
    def get_submit_stats(self, id, student_numer):

        # 判断该试卷之前是否有人提交过
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM information_schema.tables WHERE table_name = \'submit_exam_{}\');".format(id))
        if db_result == "error":
            return "database error"
        
        if db_result[0][0] == 0:
            return "not yet"
        
        # 判断是否提交过
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM submit_exam_{} WHERE student_number = \'{}\');".format(id, student_numer))
        if db_result == "error":
            return "database error"
        
        if db_result[0][0] == 0:
            return "not yet"
        
        return "submitted"
    
    # 获取全部答题情况
    def get_all_submitted(self, id):

        # 判断该试卷之前是否有人提交过
        db_result = DB_connector.connector.run_select("SELECT exists (SELECT * FROM information_schema.tables WHERE table_name = \'submit_exam_{}\');".format(id))
        if db_result == "error":
            return "database error"
        
        if db_result[0][0] == 0:
            return []

        # 判断该试卷之前是否有人提交过
        db_result = DB_connector.connector.run_select("SELECT * FROM submit_exam_{};".format(id))
        if db_result == "error":
            return "database error"
        
        return db_result

