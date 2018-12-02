import sys
sys.path.append('..')
from ExFramework.ExBlock import *

from ExFramework.ExInputPort import *
from ExFramework.ExOutputPort import *

class CosFun(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name, '余弦信号发生器')
         self.children.append(ExInputPort('A', '振幅', self))
         self.children.append(ExInputPort('w', '角速度，单位为弧度/S', self))
         self.children.append(ExInputPort('t', '初始角度,单位为弧度', self))
         self.children.append(ExInputPort('En', '有效', self))
         self.children.append(ExOutputPort('Out','输出', self))

