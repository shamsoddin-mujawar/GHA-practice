import os
import subprocess

from common.second import fun

num1 = os.getenv('INPUT_A')
num2 = os.getenv('INPUT_B')
cmd = "pwd"
subprocess.call(cmd, shell=True)
s = fun(num1, num2)
print(s)
