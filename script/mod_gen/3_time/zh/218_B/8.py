def printStr(p):
    str = ""
    for i in range(len(p)):
        str = str + chr(p[i]+96)
    print(str)
p = list(map(int, input().split()))
printStr(p)
