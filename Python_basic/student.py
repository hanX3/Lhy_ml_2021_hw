#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

##
han = Student("hanxingchi", 100)
zhao = Student("zhaomeiyang", 100)
print(han.name, han.get_grade())
print(zhao.name, zhao.get_grade())
