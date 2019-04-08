import pytest

# Function states "Fizz" for numbers that are multiples of 3, "Buzz" for multiples of 5 and 
# "FizzBuzz" for multioples of 3 and 5.
def fizzBuzz( value ):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)

# A utility method to see if a number has a remainder of 0.
def isMultiple(value, multiple):
    return (value % multiple) == 0


######## TESTS ########


# Create a utility function to be used by the testsFunction
# Function checks fizzBuzz value and expected return value
def checkFizzBuzz( value, expectedReturnValue ):
    returnValue = fizzBuzz(value)
    assert returnValue == expectedReturnValue


# Pass in 1 and get "1"
def test_returns1With1PassedIn():
    checkFizzBuzz (1, "1")
  
 #  Pass in 2 and get "2"
def test_returns2With2PassedIn():
    checkFizzBuzz (2, "2")
  
 #  Pass in 3 and get "Fizz"
def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3,"Fizz")

# Pass in 5 and get "Buzz"
def test_returnBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

# Get "Fizz" when I pass in 6 (a multiple of 3)
def test_returnFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

# Get "Buzz" when I pass in 10 (a multiple of 5)
def test_returnBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

# Get Fizz Buzz when I pass in 15 (a multiple of 3 and 5)
def test_returnFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")









