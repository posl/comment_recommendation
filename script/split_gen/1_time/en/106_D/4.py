def main():
    n, m, q = map(int, input().split())
    trains = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        l, r = map(int, input().split())
        trains[l][r] += 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            trains[i][j] += trains[i][j - 1]
    for _ in range(q):
        p, q = map(int, input().split())
        ans = 0
        for i in range(p, q + 1):
            ans += trains[i][q] - trains[i][p - 1]
        print(ans)
