# Connor McGarry
#
#
from StackCalc import StackCalc


class Link:
    def __init__(self, data):
        self.data = data   # represents one integer between 1-9 
        self.prev = None
        self.next = None

    def __str__(self):
      return str(self.data)

  
class BigNumberLL: ### To complete   (LINKED LIST)

    '''Sets up class variables, automatically creates a linked list 
        of integers based off a string of the input'''
    def __init__(self, input): 
        self.input = input
        self.first = None
        self.last = None
        self.size = 0
        self.positive = True  # FLAG FOR COMPARISONS
        if '-' in str(self.input):
            self.positive = False  # knows if input is pos or neg
        for num in str(self.input).strip('-'):
            self.size+=1
            self.insertLast(int(num))  # makes the linked list using integers
        self.trimFront()  # gets rid of the 0s at the start of the list


    '''Returns a string of the linked list values, along with its size '''
    def __str__(self):  # needs to return the list as a string to be printed, include commas and strip 0s, all that shit
        current = self.first # starts at the beginning of the list
        temp = ''
        while current is not None: # scan until the end of the list
            temp+=str(current.data)  # places the values one after another in a string 
            current = current.next 
        if self.size == 0:
            self.size = 1  # if the only number is a 0, make sure its size is 1
        if self.positive == False: # add a "-" to the string if the pos/neg flag is false
            return f'[{self.size}] -{int(temp):,}'
        else:
            return f'[{self.size}] {int(temp):,}'


    '''check if the linked list has any variables in it'''
    def isEmpty(self):
        return self.first is None
    

    '''Inserts new link to the end of the linked list'''
    def insertLast(self,num):
        newLink=Link(num)
        if self.isEmpty():   # if its empty then it is now the first link
            self.first=newLink # special case
        else:
            self.last.next = newLink # step 1
        newLink.prev = self.last # step 2
        self.last=newLink


    '''Inserts new link to the start of the list'''
    def insertFirst(self,num):
        newLink=Link(num)
        if self.isEmpty(): 
            self.last=newLink # special case
        else:
            self.first.prev = newLink # step 1
        newLink.next = self.first # step 2
        self.first=newLink 


    '''Deletes the first link in the list'''
    def deleteFirst(self):
        if self.isEmpty(): return None
        temp = self.first # save first Link
        if self.first.next is None: #only 1 item
            self.last=None # special case
        else:
            self.first.next.prev = None # step 1
        self.first = self.first.next # step 2
        return temp


    '''Gets rid of any leading 0s that are in a linked list, and creates a new link of 0 if empty after'''
    def trimFront(self):
        current = self.first
        try: 
            while current.data == 0:  # while the value of the leading link is 0
                self.size-=1  # reduce the size of the list
                self.deleteFirst()  # delete the 0
                current = current.next  # move forward
        except:
            self.insertLast(0)  # if the list runs out of links, then add a link with 0


# ----------------- TASK 1 --------------------------------------

    '''Checks if given value is greater than second value'''
    def __gt__(self,y):
        # simple comparisons regarding size and pos/neg flags
        if self.positive == True and y.positive == False:
            return True
        elif self.size > y.size:
            return True
        elif self.positive == False and y.positive == False:
            if self.size < y.size:
                return True

        elif self.size == y.size:  # if the bignumbers are the same size
            currentx = self.last
            currenty = y.last
            while currentx is not None:
                if currentx.data > currenty.data:  # run through the links and return true if there is target digits are bigger than comparison
                    return True   
                currentx=currentx.prev
                currenty=currenty.prev
        return False

    
    '''Checks is target is less than comparison
        Coded to just be gt in reverse, so just simple sign changes, same process'''
    def __lt__(self,y):
        # simple comparisons regarding size and pos/neg flags
        if self.positive == False and y.positive == True:
            return True
        elif self.positive == False and y.positive == False:
            if self.size > y.size:
                return True
        elif self.size < y.size:
            return True

        elif self.size == y.size:# if the bignumbers are the same size
            currentx = self.last
            currenty = y.last
            while currentx is not None:
                if currentx.data < currenty.data: # run through the links and return true if there is target digits are bigger than comparison
                    return True   
                currentx=currentx.prev
                currenty=currenty.prev
        return False
        

    '''Checks if target is equal to comparison, relies on gt and lt fuctions  both retuning false'''
    def __eq__(self,y):
        if self.__lt__(y) == False and self.__gt__(y) == False:  # if target is neither less than nor greater than comparison it must be the same
            return True
        return False

