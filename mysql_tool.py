import pymysql
class mysql:
    # 打开数据库连接
    def __init__(self):
        # 初始化连接配置和连接参数
        db_settings = {
            'host': '39.105.78.64',
            'db': 'flask_project',
            'user': 'root',
            'password': '123456',
            'charset': 'utf8',
            'use_unicode': True
        }

        # self.db_setting = crawler.settings.get('db_setting')
        self.conn = pymysql.connect(**db_settings)
        self.cursor = self.conn.cursor()
    def get_user(self,name,password):
        sql = "select name,password from user where name ='%s'" % name
        try:
            # 从数据库中获取一行值
            self.cursor.execute(sql)
            # 对于查询结果不能直接获取，需要通过fetchall，索引来取每个值
            info_list = self.cursor.fetchall()
            print(info_list[0])
            if info_list[0][1] == password:
                return True
            else:
                return False
        except Exception as e:
            print(e)