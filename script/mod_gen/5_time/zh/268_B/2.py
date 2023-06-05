def func(s,t):
    if t.startswith(s):
        return 'Yes'
    else:
        return 'No'
s = input()
t = input()
print(func(s,t))
