class Stack:
    #constructor
    def __init__(self):
        self.__stack = []  # create private stack
    #methods
    def pop(self):  #pop the item
        if self.isEmpty(): return None
        return self.__stack.pop()

    def peek(self): #peek the item (no removal)
        if self.isEmpty(): return None
        return self.__stack[len(self.__stack)-1]

    def push(self, item): #push the item
        self.__stack.append(item)

    def getSize(self):           #return stack size
        return len(self.__stack)

    def isEmpty(self): #check if stack empty
        return self.getSize()==0
    
    def __str__(self): # display stack in reverse order
      display=""
      for i in range(self.getSize()):
        display=display+str(self.__stack[i])+"\n"
      return(display)
