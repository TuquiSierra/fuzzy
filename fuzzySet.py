class FuzzySet:     
    def __init__(self, elements):
        self.set=elements[0]
        for e in elements[1:]:
            self.set=self.set.compose(e)
    
    def crop(self, x):
        self.set=self.set.crop(x)
    
    def defuzzify(self,  method='centroid'):
        if method=='centroid':
            return self.__centroid__()
            
        if method=='sums':
            return self.__sums__()
           
        if method=='bisection':
            return self.__bisection__()
        
        if method=='LOM':
            return self.__last_of_maxima__()
        
        if method=='FOM':
            return self.__first_of_maxima__()
        
        if method=='MOM':
            return self.__mean_of__maxima__()
            
                
    def __centroid__(self):
        return sum([x*self.set(x) for x in self.set.domain])/sum([self.set(x) for x in self.set.domain])
    
    def __sums__(self):
         return (sum([x for x in self.set.domain])*sum([self.set(x) for x in self.set.domain]))/sum([sum([self.set(x) for x in self.set.domain]) for x in self.set.domain])
        
    def __bisection__(self):
        area=sum([(self.set.domain[i+1]-self.set.domain[i])*self.set((self.set.domain[i]+self.set.domain[i+1])/2) for i in range(len(self.set.domain)-1)])
        half=0
        for i in range(len(self.set.domain)-1):
            a=sum([(self.set.domain[i+1]-self.set.domain[i])*self.set((self.set.domain[i]+self.set.domain[i+1])/2) for i in range(i-1)])
            if a> area/2:
                return half
            half=self.set.domain[i]
            
    def __first_of_maxima__(self):
        maximum=0
        max_x=0
        for x in self.set.domain:
            s=self.set(x)
            if s>maximum:
                maximum=s
                max_x=x
        return max_x
    
    def __last_of_maxima__(self):
        maximum=0
        max_x=0
        for x in self.set.domain:
            s=self.set(x)
            if s>=maximum:
                maximum=s
                max_x=x
        return max_x
    
    def __mean_of__maxima__(self):
        maximum=0
        max_x=0
        count=1
        for x in self.set.domain:
            s=self.set(x)
            if s>maximum:
                maximum=s
                max_x=x
                count=1
            elif s==maximum:
                max_x+=x
                count+=1
        return max_x/count
               
    def plot(self, x=[]):
        return self.set.plot(x)


        
        
        