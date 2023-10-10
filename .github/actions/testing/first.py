import os

from second import fun

num1 = os.getenv('INPUT_A')
num2 = os.getenv('INPUT_B')

s = fun(num1, num2)
print(s)
