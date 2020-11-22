class Expression:
    pass

    def And(self, other):
        return AndExpression(self, other)
    
    def Or(self, other):
        return OrExpression(self, other)


class BinaryExpression(Expression):
    def __init__(self, left, right):
        self.left=left
        self.right=right
    
class UnaryExpression(Expression):
    def __init__(self, variable, value):
        self.value=value
        self.variable=variable
        assert self.value in self.variable.terms
        
    def fuzzify(self, x):
        raise NotImplementedError()
    


class AtomicExpression(UnaryExpression):
    def __init__(self,variable, value):
        super().__init__(variable, value)
        
    def fuzzify(self, x):
        return self.value.membership(x)
        
        
class NotExpression(UnaryExpression):
    def __init__(self, variable, value):
        super().__init__(value, variable)
        
    def fuzzify(self, x):
        return 1-self.value.membership(x)
        
class AndExpression(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left, right)      
        
    
class OrExpression(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(left, right)
    
        
        
        
    
    

        
        
    