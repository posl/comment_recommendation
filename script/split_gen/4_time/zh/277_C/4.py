def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    a.sort()
    b.sort()
    if n % 2 == 0:
        print(b[n // 2] - a[n // 2] + b[n // 2 - 1] - a[n // 2 - 1] + 1)
    else:
        print(b[n // 2] - a[n // 2] + 1)
