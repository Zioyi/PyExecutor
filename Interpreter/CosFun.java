



class CosFun (CalculateFunction):
	String getName(){
		return "cos"
	}
	
	boolean execute(self, paraList, context){
		if(len(paraList) != 1)
	    {
	        context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
	        return False
	    }
	    Complex para = paraList.getFirst()
	    if(para.i != 0)
	    {
	        context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
	        return False
	    }
	    double result = math.cos(para.r)
	    context.setCurrentResult(Complex(result))
	    return true
	}
}
