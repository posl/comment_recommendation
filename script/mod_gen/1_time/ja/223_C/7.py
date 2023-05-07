def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    L = 0
    R = 100000000
    while R - L > 0.0000000001:
        M = (L + R) / 2
        t = 0
        for i in range(N):
            t += AB[i][0] / (AB[i][1] + M)
        if t >= M:
            L = M
        else:
            R = M
    print(L)

if __name__ == '__main__':
    solve()