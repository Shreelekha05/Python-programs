#inheritance
#multiple inheritance
class S:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class S1:
    def __init__(self,marks):

        self.marks=marks

class S2(S,S1):
    def __init__(self,name,rollno,marks,place):
        self.place=place
        S.__init__(self,name,rollno)
        S1.__init__(self,marks)
obj2=S2("shree",40,98,"ballari")
print(obj2.name)
print(obj2.rollno)
print(obj2.marks)
print(obj2.place)
