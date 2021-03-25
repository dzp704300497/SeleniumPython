import xlrd
class ExcelUtil():
    def __init__(self,filename=None,sheet_name=None):
        if filename == None:
            self.filename = "/Users/duanzhanpeng/PycharmProjects/WebProject/data/certificate_data.xlsx"
        else:
            self.filename = filename

        if sheet_name == None:
            self.sheet_name = "Sheet1"
        else:
            self.sheet_name = sheet_name
        self.book = xlrd.open_workbook(self.filename)
        self.table = self.book.sheet_by_name(self.sheet_name)

    def row_data (self):
        nrows = self.table.nrows
        num = []
        for n in range(nrows):
            row_data = self.table.row_values(n)
            num.append(row_data)

        return num

if __name__ == '__main__':
    e = ExcelUtil()
    d = e.row_data()
