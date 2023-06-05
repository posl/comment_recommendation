def func(s):
    for i in s:
        if s.count(i)==1:
            return i
    return -1
s=input()
print(func(s))
