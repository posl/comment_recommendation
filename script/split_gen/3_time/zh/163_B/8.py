def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
        return
    print(n - sum(a))
