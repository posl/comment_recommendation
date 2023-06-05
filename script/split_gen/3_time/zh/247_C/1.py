def printS(n):
    if n == 1:
        print(1,end=' ')
    else:
        printS(n-1)
        print(n,end=' ')
        printS(n-1)
n = int(input())
printS(n)
print()
