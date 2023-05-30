def solve(n, a):
    p = 0
    for i in range(n):
        p += a[i]
        if p == 0:
            p += 1
        elif p == 1:
            p += 2
        elif p == 2:
            p += 3
        elif p == 3:
            p += 4
        if p >= 4:
            p -= 4
    return p
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
