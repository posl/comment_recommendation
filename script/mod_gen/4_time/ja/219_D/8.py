def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    dp = [[False for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = True
    for a, b in ab:
        for i in range(x-a, -1, -1):
            for j in range(y-b, -1, -1):
                if dp[i][j]:
                    dp[i+a][j+b] = True
    ans = float('inf')
    for i in range(x+1):
        for j in range(y+1):
            if dp[i][j]:
                ans = min(ans, i+j)
    print(ans if ans != float('inf') else -1)

if __name__ == '__main__':
    main()