import configparser

class ReadIni():
    def __init__(self,file=None):
        self.cf = configparser.ConfigParser()
        if file == None:
            self.file = "../d/LocalElement.ini"
        else:
            self.file = file
        self.cf.read(self.file)

    def read_el(self,node,key):

        return self.cf.get(node,key)



if __name__ == '__main__':
    r = ReadIni("../config/LocalElement.ini")
    l = r.read_el("RegisterElement", "user")
    s= l.split(">")
    print(type(l))
    print(l)

    print(type(s))
    print(*s)
