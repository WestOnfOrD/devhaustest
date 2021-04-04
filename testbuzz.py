import fizzbuzz

#Some constants for testing correctness.
divByThree = "Devhaus"
divByFive = "Learning"
divBySeven = "Model"
divByThreeAndFive = "Devhaus Learning"
divByThreeAndSeven = "Devhaus Model"
divByThreeAndFiveAndSeven = "Devhaus Learning Model"

def printTestResult(description, result):
    passedString = "passed" if result else "failed"
    print(description + ": " + passedString)

# First, we'll check if our code is correctly
# converting integers into their corresponding
# strings based on that integer's divisibility
def test01_checkIntToString():
    testList = [] #tuple(string description, bool result)
    testList.append(("div by 3", divByThree == fizzbuzz.checkbuzz(3)))
    testList.append(("div by 5", divByFive == fizzbuzz.checkbuzz(5)))
    testList.append(("div by 7", divBySeven == fizzbuzz.checkbuzz(7)))
    testList.append(("div by 3 and 5", divByThreeAndFive == fizzbuzz.checkbuzz(15)))
    testList.append(("div by 3, 5, and 7", divByThreeAndFiveAndSeven == fizzbuzz.checkbuzz(105)))
    testList.append(("not divisible by 3, 5, or 7", "4" == fizzbuzz.checkbuzz(4)))
    
    # In production code we could include some additional tests for 
    # 0 and negative values, perhaps very large or smaller values.
    # While not part of expected functionality, it's easy to test
    # and could prevent bugs further down the line

    result = True
    for test in testList:
        printTestResult(test[0], test[1])
        result &= test[1]
    printTestResult("test01_checkIntToString", result)

# Next, we'll check to make sure that the correct
# number of values are actually being generated
def test02_checkNumIterations():
    testList = [] #tuple(string description, bool result)
    testList.append(("expected 5 results", 5 == len(fizzbuzz.genbuzz(5))))
    testList.append(("expected 6 results", 6 == len(fizzbuzz.genbuzz(6))))
    testList.append(("expected 105 results", 105 == len(fizzbuzz.genbuzz(105))))

    # Production code could include tests for very large values,
    # as well as zero and negative values.

    result = True
    for test in testList:
        printTestResult(test[0], test[1])
        result &= test[1]
    printTestResult("test02_CheckNumIterations", result)

# A more general purpose test to check more wholistic correctness
def test03_checkOrderAndCorrectness():
    expectedList = ["1", "2", divByThree, "4", divByFive, divByThree, divBySeven]

    fizzList = fizzbuzz.genbuzz(7)
    result = True
    for i in range(0, len(fizzList)):
        result &= fizzList[i] == expectedList[i]
    
    printTestResult("test03_CheckOrderAndCorrectness", result)

def runAllTests():
    test01_checkIntToString()
    test02_checkNumIterations()
    test03_checkOrderAndCorrectness()

runAllTests()
