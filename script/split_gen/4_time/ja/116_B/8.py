def func(s):
    if s % 2 == 0:
        return s // 2
    else:
        return 3 * s + 1
s = int(input())
a = [s]
i = 1
while True:
    if a[i-1] in a[:i-1]:
        print(i+1)
        break
    else:
        a.append(func(a[i-1]))
        i += 1
