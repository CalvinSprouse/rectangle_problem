import random
import time

def findLargestRect(numList: []):
    # ans list will be returned after editing
    ansList = []

    # find the minimum value, used for breaking list later
    minVal = min(numList)

    # add the longest rectangle possible with current list
    ansList.append([len(numList)*minVal, numList])

    # acts as an end condition for recursion
    if len(numList) > 1:
        # create new lists from split function, sep=minVal
        newLists = splitList(numList, minVal)

        for nList in newLists:
            # recursive step to get ansList from sublists
            responses = findLargestRect(nList)

            # potential area for optimization?
            # perhaps append/store responses directly/more efficiently
            for item in responses:
                ansList.append(item)

    # pass back a list of answers (answers are areas)
    return ansList

def splitList(inList: [], seperator: int):
    """Split a list based on a seperator input (does note include sperator)"""

    # result stores the lists to return
    # inner is the "working" list
    # items are appended 1 by 1 to inner
    # until the cursor hits a seperator
    # then inner is appended to result and inner is reset
    result = []
    inner = []

    # iterates over each element
    for elem in inList:
        # if the element is the seperator
        # inner append to result and inner reset
        if elem == seperator:
            if inner:
                result.append(inner)
            inner = []
        # otherwise the element is added to inner
        else:
            inner.append(elem)

    # inner is appended again to result
    # to ensure last section of list is captured
    if inner:
        result.append(inner)
    return result


if __name__ == "__main__":
    nums = 10 # number of numbers/length of initial list
    maxVal = nums # maximum value each number can take in list
    minVal = 1 # removing 0 produces more interesting results

    # in most cases setting maxVal to be >> or << than nums
    # produces uninteresting results (super long rect or super tall)

    # generate the list of numbers with above conditions
    numList = [random.randrange(minVal, maxVal, 1) for i in range(nums)]

    # run test (timing after list generation)
    print(f"Starting Test Length={maxVal} MaxVal={nums}")
    print(f"Nums List = {numList}") # comment out for large numLists
    print("")
    start = time.time()
    answers = findLargestRect(numList)
    end = time.time()

    # parse for largest rectangle
    ans = []
    ansMax = 0
    for response in answers:
        print(f"Rectangle Found: {response}")
        if response[0] > ansMax:
            ans = response
            ansMax = response[0]
    print(f"\nLargest Rectangle={ans}\nFound in: {end-start}s")
    print(f"From Nums List {numList}") # comment out for large numLists
