
import os
import datetime
class T:
    def a(sl):
        s = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.getcwd()

        print(s)
        print(log_dir)
    # def b(sl):
    #     log_dir = os.getcwd() + os.sep + "logs"
    #     log_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    #     log_file = log_dir + os.sep + log_name
    #     print(log_file)

if __name__ == '__main__':
    t = T()
    t.a()


"""
/Users/duanzhanpeng/PycharmProjects/WebProject/log
/Users/duanzhanpeng/PycharmProjects/WebProject/logs/2021-03-24.log
"""