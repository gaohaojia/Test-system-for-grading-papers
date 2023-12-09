import DB_connector

class InfoIO():

    # 初始化数据库
    def __init__(self) -> None:
        DB_connector.connector.init()
        if DB_connector.connector.status == "error":
            return "network error"

    # 获取所有班号
    def get_classes(self):
        db_result = DB_connector.connector.run_select("SELECT number FROM classes;")
        if db_result == "error":
            return "database error"
        
        return db_result