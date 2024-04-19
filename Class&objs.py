#classes and objects
class Box:
    def __init__(self,curname,currollno,curosmarks,curdsmarks):
        self.name=curname
        self.rollno = currollno
        self.osmarks = curosmarks
        self.dsmarks = curdsmarks

#obj creation
s1=Box("shree",40,88,99,)
print(s1.name)
print(s1.rollno)
print(s1.osmarks,s1.dsmarks)

s1=Box("shree",40,88,99,)
print(s1.name)
print(s1.rollno)
print(s1.osmarks,s1.dsmarks)

s1=Box("ram",50,87,98,)
print(s1.name)
print(s1.rollno)
print(s1.osmarks,s1.dsmarks)

s1=Box("xyz",60,83,94,)
print(s1.name)
print(s1.rollno)
print(s1.osmarks,s1.dsmarks)

s1=Box("hello",70,75,100,)
print(s1.name)
print(s1.rollno)
print(s1.osmarks,s1.dsmarks)
