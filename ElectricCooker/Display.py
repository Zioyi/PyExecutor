import sys
sys.path.append('..')
from ExFramework.ExBlock import *

class Display(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name, '表示面板')
         self.children.append(ExInputPort('In1', '输入1', self))
         self.children.append(ExInputPort('In2', '输入2', self))
         self.children.append(ExInputPort('In3', '输入3', self))
         self.children.append(ExOutputPort('Sta', '状态输入', self))



