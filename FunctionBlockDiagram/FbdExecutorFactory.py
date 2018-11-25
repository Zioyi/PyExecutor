from FunctionBlockDiagram.FbdConnector import *
from FunctionBlockDiagram.SinFun import *
from FunctionBlockDiagram.CosFun import *
from FunctionBlockDiagram.MathFun import *
from FunctionBlockDiagram.GraphFun import *

#sys.path.append('..')

from PyExecutorFactory import *
from ExFramework.ExComponentFactory import *
from ExFramework.ExJsonEncoder import *

class FbdExecutorFactory(ExComponentFactory):
    def __init__(self):
        PyExecutorFactory().register('fbd', 'element', self)

    def make_connector(self):
        return FbdConnector()

    def element_types(self):
        types = ['Sin', 'Cos', 'Math', 'Graph']
        parent_types = ExComponentFactory.element_types(self)
        for t in parent_types:
            types.append(t)
        return types

    def make_element(self, type):
        if type=='Sin':
            return SinFun('Sin')
        elif type=='Cos':
            return CosFun('Cos')
        elif type=='Math':
            return MathFun('Math')
        elif type=='Graph':
            return GraphFun('Graph')
        return ExComponentFactory.make_element(self, type)

FbdExecutorFactory()
