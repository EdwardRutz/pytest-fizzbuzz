import pytest

# Function states "Fizz" for numbers that are multiples of 3, "Buzz" for multiples of 5 and 
# "FizzBuzz" for multioples of 3 and 5.
def fizzBuzz( value ):
  if value == 3:
    return "Fizz"
  return str(value)



######## TESTS ########


# Create a utility function to be used by the testsFunction
# Function checks fizzBuzz value and expected return value
def checkFizzBuzz( value, expectedReturnValue ):
  returnValue = fizzBuzz(value)
  assert returnValue == expectedReturnValue


# Get "1" when I pass in 1
def test_returns1With1PassedIn():
  checkFizzBuzz (1, "1")
  
# Get "2" when I pass in 2
def test_returns2With2PassedIn():
  checkFizzBuzz (2, "2")
  
# Get "Fizz" when I pass in 3
def test_returnsFizzWith3PassedIn():
  checkFizzBuzz(3,"Fizz")

# Get "Buzz" when i pass in 5
# Get "Fizz" when I pass in 6 (a multiple of 3)
# Get "Buzz" when I pass in 10 (a multiple of 5)
# Get Fizz Buzz when I pass in 15 (a multiple of 3 and 5)
