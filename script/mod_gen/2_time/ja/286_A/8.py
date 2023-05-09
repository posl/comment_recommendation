def swapList(numList, start, end):
    tmpList = numList[start:end]
    tmpList.reverse()
    numList = numList[:start] + tmpList + numList[end:]
    return numList

if __name__ == '__main__':
    swapList()