# ----------------------------------- TASK 2 ---------------------------

    '''Adds two bignumbers together, returns a new bignumber
        Digit by digit, results plus carries are inserted to a new linked list, thus creating the answer'''
    def __add__(self,y):
        currentx = self.last
        currenty = y.last
        total = BigNumberLL('')  # initiate a new linked list for creating the result, requires an input due to setup format
        total.deleteFirst() # need this to clear the initiated linked list of its temporary link

        # -- GENERALIZATION --
        if y.positive is not True and self.positive is not True: # when both numbers are negative
            total.positive = False

        elif y.positive is not True and self.positive is True:
            y.positive = True
            if y.__lt__(self):  # subtract the smaller pos value from the larger pos value 
                return self.__sub__(y)
            else:
                a = y.__sub__(self)
                if a.first.data == 0:  # makes sure that the result is not "-" if the result is 0
                    a.positive = True 
                    return a
                a.positive = False   # makes the result negative
                return a

        elif y.positive is True and self.positive is not True:
            self.positive = True  # changing values to true and subtracting them to get the result, ehich is then negated 
            if self.__lt__(y):
                return y.__sub__(self)
            else:    
                a= self.__sub__(y)
                if a.first.data == 0:
                    a.positive = True
                    return a  # makes sure that there is no negative sign if result is 0
                a.positive = False
                return a

        # -- add --
        if self.size == y.size:   # EQUAL SIZED NUMBERS
            while (currentx is not None) and (currenty is not None):
                if currentx.data + currenty.data >=10: # if the result of the addition is over 10
                    total.insertFirst((currentx.data + currenty.data)%10) # takes the last digit in the result, like the 4 in 14 for example
                    if currentx.prev is not None:
                        currentx.prev.data = currentx.prev.data + (currentx.data + currenty.data)//10  # takes the 1 in 14 for example, and adds to next value (carry)
                    elif currentx.prev is None and currenty.prev is None:
                        total.size+=1
                        total.insertFirst((currentx.data + currenty.data)//10) # if there are no more digits to add, then insert the carry into linked list
                else:
                    total.insertFirst(currentx.data + currenty.data)   # if additon not over 10, add normally and continue

                total.size +=1
                currentx = currentx.prev
                currenty = currenty.prev
                

        if self.size != y.size:
            if self.size < y.size:
                for i in range(y.size-self.size):
                    self.insertFirst(0)  # if the numbers are inequal, add "filler" 0s to the smaller number

                # functions essentially the same as the when they are equal to eachother now 
                while currenty is not None:
                    if currentx.data + currenty.data >=10:
                        total.insertFirst((currentx.data + currenty.data)%10)
                        total.size +=1
                        carry = (currentx.data + currenty.data)//10
                        if currenty.prev is None:
                            total.insertFirst(carry)
                            total.size += 1
                            return total   # return the total if there are no more digits, and put carry in front
                        currenty.prev.data = currenty.prev.data + carry #carries the number                     
                        
                    else:
                        total.insertFirst(currentx.data + currenty.data)
                        total.size +=1

                    currentx = currentx.prev
                    currenty = currenty.prev


            elif self.size > y.size:
                for i in range(self.size-y.size):
                    y.insertFirst(0)

                # essentially the same as previous condition
                while currentx is not None:
                    if currentx.data + currenty.data >=10:
                        total.insertFirst((currentx.data + currenty.data)%10) #sum
                        total.size +=1
                        carry = (currentx.data + currenty.data)//10
                        if currentx.prev is None:
                            total.insertFirst(carry)
                            total.size += 1
                            return total
                        currentx.prev.data = currentx.prev.data + carry #carry
                        
                    else:
                        total.insertFirst(currentx.data + currenty.data)
                        total.size +=1
                   
                    currentx = currentx.prev
                    currenty = currenty.prev
        
        return total # returns new linked list bignumber
               

# ---------------------- TASK 3 ----------------------------------------

    '''Subtracts smaller number from larger. Done a little differently than add in terms of handing conditions, but just based on preference
         '''
    def __sub__(self,y):
        currentx = self.last
        currenty = y.last
        total = BigNumberLL('')
        total.deleteFirst()

        # - GENERALIZATION -
        if (self.size == y.size) and (self.__lt__(y)):  # specifically for when the numbers are the same size as alreadly handles otherwise
            a = self.__sub__(y)
            a.positive = False
            return a

        if self.positive is True and y.positive is not True:
            y.positive = True
            a = y.__add__(self)  # - minus + is adding 
            return a

        elif self.positive is not True and y.positive is True:
            self.positive = True
            a= y.__add__(self)  # + minus - is adding
            a.positive = False
            return a

        # SUB
        if (y.size < self.size) or (y.size > self.size):
            if y.size < self.size:
                for i in range(self.size-y.size):
                    y.insertFirst(0)  # adds 0s to the smaller number to make equal
            elif self.size < y.size:
                total.positive = False  # make the result negative if subtracting larger from smaller
                for i in range(y.size-self.size):
                    self.insertFirst(0) # adds 0s to the smaller number to make equal
                temp = currentx  # different than add, basically just swap the numbers with eachother so I can get rid of a section of code
                currentx = currenty
                currenty = temp
            
            while (currenty is not None) and (currentx is not None):
                if (currentx.data - currenty.data) < 0: # if values are negative

                    total.insertFirst((currentx.data - currenty.data) + 10) # subtract the values and add 10 to them
                    total.size +=1
                    currenty.prev.data = currenty.prev.data + 1  #carry
                    
                else:
                    total.insertFirst(currentx.data - currenty.data) # just subtract and move on
                    total.size +=1

                
                currentx = currentx.prev
                currenty = currenty.prev


        elif y.size == self.size:
            #carry = currentx.data - currenty.data
            # ----if the remainder carries over to be added tp the last digit
            while (currenty is not None) and (currentx is not None):
                if (currentx.data - currenty.data) < 0: # if values are negative

                    total.insertFirst((currentx.data - currenty.data) + 10) # subtract the values and add 10 to them
                    total.size +=1
                    currenty.prev.data = currenty.prev.data + 1  #carry
                    
                else:
                    total.insertFirst(currentx.data - currenty.data)
                    total.size +=1


                currentx = currentx.prev
                currenty = currenty.prev

        total.trimFront()  # helps with the count in the situation that the result is zero. (ensures that it is 1)
        return total


# ------------------------------ TASK 4 ----------------------------
    
    '''Multiplies a bignumber by a single digit, digit by digit'''
    def scale(self,factor):
        current = self.last
        scaled = BigNumberLL('')
        scaled.deleteFirst()  # initiate a linkedlist for answer
        carry = 0

        while current is not None:
            if (factor*current.data) >= 10: # if the digit multiplication is over 10
                scaled.insertFirst((factor*current.data + carry)%10)  # insert the 4 in 14 for example for 7*2
                scaled.size += 1
                carry = (factor*current.data + carry)//10 # the carry is the 5 in 54 for 9*6 for example
                if current.prev is None:
                    scaled.insertFirst(carry) # if there are no numbers left to multipy, add the carry to the front
                    scaled.size+=1
            else:
                scaled.insertFirst(factor*current.data + carry) # just multiply and carry on if under 10
                scaled.size += 1
                carry = 0

            current = current.prev

        # GENERALIZATION
        if (self.positive is not True) and (scaled.first.data != 0):
            scaled.positive = False

        scaled.trimFront()   # if the factor is 0, want to return a 0 with size of 1
        return scaled


    '''Uses scale to find multiple products, and then add them together  by shifting with 0s'''
    def __mul__(self,y):
        currentx = self.last
        sums = BigNumberLL(0) # linkedlist with one link value of 0 

        i = 0
        while currentx is not None:
            a = y.scale(currentx.data)
            a.positive = True
            if i > 0:  # for every loop, insert one addtional zero into the addition row
                for x in range(i):  # add 0s every new multiplication row for addition
                    a.insertLast(int(0))
                    a.size +=1
            sums = sums.__add__(a)  # keep adding the products to the new products that are created 
            currentx = currentx.prev
            i += 1
        
        # Generalization
        if (y.positive is True and self.positive is not True) or (y.positive is not True and self.positive is True):
            sums.positive = False

        return sums


# ---------------------------- EXTRA CREDIT ------------------------------

    '''Divides two big numbers rounded to an integer, or in this case, check how many times "y" can be divided by "self" '''
    def __floordiv__(self,y):
        # reference variables used for the generalization, means that I dont need to change the flag of the variables used in the calculatins
        tempx = self.positive
        tempy = y.positive

        if (tempy is True and tempx is not True) or (tempy is not True and tempx is True) or (tempy is not True and tempx is not True):
            y.positive = True    # Sets the big numbers to positive in any case where they both are already not 
            self.positive = True

        final = BigNumberLL(0)  # how many times y can be divided (counts subtraction)

        if self.__lt__(y):   # if the result would be a float less than 0, just return 0
            return BigNumberLL(0)

        while self.__gt__(y) or self.__eq__(y):  # if y can be subtracted from self, add one to the final amount 
            final.first.data += 1
            self = self.__sub__(y)

        if (tempy is True and tempx is not True) or (tempy is not True and tempx is True):
            final.positive = False  # if the final answer should be negative, then change the pos/neg flag of final answer

        return final  # the amount of times that y was subtracted from self 
        


