def solve():
    a, b, k = map(int, input().split())
    comb = [[1] * (a + b + 1) for _ in range(a + b + 1)]
    for i in range(1, a + b + 1):
        for j in range(1, i):
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
    ans = []
    while a + b > 0:
        if a > 0:
            if k <= comb[a + b - 1][a - 1]:
                ans.append('a')
                a -= 1
            else:
                ans.append('b')
                b -= 1
                k -= comb[a + b][a]
        else:
            ans.append('b')
            b -= 1
    print(''.join(ans))
solve()

if __name__ == '__main__':
    solve()