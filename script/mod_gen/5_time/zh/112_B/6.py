def solve():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        ci, ti = map(int, input().split())
        c.append(ci)
        t.append(ti)
    min_cost = 1001
    for i in range(N):
        if t[i] <= T and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == 1001:
        print('TLE')
    else:
        print(min_cost)

if __name__ == '__main__':
    solve()