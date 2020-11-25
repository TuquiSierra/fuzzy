from matplotlib import pyplot as plt
import numpy as np
import math

class Membership:
    def __init__(self, func, domain):
        self.func=func
        self.domain=domain
        
    
    def __call__(self, x):
        return self.func(x)
    
    def plot(self, points=[]):
        plt.plot([x for x in self.domain],[self.func(x) for x in self.domain])
        plt.ylabel('Membership')
        plt.ylim(-0.05, 1.05)
        colors=['r', 'b', 'c', 'm', 'y', 'g']
        for i,p in enumerate(points):
            plt.plot(p[0], self.func(p[0]), colors[i]+'o', label=p[1])
        plt.legend()
        plt.show()
        
        
    def compose(self, other):
        def composite(x):
            return max(self.func(x),other(x))
        return Membership(composite, np.linspace(min(self.domain[0], other.domain[0]),max(self.domain[-1], other.domain[-1]), 200))
    
    def clip(self, top):
        def cropped(x):
            return min(self.func(x),top)
        return Membership(cropped, self.domain)
    
    def scale(self, value):
        def scaled(x):
            return value*self.func(x)
        return Membership(scaled, self.domain)
        
    
class TriangularMembership(Membership):
    def __init__(self, start, peak, end, domain=None):
        def triangle(x):
            if x<start or x>end:
                return 0
            if x==peak:
                return 1
            if x<peak:
                return (1/(peak-start))*x+((1/(start-peak))*start)
            return (1/(peak-end))*x+((1/(end-peak))*end) 
        if not domain:
            domain=[i for i in np.linspace(start, end, 200)]
        super().__init__(triangle, domain)
        
class TrapezoidalMembership(Membership):
    def __init__(self, start, first_peak, second_peak, end, domain=None):
        def trapezoid(x):
            if x<start or x>end:
                return 0
            if x>=first_peak and x<=second_peak:
                return 1
            if x<first_peak:
                return (1/(first_peak-start))*x+((1/(start-first_peak))*start)
            return (1/(second_peak-end))*x+((1/(end-second_peak))*end)  
        if not domain:
            domain=[i for i in np.linspace(start, end, 200)]
        super().__init__(trapezoid,  domain)
        
class SigmoidalMembership(Membership):
    def __init__(self, growth=1, domain=None):
        if not domain:
            domain=[i for i in np.linspace(0, 10, 200)]
        def sigmoid(x):
            return 1/(math.e**(-(x*growth-domain[len(domain)//2]))+1)
        
        super().__init__(sigmoid, domain)
        

        
        
        