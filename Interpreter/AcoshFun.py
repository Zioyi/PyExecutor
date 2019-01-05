import math
from Interpreter.CalculateFunction import *
from Interpreter.Complex import *


class AcoshFun(CalculateFunction):
    def getName(self):
        return 'acosh'

    def execute(self, paraList, context):
        if len(paraList) != 1:
            context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
            return False

        para = paraList[0]
        if (para.i != 0):
            context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
            return False

        if (para.r < 1):
            context.setErrorMessage(self.getName(), R_string.error_invalid_input)
            return False

        value = math.sqrt((para.r + 1) / 2) + math.sqrt((para.r - 1) / 2)
        if (value == 0):
            context.setErrorMessage(self.getName(), R_string.error_invalid_input)
            return False

        context.setCurrentResult(Complex(math.log(value) * 2))
        return self.checkResult(context)
