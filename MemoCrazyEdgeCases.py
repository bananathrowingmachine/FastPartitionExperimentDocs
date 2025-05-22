import random

"""
Solves the partition problem using a top down dynamic programming algorithm, which is an algorithm that recurses but it stores results of solved subproblems and refers back to them if needed.
This version however uses a "abs-value trick" that I independently discovered to help speed things up (or that's at least what I'm creating the entire complexity experiment to test). 
Out of all the versions of partition, this is the one that is the most my own, as the crazy math is my own, while the general partition/subset sum algorithm itself is written by Jeff Erickson and then translated for this experiment.

This partition algorithm is mostly just Jeff Erickson's Subset Sum algorithm with a reverse memoization order, like 2 extra things, then the crazy math translation into a solution to partition.
His version can be found in Chapter 3, pages 116 and 117 in his free online algorithms textbook located here: http://algorithms.wtf/

Made by bananathrowingmachine on May 9th, 2025.
"""
class MemoizedCrazy:
    """
    This is a class solely to make interationCount effectively pass by reference. Storing the answer map and input list is just an extra bonus.
    """
    def __init__(self, inputList: list[int]):
        """
        Creates a "pass by reference" integer and then also stores the absolute list and answer map for ease of use.

        :param inputList: The inputted list, which will mapped to a list of absolute values in the input.
        """
        self.absoluteList = list(map(abs, inputList))
        self.answerMap: dict[tuple[int, int], bool] = {}

    @classmethod
    def testIterations(cls, inputList: list[int]) -> tuple[int, bool]:
        """
        Tests the iteration count of a very slightly modified subset sum that uses top down dynamic programming with a bit of extra input and output code to produce an answer to partition for the same input.

        :param inputList: The inputted list, which will mapped to a list of absolute values in the input internally.
        :return: A tuple containing the iteration count, and the computed answer.
        """
        solver = cls(inputList)
        if sum(inputList) % 2 == 1:
            return 0, False
        if sum(inputList) == 0:
            return 0, True
        if max(solver.absoluteList) > sum(solver.absoluteList)/2:
            return 0, False
        result = solver.subsetSum(0, int(sum(inputList)/2))
        return len(solver.answerMap), result # Since the answer map is added to each recursive call, it's length is an iteration count.

    def subsetSum(self, index, goal) -> bool:
        """
        Recursively solves the subset sum problem with inputs for partition. 

        :param index: The current index of the list the algorithm is considering.
        :param goal: The current goal the algorithm needs to reach to find a valid answer.
        :return: A boolean of if the set (list) can be partitioned.
        """
        if goal == 0:
            return True
        if index >= len(self.absoluteList):
            return False
        
        
        if goal >= self.absoluteList[index]: # Bounds checking, better than the others though as it can use the current goal.
            if (index + 1, goal-self.absoluteList[index]) in self.answerMap:
                take = self.answerMap[(index + 1, goal-self.absoluteList[index])]
            else:
                take = self.subsetSum(index + 1, goal-self.absoluteList[index])
            if take == True:
                self.answerMap[(index, goal)] = True
                return True

        if (index + 1, goal) in self.answerMap:
            skip = self.answerMap[(index + 1, goal)]
        else:
            skip = self.subsetSum(index + 1, goal)
        
        self.answerMap[(index, goal)] = skip
        return skip
    
inputList = [1 for _ in range(100)] 
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [i for i in range(50)] 
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2 ** i for i in range(25)]
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2**i + (-1)**i for i in range(25)]
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [i % 17 for i in range(100)] 
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [11, 13, 17, 19, 29, 31, 41, 43] 
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [3 for _ in range(33)] + [1] 
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == False else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")

inputList = [2**i + (-1)**(i+1) for i in range(25)]
print(len(inputList))
result = MemoizedCrazy.testIterations(inputList)
output = ("Trivial!" if result[0] == 0 else result[0], result[1], "Correct" if result[1] == True else "Incorrect")
print(output)
print("max = " + str(2 ** len(inputList)) + "\n")