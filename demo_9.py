# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def print_age(self):
#         print(self.name,':',self.age)
# s1 = Student('sb', 100)
# s1.print_age()

class Sb(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print(self.__name, 'has the score of', self.__score)
        
sb1 = Sb('qwer', 4)
sb1.print_score()

