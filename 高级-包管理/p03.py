'''
-import 模块 as 别名
    - 导入的同时给模块起一个别名
    - 其余用法跟第一种相同
    - 案例p03
'''

import p01 as p
stu = p.Student("yueyue",18)
stu.say()