def solve():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    print(sum(p) - p[-1]//2)
solve()
