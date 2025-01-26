import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import im.module10 as module10
#遇到问题，无法导入module10.py中的变量
from im.module10 import z
y=20
print(y)
print(module10.y)#不同模块中的变量名可以相同
print(z)
