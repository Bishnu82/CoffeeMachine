import math
num = 23

# your code here
def override(_):
    print("Don't cheat!")

# don't delete this line, please
math.factorial = override
math.factorial(num)
