def swapList(numList, start, end):
    tmpList = numList[start:end]
    tmpList.reverse()
    numList = numList[:start] + tmpList + numList[end:]
    return numList
