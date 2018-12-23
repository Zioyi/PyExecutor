from ExFramework.ExComponentFactory import *
from ExFramework.ExJsonEncoder import *
from PyExecutorFactory import *

from ElectricCooker.EcConnector import *
from ElectricCooker.OpPanel import *
from ElectricCooker.TempSensor import *
from ElectricCooker.HeatingController import *
from ElectricCooker.Display import *
from ElectricCooker.Heater import *


class EcComponentFactory(ExComponentFactory):

    def __init__(self):
        PyExecutorFactory().register('ecd', 'element', self)

    # 添加链接线
    def make_connector(self, parent):
        return EcConnector(parent, '')

    def element_types(self):
        types = ['OpPanel', 'TempIn', 'ComIn', 'ComOut','Contr', 'Disp', 'Heater']
        parent_types = ExComponentFactory.element_types(self)
        for t in parent_types:
            types.append(t)
        return types

    def make_element(self, parent, type):
        if type=='OpPanel':
            return OpPanel(parent, 'OpPanel').construct()
        elif type=='TempIn':
            return TempSensor(parent, 'TempSensor').construct()
        elif type=='ComIn':
            return CommInputFun(parent).construct()
        elif type=='ComOut':
            return CommOutputFun(parent).construct()
        elif type=='Contr':
            return HeatingController(parent, 'Controller').construct()
        elif type=='Disp':
            return Display(parent, 'Display').construct()
        elif type == 'Heater':
            return Heater(parent, 'Heater').construct()
        return ExComponentFactory.make_element(self, parent, type)

EcComponentFactory()