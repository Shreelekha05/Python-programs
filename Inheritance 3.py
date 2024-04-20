#inheritance
#multilevel inheritance
class S:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class S1(S):
    def __init__(self,name,marks,rollno):

        self.marks=marks
        S.__init__(self,name,rollno)
class S2(S1):
    def __init__(self,name,rollno,marks,place):
        self.place=place
        S.__init__(self,name,rollno)
        S1.__init__(self,name,marks,rollno)
obj2=S2("shree",40,95,"ballari")
print(obj2.name)
print(obj2.rollno)
print(obj2.marks)
print(obj2.place)
