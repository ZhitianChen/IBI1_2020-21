class student(object):  # to define a new class
    def __init__(self, fn, ln, major):
        self.fn = fn
        self.ln = ln
        self.major = major
    def displayinfo(self):  # to define a new function
        print('Name: ' + self.ln + ' ' + self.fn + ', Major: ' + self.major)

student = student("Keina", "Suda", "BMS")  # a example for input
student.displayinfo()  # use the function
