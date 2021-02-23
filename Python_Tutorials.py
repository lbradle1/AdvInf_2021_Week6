####################################################
## Python Tutorial Video 1 - Variables and Strings## 
####################################################

#variables have no quotes and don't need to use print()
a = 1
a 

# strings have quotes don't need print() to see
c = "hello world"
c

# can assign variables to eachother
# f doesn't = a, it equals what a refers to, so 1
f = a
f

# if i now change a, f doesn't change
a = 2
f # stays 1, when we assigned f = a, a refered to 1 so f = 1, not a

g = c # g is "hello world" NOT c
c = "hello" # change c, g stays "hello world"
g # = "hello world still"
#ORDER MATTERS IN COMPUTING 

#Switching variables
v1 = "first string"
v2 = "second string"

#how to switch these variables
# can't just do
# v1 = v2, v2 = v1
# this will make 1st v1 = "second string"
# then v2 = v1 makes v2 ALSO equal "second string"

#solution
x = v1 # x is 'first string'
y = v2 # y is "second string"

v1 = y #v1 now equals 'second string'
v2 = x #v2 = 'first string'

# OR
x = v1 # x now = 'first strging'
v1 = v2 # v1 = 'second string'
v2 = x # v2 = 'first string'
## REMEMBER ORDER MATTERS ## 

#################################################
## Python Tutorial Video 2 - If Else Statements## 
#################################################

# will print string only if statement is true
a = 1
b = 2
if a < b:
    print("a is less than b") 

# If / Else - prints first string if true, 2nd if false
c = 3 
d = 4
if c < d:
    print("c is less than d")
else:
    print("c is NOT less than d")

# What about for multiple cases
# in this case 'elif' adds another IF/ELSE statement
# if the first IF statement is flase 
    # == indicates evaluating not assigning 
e = 9
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
else:
    print("e is greater than f")

# Adding if/else statement within an if/else clause 
g = 9
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")

# Example - create a BMA calculator
name = "YK"
height_m = 2
weight_kg = 90
bmi = weight_kg / (height_m ** 2) # **is squared
if bmi < 25:
    print("bmi:")
    print(name)
    print(bmi)
    print("not overweight")
else:
    print("bmi:")
    print(name)
    print(bmi)
    print("overweight")


############################################
## Python Tutorial Video 3 - Use Functions##
############################################

# define a function
def function1():
    print("ahhh")
    print("ahhh 2")
print("this is a outside the function")

#call a function - can run this multiple times in a row
function1()

# can be a mapping
# maps the input x to the output 2*x
def function2(x):
    return 2*x
# can use this as an argument 
a = function2(3)
# a now = 6, this is a return value or output 

# multiple arguments in single finction 
def function3(x, y):
    return x + y
e = function3(1, 2) # e is 3 

def function4(x):
    print(x)
    print("still inside this function")
    return 3*x
f = function4(4) # this prints whats in the funtion
f # f is 12

# BMI calculator for multiple people

#info of 3 people 
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK brother"
height_m3 = 2.5
weight_kg3 = 160

#this function (bmi_calc) when given the arguments (name, height_m, weight_kg)
# will output "bmi: , the persons bmi, and if they are overweight or not 
def bmi_calc(name, height_m, weight_kg):
    bmi = weight_kg / (height_m **2)
    print("bmi:")
    print(bmi)
    if bmi < 25:
        return name + " not overweight"
    else:
        return name + " overweight"

#see if YK is overweight 
# can use just the function to see all outputs
bmi_calc(name1, height_m1, weight_kg1)
#if assign it to something shoes just the "print" stuff
result1 = bmi_calc(name1, height_m1, weight_kg1)
#then result returns the if/else statement
result1

#####################################
##Python Tutorial Video 4 - LISTS ###
#####################################

# square brackets
a = [3, 10, -1]

# add an item, adds 1 to end of list
# append is command so x.append 
a.append(1)

#add a string to end of list, or a list within a list!
a.append("hello")
a.append([1,2])

#DELETE an item with .pop - deletes last item
a.pop()

#retrieve specific item 
#first item in list is 0, 2nd is 1
a[0]

#change content of list
#first select item with a[x], then assign 
a[0] = 100

