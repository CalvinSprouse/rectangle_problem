import random
import time

def findLargestRect(numList: []):
    ansList = []
    ansList.append(len(numList)*min(numList))

    if len(numList) > 1:
        newLists = split_list(numList, min(numList))

        for nList in newLists:
            responses = findLargestRect(nList)

            for item in responses:
                ansList.append(item)
    return ansList

def split_list(input_list, seperator):
    outer = []
    inner = []
    for elem in input_list:
        if elem == seperator:
            if inner:
                outer.append(inner)
            inner = []
        else:
            inner.append(elem)
    if inner:
        outer.append(inner)
    return outer

if __name__ == "__main__":
    maxVal = 100000000
    nums = maxVal
    numList = [random.randrange(0, maxVal, 1) for i in range(nums)]

    start = time.time()
    answers = findLargestRect(numList)
    end = time.time()

    # print(numList)
    print(max(answers))
    print(end-start)
