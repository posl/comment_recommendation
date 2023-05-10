def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = -1
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                a[i][j] += a[i][j-1]
            elif j == 0:
                a[i][j] += a[i-1][j]
            else:
                a[i][j] += max(a[i-1][j], a[i][j-1])
            ans = max(ans, a[i][j])
    print(ans)
