def getStr(str, start, end):
    return str[start-1:end]
str = "atcoder"
start, end = map(int, input().split())
print(getStr(str, start, end))
