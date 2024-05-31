#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        knowledge = []
        self.knowledge = knowledge
    
    def learn(self,string):
        self.string = string
        self.knowledge.append(string)
        return self.knowledge

calvin = Student("Calvin", "Klein")
print(calvin.learn("ABC"))
print(calvin.learn("alphabet"))