#lsit with 3 strings, switch 1st and 3rd values 
b = ["banana", "apple", "google"]
x = b[0]
b[0] = b[2]
b[2] = x
#>>> b
#    ['google', 'apple', 'banana']
#SHORTCUT
b[0], b[2] = b[2], b[0]


########################################
##Python Tutorial Video 5 - For Loops ##
########################################

#make a new list
a = ["banana", "apple", "google"]

#for loop can do the same thing through all elements in a list
#saves time - automate a task
## dont need to use word element - arbitrary 

# make a script to print each element in list 'a'
for element in a:
    print(element)

#make list of numbers, find sum of list
# this takes orig total (0), and adds it to e (20)
# this is then new total (20), which is added to NEXT e (10)
# NEW total (30), added to NEXT e (5) - gives FINAL total
#because were all the way through the list 
b = [20, 10, 5]
total = 0
for e in b:
    total = total + e
b

# list converts range to list 
c = list(range(1,5)) #creates range of #'s from 1-5 not including 5

# i is colloquial for iterations
for i in range(1, 5):
    print(i)

# find totals of this list
total2 = 0
for i in range(1,5):
    total2 += i # += is shortcut for old value plus new =

#example
# make a list 1-7
list(range(1, 8))

#find sum of only multiples of 3
# need to learn a modulo operator
    # ex 4 % 3 - divide 4 by 3
    # gives value 1, which is the REMAINDER 
    # if i is mult of 3 then remainder is 0
total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i            

# PRACTICE 
# compute all multiples of 3, 5, that are <100

total4 = 0
for i in range (1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total4 += i
total4 # = 2318



#################################################################
##Python Tutorial Video 6 - While Loops and The Break Statement##
#################################################################

# review a basic for loop
total = 0
for i in range (1, 5):
    total += i
print(total)

#while loops
#if you don't know how many loops you need beforehand 
total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)

# for example, summation of only the positive integers in a list 
given_list = [5 ,4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while given_list[i] > 0:
    total3 += given_list[i]
    i += 1 
print(total3)

#use a for loop instead of a why loop to add only positive integers
# need to use a BREAK statement  
given_list2 = [5 ,4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
    if element <= 0:
        break
    total4 += element
print(total4)

#while loop with break 
total5 = 0
i = 0
while True:
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break
print(total5)



###############################
###VIDEO 7 some practice ######
###############################

#Practice problem - find sum of neg numbers 
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0
j = len(given_list3) - 1
while given_list3[j] < 0:
    total += given_list3[j]
    j -= 1
print(total)

################################
#### VIDEO 8 - Dictionaries ####
################################

# think of it like a look-up table 
# values associated with a string  

# assigns new empty dictionary d
d = {}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

print(d["Tom"])

# can change a value
d["Jenny"] = 20

#keys are usually strings or numbers


###################################
### VIDEO 9 CLASES AND OBJECTS ####
###################################

# create a class
class Robot:
    def introduce_self(self):
        print("My name is " + self.name)

#create new object with class Robot
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r1.introduce_self()

# create a constructor, make the stuff for you 
  class Robot:
    def __init__ (self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

#makes specifying attribute stuff much cleaner
r1 = Robot("Tom", "red", 30)
r1.introduce_self()

###########################################
### VIDEO 10 CLASSES AND OBJECTS AGAIN ####
###########################################

class Robot:
    def __init__ (self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

#classify ownership of robots 
p1.robot_owned = r2
p2.robot_owned = r1

##########################
## VIDEO 11 BOOLEAN ######
##########################

#another type of data like strings and integers
#only two possible value T or F

type() # allows us to see type of any value 

if a > b:
    print("a is greater than b")

if True:
    print("a is greater than b")

boolean_value = a > b

#write function called are you sad
def are_you_sad(is_rainy, has_umbrella):
    if is_rainy == True and has_umbrella == False:
        return True
    else:
        return False

# can also write 
def are_you_sad(is_rainy, has_umbrella):
    if is_rainy and not has_umbrella:
        return True
    else:
        return False

# can simplify more 
def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella

# are you sad if it's rainy and you dont have an umbrella      
are_you_sad(True, False)

# practice
def c_greater_than_d_plus_e(c, d, e):
    return c > d + e 

c_greater_than_d_plus_e(3, 1, 1)



