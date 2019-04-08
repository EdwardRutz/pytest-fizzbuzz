import pytest

# Function states "Fizz" for numbers that are multiples of 3, "Buzz" for multiples of 5 and 
# "FizzBuzz" for multioples of 3 and 5.
def fizzBuzz( value ):
  return str(value)



######## TESTS ########


# Can I call FizzBuzz
def test_canCallFizzBuzz():
  fizzBuzz(1) 
  
# Get "1" when I pass in 1
def test_returns1With1PassedIn():
  returnValue = fizzBuzz(1)
  assert returnValue == "1"
  
# Get "2" when I pass in 2
def test_returns2With2PassedIn():
  returnValue = fizzBuzz(2)
  assert returnValue == "2"

# Get "Fizz" when I pass in 3
# Get "Buzz" when i pass in 5
# Get "Fizz" when I pass in 6 (a multiple of 3)
# Get "Buzz" when I pass in 10 (a multiple of 5)
# Get Fizz Buzz when I pass in 15 (a multiple of 3 and 5)
