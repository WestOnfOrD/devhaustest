# ~Foreword~
# Because of the requested tests I felt it was prudent
# to break down the classic Fizzbuzz into smaller functions.
# This allows the testing to more closely resemble how I would
# expect tests to be written within production code.

# I believe it's a common problem that engineers, when given
# a simple problem, will tend to overengineer their solution
# until it becomes a complicated problem - a kind of derivative
# of Parkinson's Law. This is my acknowledgement in absentia should
# the person reviewing this code be very critical of overlong solutions. 
# 
# I have no similar defense for overlong comments...

#Some useful constants
devhaus = "Devhaus"
learning = "Learning"
model = "Model"
    
# Checks number's divisibility and returns corresponding string
# int i: the number to check
# returns string converted from i based on stated rules
def checkbuzz(i): #This would look nicer if there was a "5 and 7" scenario.
    byThree = i % 3 == 0
    byFive = i % 5 == 0
    bySeven = i % 7 == 0
    
    result = ""
    if byThree:
        result += devhaus
        if byFive:
            result += " " + learning
        if bySeven:
            result += " " + model
    elif byFive:
        result += learning
    elif bySeven:
        result += model
    else:
        result += str(i) #converts integer to string i.e. 13 => "13"
    
    return result

# Generates list of strings from 1 to n (inclusive)
# int n: top number range (inclusive) 
# returns list of strings 
def genbuzz(n):
    resultStrings = []

    for i in range(1, n+1):
        resultStrings.append(checkbuzz(i))
    
    return resultStrings

# Prints each element of theList with a new line in between.
def printbuzz(theList):
    for string in theList:
        print(string)

# Fizzbuzzes from 1 to n (inclusive)
# int n: top number range (inclusive)
# prints to std out
def fizzbuzz(n):
    result = genbuzz(n)
    printbuzz(result)