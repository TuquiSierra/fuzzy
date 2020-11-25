from expression import *
from fuzzySet import FuzzySet

class Rule:
    def __init__(self, precedent, consequent):
        self.precedent=precedent
        self.consequent=consequent
        

    def __fuzzify__(self, expression, values):
        if isinstance(expression, UnaryExpression):
            try:
                return expression.fuzzify(values[expression.variable.name])
            except KeyError:
                pass
        elif isinstance(expression, AndExpression):
            return min(self.__fuzzify__(expression.left, values), self.__fuzzify__(expression.right, values))
        elif isinstance(expression, OrExpression):
            return max(self.__fuzzify__(expression.left, values), self.__fuzzify__(expression.right, values))
        
    def apply(self, values):
        return self.__fuzzify__(self.precedent, values)
    
    
class RuleSet:
    def __init__(self, rules):
        self.rules=rules
        
    def __call__(self, values, d_method='centroid', a_method='Mamdani'):
        s=[]
        for r in self.rules:
            if isinstance(r.consequent, AndExpression):
                if a_method=='Mamdani':
                    s.append(r.consequent.left.value.membership.clip(r.apply(values)))
                    s.append(r.consequent.right.value.membership.clip(r.apply(values)))
                elif a_method=='Larsen':
                    s.append(r.consequent.left.value.membership.scale(r.apply(values)))
                    s.append(r.consequent.right.value.membership.scale(r.apply(values)))
                else:
                    raise Exception('Cut method must be one of (Mamdani, Larsen)')
                    
            elif isinstance(r.consequent, UnaryExpression):
                if a_method=='Mamdani':
                    s.append(r.consequent.value.membership.clip(r.apply(values)))
                elif a_method=='Larsen':
                    s.append(r.consequent.value.membership.scale(r.apply(values)))
                else:
                    raise Exception('Cut method must be one of (Mamdani, Larsen)')
            
        self.set=FuzzySet(s)
        return self.set.defuzzify(d_method)
    
    def plot(self, x=None):
        return self.set.plot(x)
        
            
        
    
        
        
        
        
        
        
        
        