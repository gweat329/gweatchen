'''
- from module_name import func_name,class_name,var_name
    - 按上述方法有选择性的导入
    - 使用的时候可以直接使用导入的内容，不需要前缀
    - 案例 p04
'''
from p01 import Student, sayHello

stu = Student("帅哥",19)
stu.say()
sayHello()
