def getStr(s, start, end):
    return s[start-1:end]
s = input()
l, r = map(int, input().split())
print(getStr(s, l, r))
