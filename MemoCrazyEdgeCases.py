"""
This uses the current iteration of the New Memoized Crazy file from my GitHub and runs it against a bunch of worst case scenario sets.
Definitely still working on this it's by no means finished.

Made by bananathrowingmachine on Nov 24th, 2025.
"""
import importlib
from inputimeout import TimeoutOccurred, inputimeout

def getModuleSource(localMode):
    """
    Allows for the choice of either pulling the module from my pc on github, allowing me to easily test many different versions.

    :param localMode: If localMode is to be enabled or not.
    :return: The module of code.
    """
    if localMode:
        import os
        with open(os.path.expanduser('~/vscode/personal/fastPartition/experiment_code/versions/NewMemoizedCrazy.py'), 'r') as f:
            return f.read()
    else:
        import requests
        answer = 'https://github.com/bananathrowingmachine/FastPartitionExperiment/blob/main/experiment_code/versions/NewMemoizedCrazy.py'
        try:
            answer = inputimeout("Please input the link you'd like to use below:\n", 10)
        except TimeoutOccurred:
            print("No input given. Using the current version on my GitHub.")
        response = requests.get(answer + '?raw=true')
        response.raise_for_status()
        return response.text

def getResult(inputList: list[int]) -> tuple[int, bool]:
    """
    Re adds the trivial case checking that was removed when I switched to using a link version. In a full version of this algorithm these trivial cases will need to be added at the start.

    :param inputList: The inputted list, which will mapped to a list of absolute values in the input internally.
    :return: A tuple containing the iteration count, and the computed answer.
    """
    if sum(inputList) % 2 == 1:
        return 0, False
    if sum(inputList) == 0:
        return 0, True
    if max(list(map(abs, inputList))) > sum(list(map(abs, inputList)))/2:
        return 0, False
    return module.NewMemoizedCrazy.testIterations(inputList)

localMode = False
try:
    answer = inputimeout("Run local mode? [Y/N] \n", 10)
    if answer.lower() == "y":
        localMode = True
        print("Running on local mode.")
    else:
        print("Running on online mode.")
except TimeoutOccurred:
    print("Input timeout occured. Defaulting to running on online mode.")
module = type(importlib)('dynamic_module')
exec(getModuleSource(localMode), module.__dict__)

inputList = [1 for _ in range(100)] 
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [i for i in range(50)] 
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2 ** i for i in range(25)]
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2**i + (-1)**i for i in range(25)]
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [i % 17 for i in range(100)] 
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [11, 13, 17, 19, 29, 31, 41, 43] 
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [3 for _ in range(33)] + [1] 
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2**i + (-1)**(i+1) for i in range(25)]
print(len(inputList))
print(inputList)
result = getResult(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")