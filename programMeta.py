# Information in the program we want to be everywhere

class program_meta:
    def __init__(self, file_name, delimeter = ','):
        self.file_name = file_name
        self.delimeter = delimeter
        
    def changeFileName(self, file_name):
        self.file_name = file_name