def getABCProblemCount(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8
n = int(input())
print(getABCProblemCount(n))
