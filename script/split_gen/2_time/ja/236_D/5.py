def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            b[i] ^= a[i][j]
    ans = 0
    for i in range(1, 1<<n):
        tmp = 0
        for j in range(n):
            if (i>>j)&1:
                tmp ^= b[j]
        ans = max(ans, tmp)
    print(ans)
