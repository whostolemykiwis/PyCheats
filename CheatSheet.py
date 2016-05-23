print ("intro to python cheat/learing sheet")
print ('-----------------------')

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
print (myList[1])#prints 2nd value in list (8)

#working with strings ----------------------------------------------------------------------------------------------------
testString = "hello world!"
print (len(testString))#prints length of string (12)
print (testString.index("o")) #finds the first index of the letter 'o' (4)
print (testString.count("o"))# counts how many o's in the string (2)

#general form [start:stop:step]
print (testString[3:7])#splices string from index 3 to 7 (lo w)
print (testString[:7])#splices string from begining to 7th index (hello w)
print (testString[3:])#splices string from 3rd index to end (lo world!)
print (testString[-3:])#splices string from 3rd index from the end to end (ld!)
print (testString[3:11:2])#splices stirng from 3rd to 7th but skips every other(l ol)
print (testString[::-1])#reverses order of string

print (testString.upper())#string to all upper
#string.lower() goes all lower

#returns boolean (True/False)
print (testString.startswith("hello"))# checks if string starts with 'hello'
print (testString.endswith("world!"))#checks from right to left if strings are ==

#Takes index with that value removes it and splits the string into sections around that indes with that value 
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
print ("%s is %d years old." % (Name, Age)) #prints: Bill is 32 years old.
print ("%s this is my list" % myList)#works with lists too

#math ops ----------------------------------------------------------------------------------------------------------------------
number = 1 + 2 * 3 / 4.0 # basic math all works (2.5)
#^^ number is a floating-point because it was operated by a floating-point

mod = 11 % 3 # mod is = to 2... this is the remainder 
squared = 7 ** 2
cubed = 2 ** 3

# you can make a string equal to whatever is in "" times a multiple
# you can also print things this way
lotsOfHellos = "hello" * 10
print ("hey there " * 10)# prints 'hey there '  ten times

#conditons ---------------------------------------------------------------------------------------------------------------------------------------

# == is different that =... == checks for truth
x = 2
print (x == 2) # prints out True
print (x == 3) # prints out False
print (x < 3)  # prints out True

#if, else, elif, in, is, not 
name = "John"
age = 23
#ex of and operator
if name == "John" and age == 23:
    print ("Your name is %s, and you are also %d years old." %(name, age))
#ex of or operator 
if name == "John" or name == "Rick":
    print ("Your name is either John or Rick.")

#'in' operator
if name in ["John", "Rick"]:
    print ("your name is either John or Rick")#Checks to see if the var is in some list

#if statements
#x = 2
if x == 2: #need boolean equals
    print ("x equals 2")
else:
    print "x doesnt equal 2"
    
#is operator
list1 = [1,2,3]
list2 = [1,2,3]
print (x == y) #will be true because '==' matches values in list to see if =
print (x is y)
