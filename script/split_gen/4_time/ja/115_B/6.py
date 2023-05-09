def solve():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))
