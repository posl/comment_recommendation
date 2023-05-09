def count_seq(n, m, k):
    c = [[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(n+1):
        c[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            c[i][j] = c[i][j-1] + c[i-1][j] - (c[i-1][j-m-1] if j-m-1 >= 0 else 0)
    return c[n][k]
n, m, k = map(int, input().split())
print(count_seq(n, m, k) % 998244353)

if __name__ == '__main__':
    count_seq()