
# 包含一个学生类，
# 一个sayhello函数，
# 一个打印语句

class Student():
    def __init__(self,name="NoName",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("Hi, 欢迎来到图灵学院！")

# 此判断语句建议一直作为程序的入口
# 此判断语句含义：
#   在当前模块中直接运行时，会执行if后的语句，
#   在被其他调用此模块时，不会执行if后的语句。
# __name__含义：模块名称，是系统设定的变量名。
# '__main__'含义：当前的模块执行时的名称。
if __name__ == '__main__':

    print("我是模块p01呀，你特么的叫我干毛")