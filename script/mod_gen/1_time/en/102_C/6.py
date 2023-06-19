def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = [a[i] - i - 1 for i in range(n)]
    a.sort()
    b = a[n//2]
    print(sum([abs(a[i]-b) for i in range(n)]))
solve()
