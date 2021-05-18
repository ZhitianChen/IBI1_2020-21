class Score(object):  # to define a new class
    def __init__(self, n, g_cp, g_pp, g_fe):
        self.n = n
        self.g_cp = g_cp
        self.g_pp = g_pp
        self.g_fe = g_fe
    def displayScore(self):  # to define a new function
        print(self.n)  # to print the name of the student
        print(self.g_cp * 0.4 + self.g_fe * 0.3 + self.g_pp * 0.3)  # to print scores of the students

student = Score("Yamako", 85, 90, 79)  # a example for input
student.displayScore()  # use the function
