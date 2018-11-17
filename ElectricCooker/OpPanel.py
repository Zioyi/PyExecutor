import sys
#sys.path.append('..')
from ExFramework.ExBlock import *

class OpPanel(ExBlock):
     def __init__(self, name):
         ExBlock.__init__(self,name)
         self.children.append(ExInputPort('Enable', self))
         self.children.append(ExOutputPort('Mode', self))
         self.children.append(ExOutputPort('Start', self))

