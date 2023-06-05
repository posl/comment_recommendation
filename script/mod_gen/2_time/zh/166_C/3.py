def solve():
    n, k = map(int, input().split())
    snukes = [0 for i in range(n)]
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for i in range(d):
            snukes[a[i]-1] += 1
    print(snukes.count(0))
solve()
