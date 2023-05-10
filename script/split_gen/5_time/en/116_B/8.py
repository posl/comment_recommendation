def calc(a):
    if a % 2 == 0:
        return a/2
    else:
        return 3*a+1
s = int(input())
a = [s]
i = 1
while True:
    a.append(calc(a[i-1]))
    if a[i] in a[:i]:
        print(i+1)
        break
    i += 1
