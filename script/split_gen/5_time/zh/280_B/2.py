def solve():
    n = int(input())
    s = [int(i) for i in input().split()]
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(' '.join(str(i) for i in a))
