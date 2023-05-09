def solve():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    p[0] = p[0] // 2
    print(sum(p))
