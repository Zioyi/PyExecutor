from Interpreter.CalculateFunction import *
from Interpreter.Complex import *

class SinhFun (CalculateFunction):
	def get_name(self):
		return "sinh"

	def execute(self, paraList):
		if len(paraList) != 1:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_parameter_count)
			return False
		para = paraList[0]
		if para.i:
			context.setErrorMessage(self.get_name(), R_string.error_invalid_date_type)
			return False

		result = math.sinh(para.r)
		context.setCurrentResult(Complex(result))
		return True
