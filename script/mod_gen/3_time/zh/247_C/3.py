def printS(n):
    if n == 1:
        return "1"
    else:
        return printS(n-1) + " " + str(n) + " " + printS(n-1)
n = int(input())
print(printS(n))
