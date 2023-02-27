from StackCalc import *
from BigNumberLL import *

print("Welcome to the RPN calculator ('quit' to quit)")

mystack=StackCalc()

while True:    
  print(str(mystack)+"----------------------------------------------")
  prompt=input("$ ")    
  if prompt=="quit": break
  elif prompt=="": mystack.copy()
  elif prompt=="+": mystack.add()    
  elif prompt=="*": mystack.multiply()    
  elif prompt=="-": mystack.subtract()    
  elif prompt=="/": mystack.divide()
  elif prompt[0]=="s": mystack.scale(prompt)
  elif prompt in "=><": mystack.compare(prompt)
  else:
       mystack.push(BigNumberLL(prompt))  # it isnt pushing a string, rather a class object324

print("Thanks for using the RPN calculator")
