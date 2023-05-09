def main():
    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ((xys[j][0] - xys[i][0]) * (xys[k][1] - xys[i][1]) - (xys[k][0] - xys[i][0]) * (xys[j][1] - xys[i][1])) != 0:
                    ans += 1
    print(ans)
