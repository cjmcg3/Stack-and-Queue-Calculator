from Stack import *

class StackCalc(Stack):    
    def __init__(self):        
      super().__init__() 
      
    def add(self):      
      if self.getSize() >= 2:         
        self.push(self.pop()+self.pop())   

    def multiply(self):       
      if self.getSize() >= 2:            
        self.push(self.pop()*self.pop())

    def divide(self): 
      if self.getSize() >= 2:      
        a=self.pop()            
        b=self.pop()            
        self.push(b//a)    

    def subtract(self):        
      if self.getSize() >= 2:
        a=self.pop()            
        b=self.pop()            
        self.push(b-a)


    def compare(self,symbol):        
      if self.getSize() >= 2:
        a=self.pop()            
        b=self.pop()
        if symbol=="=":
            print(b==a)
        elif symbol==">":
            print(b>a)
        elif symbol=="<":
            print(b<a)

    def copy(self):        
      if self.getSize() >= 1:
        a=self.peek()                        
        self.push(a)

    def scale(self,factor):        
      if self.getSize() >= 1:
        a=self.pop()                        
        self.push(a.scale(int(factor[1])))
    
