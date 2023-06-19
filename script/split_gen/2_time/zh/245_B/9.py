def f():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = []
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])
    for i in range(len(b)):
        if b[i] != i:
            print(i)
            return
    print(len(b))
f()
