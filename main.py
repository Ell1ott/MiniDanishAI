words = ["jeg", "fordi", "har", "en", "et", "mælk", "hus"]

import random
from time import sleep

weights = [
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
    ]



startIndex = -1
while True:
    startingWord = input("Første ord: ")
    
    if(startingWord in words):
        startIndex = words.index(startingWord)
        break
    else:
        print("Jeg kender ikke " + startingWord)
        

def getInput(lastWordIndex):
    input = [0, 0, 0, 0, 0, 0, 0]
    input[lastWordIndex] = 1
     
    return input 

def getOutput(input):
    output = [0, 0, 0, 0, 0, 0, 0]
    
    for a in range(7):
        
        iOutput = 0
        
        for b in range(7):
            iOutput += weights[b][a] * input[b]
        output[a] = iOutput
    return output
    

def get_indexes_of_max_values(lst):
    max_value = max(lst)
    indexes = [index for index, value in enumerate(lst) if value == max_value]
    return indexes

def chooseBestIndex(output):
    return random.choice(get_indexes_of_max_values(output))

bestIndex = startIndex

print(startingWord, end=" ")

for i in range(100):
    bestIndex = chooseBestIndex(getOutput(getInput(bestIndex)))
    print(words[bestIndex], end=" ", flush=True)
    sleep(0.5)


        


