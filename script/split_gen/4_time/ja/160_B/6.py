def exchange(x):
    if x >= 500:
        return 1000
    elif x >= 5:
        return 5
    elif x >= 1:
        return 1
    else:
        return 0
x = int(input())
r = 0
while x > 0:
    r += exchange(x)
    x -= exchange(x)
print(r)
