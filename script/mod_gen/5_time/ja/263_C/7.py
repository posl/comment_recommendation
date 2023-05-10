def solve():
    from itertools import combinations
    N,M = map(int,input().split())
    for i in combinations(range(1,M+1),N):
        print(*i)
solve()

if __name__ == '__main__':
    solve()