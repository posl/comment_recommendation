def solve():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    d = {}
    for s in S:
        d[s] = 'No'
    for t in T:
        d[t] = 'Yes'
    for s in S:
        print(d[s])

if __name__ == '__main__':
    solve()