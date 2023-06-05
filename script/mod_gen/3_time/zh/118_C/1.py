def solve(n, a):
    a.sort()
    for i in range(n-1):
        if a[i+1] % a[i] == 0:
            a[i+1] = a[i]
        else:
            a[i+1] %= a[i]
    return a[-1]
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
