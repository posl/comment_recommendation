def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[False for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k] and j+a[i] <= x and k+b[i] <= y:
                    dp[j+a[i]][k+b[i]] = True
    for j in range(x, -1, -1):
        for k in range(y, -1, -1):
            if dp[j][k]:
                print(j+k)
                exit()
    print(-1)
