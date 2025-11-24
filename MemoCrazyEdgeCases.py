"""
This uses the current iteration of the New Memoized Crazy file from my GitHub and runs it against a bunch of worst case scenario sets.
Definitely still working on this it's by no means finished.

Made by bananathrowingmachine on Nov 23rd, 2025.
"""

import requests
import importlib

response = requests.get("https://github.com/bananathrowingmachine/FastPartitionExperiment/blob/main/experiment_code/versions/OldMemoizedCrazy.py?raw=true")
response.raise_for_status()
module = type(importlib)('dynamic_module')
exec(response.text, module.__dict__)

inputList = [1 for _ in range(100)] 
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [i for i in range(50)] 
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2 ** i for i in range(25)]
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2**i + (-1)**i for i in range(25)]
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [i % 17 for i in range(100)] 
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [11, 13, 17, 19, 29, 31, 41, 43] 
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [3 for _ in range(33)] + [1] 
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2**i + (-1)**(i+1) for i in range(25)]
print(len(inputList))
result = module.OldMemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")