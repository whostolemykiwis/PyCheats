'''
Created on May 29, 2016

@author: photonproton
'''

print "intro to python cheat/learing sheet"
print '-----------------------'

#varibles and types ----------------------------------------------------------------------------------------------------
theInt = 7 #initializes int variable
a, b = 1, 2 #you can do two at once
theFloat = 7.0 #intitalizes floating-point varible
#or theFloat = float(7)

theString1 = "hey" #initializes string 
theString2 = 'there' #^^

#combining stuff
three = a + b #adds the ints a and b to make another in that is name 'three'
greeting = theString1 + " " + theString2   # greeting is ==  "hey there"

# lists-------------------------------------------------------------------------------------------------------------------------
#makes list and adds appends one value
myList = [1,8,3,44]

#side note you can add lists together to make one combined list

myList.append(5)
print myList[1]#prints 2nd value in list (8)

#working with strings ----------------------------------------------------------------------------------------------------
testString = "hello world!"
print len(testString)#prints length of string (12)
print testString.index("o") #finds the first index of the letter 'o' (4)
print testString.count("o")# counts how many o's in the string (2)
       
#general form [start:stop:step]
print testString[3:7]#splices string from index 3 to 7 (lo w)
print testString[:7]#splices string from begining to 7th index (hello w)
print testString[3:]#splices string from 3rd index to end (lo world!)
print testString[-3:]#splices string from 3rd index from the end to end (ld!)
print testString[3:11:2]#splices string from 3rd to 7th but skips every other(l ol)
print testString[::-1]#reverses order of string

print testString.upper()#string to all upper
#string.lower() goes all lower

#returns boolean (True/False)
print testString.startswith("hello")# checks if string starts with 'hello'
print testString.endswith("world!")#checks from right to left if strings are ==

#Takes index with that value removes it and splits the string into sections around that indexes with that value 
newTest = testString.split("w")
print (newTest)    


