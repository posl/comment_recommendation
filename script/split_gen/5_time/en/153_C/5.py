def solve():
    n, k = map(int, input().split())
    h = sorted(map(int, input().split()), reverse=True)
    print(sum(h[k:]))
