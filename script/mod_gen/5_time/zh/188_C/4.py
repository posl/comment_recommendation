def f(a):
    if len(a) == 1:
        return a[0]
    elif len(a) == 2:
        return max(a[0], a[1])
    else:
        b = []
        for i in range(0, len(a), 2):
            if a[i] > a[i+1]:
                b.append(a[i])
            else:
                b.append(a[i+1])
        return f(b)
n = int(input())
a = []
for i in range(2**n):
    a.append(int(input()))
b = []
for i in range(0, len(a), 2):
    if a[i] > a[i+1]:
        b.append(a[i+1])
    else:
        b.append(a[i])
print(a.index(f(b)) + 1)
