def solve():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(sum(p) - p[-1]//2)
