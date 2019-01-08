'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
mingyue = Student()

# 在定义一个类，用来描述听Python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("我在做作业")

        # 推荐在函数末尾使用return语句
        return None

zengzhen = PythonStudent()
print(zengzhen.name)
print(zengzhen.age)
zengzhen.doHomework()