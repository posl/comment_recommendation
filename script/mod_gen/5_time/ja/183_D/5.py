def solve():
    N, W = map(int, input().split())
    imos = [0] * (2 * 10 ** 5 + 1)
    for _ in range(N):
        s, t, p = map(int, input().split())
        imos[s] += p
        imos[t] -= p
    for i in range(2 * 10 ** 5):
        imos[i + 1] += imos[i]
        if imos[i + 1] > W:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()