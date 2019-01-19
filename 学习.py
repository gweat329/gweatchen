'''
for i in range(100,1000):
    temp = list(str(i))
    a = temp[0]
    b = temp[1]
    c = temp[2]
    if a**3 + b**3 + c**3 == i:
        print(i)
'''
class Student():

    def fget(self):
        return str(self._age)* 2
    def fset(self,age):
        self._age = int(age)

    def fdel(self):
        pass
    age = property(fget,fset,fdel,"对age进行下下操作啦")

stu1 = Student()
stu1.age = 19.8
print(stu1.age)