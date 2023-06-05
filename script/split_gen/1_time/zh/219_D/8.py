def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0 for i in range(y+1)] for j in range(x+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k] == 1:
                    dp[min(j+a[i], x)][min(k+b[i], y)] = 1
    ans = 0
    for i in range(1, n+1):
        if dp[min(x*i, x)][min(y*i, y)] == 1:
            ans = i
            break
    print(ans)
