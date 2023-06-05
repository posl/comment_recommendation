def getStr(str, begin, end):
    return str[begin-1:end]
str = 'atcoder'
begin, end = map(int, input().split())
print(getStr(str, begin, end))
