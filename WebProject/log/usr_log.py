import logging
import os
import datetime


'''
1,创建Logger
2，Logger设置Level日志等级
3，创建Handler
4，输出
'''
class UsrLog():
    def __init__(self):

        #创建一个logger
        self.logger = logging.getLogger()
        #指定日志的最低输出级别，默认为WARN级别
        self.logger.setLevel(logging.DEBUG)

        # 设置log文件名
        self.log_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + "logs"
        self.log_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        self.log_file = self.log_dir + os.sep + self.log_name

        #创建一个handler用于写入日志文件
        self.file_handle = logging.FileHandler(filename=self.log_file)

        # 将log输出到控制台
        consle = logging.StreamHandler()
        self.logger.addHandler(consle)

        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(lineno)d %(message)s')
        self.file_handle.setFormatter(formatter)
        consle.setFormatter(formatter)


        self.logger.addHandler(self.file_handle)
        self.logger.addHandler(consle)

        # self.logger.debug("test")


    # def __del__(self):
    #     self.logger.removeHandler(self.file_handle)
    #     self.file_handle.close()

    def get_log(self):
        return self.logger
if __name__ == '__main__':
    u = UsrLog()
    u.get_log().debug("fsdfdsfsdfs")