#using '%' operator ------------------------------------------------------------------------------------------------------
'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
'''
    
Name = "Bill"
Age = 32
print "%s is %d years old." % (Name, Age) #prints: Bill is 32 years old.
print "%s this is my list" % myList#works with lists too

#math ops ----------------------------------------------------------------------------------------------------------------------
number = 1 + 2 * 3 / 4.0 # basic math all works (2.5)
#^^ number is a floating-point because it was operated by a floating-point

mod = 11 % 3 # mod is = to 2... this is the remainder 
squared = 7 ** 2
cubed = 2 ** 3

# you can make a string equal to whatever is in "" times a multiple
# you can also print things this way
lotsOfHellos = "hello" * 10
print "hey there\n" * 10#prints 'hey there '  ten times
#'\n' makes a new line

#conditons ---------------------------------------------------------------------------------------------------------------------------------------

# == is different that =... == checks for truth
x = 2
print x == 2 # prints out True
print x == 3 # prints out False
print x < 3  # prints out True

#if, else, elif, in, is, not 
name = "John"
age = 23
#ex of and operator
if name == "John" and age == 23:
    print "Your name is %s, and you are also %d years old." %(name, age)
#ex of or operator 
if name == "John" or name == "Rick":
    print "Your name is either John or Rick."

#'in' operator
if name in ["John", "Rick"]:
    print "your name is either John or Rick"#Checks to see if the var is in some list

#if statements
#d = 2
if x == 2: #need boolean equals
    print "x equals 2"
else:
    print "x doesnt equal 2"
    
#is operator
list1 = [1,2,3]
list2 = [1,2,3]
print list1 == list2 #will be true because '==' matches values in list to see if =
print list1 is list2 #prints out False

#not operator
print not False #prints out true
print (not False) == (False) #Prints out False

#Loops-----------------------------------------------------------------------------------------------------------------
#for loops
#prints out the numbers 0,1,2,3,4
for x in range(5):#or range(5)
    print x
    
primes = [2, 3, 5, 7]
for prime in primes: 
    print prime
        
#print out 3,4,5
for x in range (3, 6): #or range (3, 6)
    print x

#print out 3,5,7
for x in range(3, 8, 2): #or range(3, 8, 2)
    print x

#while loops
#print out 0,1,2,3,4
count = 0 
while count < 5:
    print count
    count += 1 #same as count = count + 1 (or you can do count++)

#break and continue statements    
#prints out 0,1,2,3,4
count = 0
while True:
    print count 
    count += 1
    if count >= 5:
        break

#print out only odd numbers - 1,3,5,7,9
for x in range(10):
    #checks if x is even
    if x % 2 == 0:
        continue
    print x

#prints out 0,1,2,3,4 and then it prints 'count value reached 5'

count = 0
while(count<5):
    print count
    count += 1
else: 
    print ("count value reached %d" 
           %count)
    
#print out 1,2,3,4
for i in range(1,10):
    if (i % 5 == 0):
        break
    print i
else: 
    print "this is not printed because for loop is terminated\
    because of break but not due to fail in condition"

#Functions---------------------------------------------------------------------------------------------------------------------------------------
def myFunction():
    print "Hello from my function!"
    
def functionWithArgs(username, greeting):
    print"hey, %s, from my function! I wish i could %s" %(username, greeting)
    
def sumTwoNumbers(a, b):
    return a + b

#prints the greetings and the sum
myFunction()

functionWithArgs("john", "fuck you")

w = sumTwoNumbers(2,3)
print w

#Classes and Objects------------------------------------------------------------------------------------------------------------------------------

class MyClass:
    Variable = "blah"
    
    def funck(self):
        print "This is the message inside the class"

myObjectx = MyClass() #enitializes object 

myObjectx.Variable # call to the variable
# if you were to print this, it would print 'blah'

# PRACTICE USING OBJECTS

# define the Vehicle class
class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" % (self.name, self.color,
                                                   self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00


print car1.description()
print car2.description()

#Dictionaries---------------------------------------------------------------------------------------

phoneBook = {}
phoneBook["John"] = 1234567
phoneBook["Jack"] = 9383772
phoneBook["Jill"] = 9476627

''' 
#you can also initialize dictionaries like this 
#this is the same thing as ^^^
phoneBook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
'''
#iterates over values in phoneBook
for name, number in phoneBook.items():
    print "Phone number of %s is %d" % (name, number)

#removing values
del phoneBook['John']
#or 'phoneBook.pop("John")'

#Generators-------------------------------------------------------------------------------------

import random

def lottery(): 
    #returns 6 nums between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)
        
    #returns a 7th number between 1 & 15
    yield random.randint(1, 15)
    
for randNumber in lottery():
    print "the next number is %d!" %randNumber

#List Comprehension-----------------------------------

sentence = "the quick brown fox jumps over the lasy dog"
words = sentence.split()
wordLength = []
for word in words:
    if word != "the":
        wordLength.append(len(word))
'''
this notation is also acceptable

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
'''
        
#Mulitple Function arguments-------------------------------------------------------------------------

def foo(first, second, third, *theRest):
    print "first #: %s\n\
second: %s\n\
third: %s" %(first, second, third)
    print "all the rest %s" %list(theRest)
    
foo(1,2,3,4,5)
'''
this will print 
first #: 1
second: 2
third: 3
all the rest [4, 5]
'''

#exmaple wiht keywords
#there are precodition one knowing what the options may do
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print "Result: %d" % result

#exception Handling----------------------------------------------------------
#origonal by photonproton
def sumUpTo(n):
    '''recursive funtion that return sum of natural numbers 
    up to n'''
    if n == 1:
        return n
    else: 
        return n + sumUpTo(n-1)
    
#taking input from user
inputNumber = int(input("Enter a number:"))

try:
    sumUpTo(inputNumber)
except RuntimeError: 
    print "Value must 1 or more"
#you must specify which error you would expect


